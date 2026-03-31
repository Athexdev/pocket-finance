from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta, datetime
from django.core.paginator import Paginator
import csv
import io
from django.http import HttpResponse
from .models import Expense, Category
from .forms import ExpenseForm

def landing_page(request):
    return render(request, 'landing/landing.html')

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'registration/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'registration/register.html')

        try:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully! Please sign in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return render(request, 'registration/register.html')

    return render(request, 'registration/register.html')

@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    
    # Total expenses
    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Current month expenses
    today = timezone.now().date()
    current_month_expenses = expenses.filter(date__year=today.year, date__month=today.month).aggregate(Sum('amount'))['amount__sum'] or 0
    
    # Recent 5 expenses
    recent_expenses = expenses.order_by('-date')[:5]
    
    # Category-wise expense summary for Chart.js
    categories = Category.objects.all()
    category_data = []
    category_labels = []
    
    for category in categories:
        total = expenses.filter(category=category).aggregate(Sum('amount'))['amount__sum'] or 0
        if total > 0:
            category_labels.append(category.name)
            category_data.append(float(total))

    # Daily trend (last 30 days)
    thirty_days_ago = today - timedelta(days=30)
    daily_expenses = expenses.filter(date__gte=thirty_days_ago).values('date').annotate(daily_total=Sum('amount')).order_by('date')
    
    date_labels = []
    date_data = []
    for entry in daily_expenses:
        date_labels.append(entry['date'].strftime('%b %d'))
        date_data.append(float(entry['daily_total']))
            
    context = {
        'total_expenses': total_expenses,
        'current_month_expenses': current_month_expenses,
        'recent_expenses': recent_expenses,
        'category_labels': category_labels,
        'category_data': category_data,
        'date_labels': date_labels,
        'date_data': date_data,
    }
    return render(request, 'expenses/dashboard.html', context)

@login_required
def expense_list(request):
    expenses_list = Expense.objects.filter(user=request.user).order_by('-date')
    categories = Category.objects.all()
    
    # Filtering and Search
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    try:
        category_id = int(category_id) if category_id else ''
        selected_category = [category_id] if category_id else []
    except ValueError:
        category_id = ''
        selected_category = []
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    if search_query:
        expenses_list = expenses_list.filter(title__icontains=search_query)
    if category_id:
        expenses_list = expenses_list.filter(category_id=category_id)
    if start_date:
        expenses_list = expenses_list.filter(date__gte=start_date)
    if end_date:
        expenses_list = expenses_list.filter(date__lte=end_date)
        
    # Pagination
    paginator = Paginator(expenses_list, 10) # 10 expenses per page
    page_number = request.GET.get('page')
    expenses = paginator.get_page(page_number)
    
    context = {
        'expenses': expenses,
        'categories': categories,
        'search_query': search_query,
        'category_id': category_id,
        'selected_category': selected_category,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'expenses/expense_list.html', context)

@login_required
def expense_export(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    
    # Apply the same filters for export
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    try:
        category_id = int(category_id) if category_id else ''
    except ValueError:
        category_id = ''
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    
    if search_query:
        expenses = expenses.filter(title__icontains=search_query)
    if category_id:
        expenses = expenses.filter(category_id=category_id)
    if start_date:
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
        expenses = expenses.filter(date__lte=end_date)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="expenses.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Date', 'Title', 'Category', 'Amount', 'Description'])
    
    for expense in expenses:
        cat_name = expense.category.name if expense.category else 'Uncategorized'
        writer.writerow([expense.date, expense.title, cat_name, expense.amount, expense.description])
        
    return response

@login_required
def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        
        if not csv_file:
            messages.error(request, 'Please upload a CSV file.')
            return render(request, 'expenses/import_csv.html')

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'This is not a CSV file.')
            return render(request, 'expenses/import_csv.html')

        try:
            # Read and decode the file
            data_set = csv_file.read().decode('UTF-8', errors='ignore')
            io_string = io.StringIO(data_set)
            
            reader = csv.reader(io_string, delimiter=',', quotechar='"')
            
            # Skip header
            try:
                next(reader)
            except StopIteration:
                messages.error(request, 'The CSV file is empty.')
                return render(request, 'expenses/import_csv.html')
            
            records_count = 0
            for row in reader:
                if not row or len(row) < 4:
                    continue
                
                try:
                    date_str = row[0].strip()
                    title = row[1].strip()
                    category_name = row[2].strip()
                    amount_str = row[3].strip()
                    description = row[4].strip() if len(row) > 4 else ""

                    # Parsing date (DD-MM-YYYY)
                    date_obj = datetime.strptime(date_str, '%d-%m-%Y').date()
                    
                    # Parsing amount - handle potential commas or currency symbols
                    amount_clean = amount_str.replace('₹', '').replace(',', '').strip()
                    amount = float(amount_clean)
                    
                    # Get or create category
                    category, created = Category.objects.get_or_create(name=category_name)
                    
                    # Create expense
                    Expense.objects.create(
                        user=request.user,
                        category=category,
                        title=title,
                        amount=amount,
                        date=date_obj,
                        description=description
                    )
                    records_count += 1
                except (ValueError, IndexError):
                    continue # skip invalid rows
            
            if records_count > 0:
                messages.success(request, f'Successfully imported {records_count} expenses!')
                return redirect('expense_list')
            else:
                messages.error(request, 'No valid records found in the CSV file.')
        except Exception as e:
            messages.error(request, f'Error importing CSV: {str(e)}')
            
    return render(request, 'expenses/import_csv.html')

@login_required
def expense_add(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Add Expense'})

@login_required
def expense_edit(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Edit Expense'})

@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
        return redirect('expense_list')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense})

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Check which form was submitted
        if 'update_username' in request.POST:
            new_username = request.POST.get('username')
            if new_username:
                request.user.username = new_username
                request.user.save()
                messages.success(request, "Username updated successfully")
                return redirect('profile')
        
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Keep user logged in
                messages.success(request, "Password changed successfully")
                return redirect('profile')
            else:
                messages.error(request, "Please correct the error below.")
        else:
            password_form = PasswordChangeForm(request.user)
    else:
        password_form = PasswordChangeForm(request.user)
    
    return render(request, 'expenses/profile.html', {
        'password_form': password_form,
        'title': 'Profile Settings'
    })
