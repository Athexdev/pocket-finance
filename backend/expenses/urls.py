from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.expense_add, name='add_expense'),
    path('expenses/<int:pk>/edit/', views.expense_edit, name='expense_edit'),
    path('expenses/<int:pk>/delete/', views.expense_delete, name='expense_delete'),
    path('expenses/export/', views.expense_export, name='expense_export'),
    path('expenses/import/', views.import_csv, name='import_csv'),
    path('profile/', views.profile_view, name='profile'),
]
