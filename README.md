<![CDATA[# 💸 PocketPulse — Personal Expense Tracker

> **Feel the rhythm of your finances.**  
> A modern, full-stack expense tracking web application built with Django, featuring a premium dark-mode admin panel UI, interactive charts, bulk CSV import/export, and a stunning SaaS-style landing page.

---

## ✨ Features

### 🔐 Authentication & User Management
- Secure **Registration**, **Login**, and **Logout** via Django's built-in auth system
- **Profile Settings** — update username and change password without re-login

### 📊 Dashboard & Analytics
- **Summary Cards** — total expenses, current month spending at a glance
- **Category Breakdown** — interactive Chart.js bar chart for expense distribution
- **30-Day Spending Trend** — line chart tracking daily expenditure over the last month
- **Recent Expenses** — quick-view table of the 5 most recent entries

### 💰 Expense Management (CRUD)
- **Add / Edit / Delete** expenses with title, amount, date, category, and description
- **Category System** — organise expenses into custom categories (Food, Travel, Rent, etc.)
- **Advanced Filtering** — filter by date range, category, or search by title
- **Pagination** — smooth handling of large datasets (10 per page)

### 📥 Import & Export
- **Bulk CSV Import** — upload a CSV file (`Date, Title, Category, Amount, Description`) to batch-create expenses; categories are auto-created if they don't exist
- **CSV Export** — download filtered expenses as a `.csv` file

### 🎨 Premium UI/UX
- **Dark-mode admin panel** aesthetic with high-contrast glassmorphism cards
- **SaaS-style landing page** with gradient branding, feature highlights, and CTAs
- **Google Fonts** (Montserrat) typography
- **Smooth CSS animations** and micro-interactions throughout
- Fully **responsive** design

---

## 🛠️ Tech Stack

| Layer         | Technology                          |
|---------------|-------------------------------------|
| **Backend**   | Python 3, Django 6.0                |
| **Database**  | SQLite (default)                    |
| **Frontend**  | Django Templates, HTML5, CSS3       |
| **Charts**    | Chart.js                            |
| **Fonts**     | Google Fonts (Montserrat)           |
| **Static**    | WhiteNoise                          |
| **Deployment**| Gunicorn + Procfile (Heroku-ready)  |

---

## 📁 Project Structure

```
expense-tracker/
├── .gitignore
├── README.md
└── backend/
    ├── manage.py
    ├── requirements.txt
    ├── Procfile
    ├── db.sqlite3
    ├── expense_tracker/        # Django project config
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    ├── expenses/               # Main app
    │   ├── models.py           # Category & Expense models
    │   ├── views.py            # All view logic (dashboard, CRUD, import/export, profile)
    │   ├── forms.py            # ExpenseForm (ModelForm)
    │   ├── urls.py             # App URL routing
    │   └── admin.py            # Admin site registration
    ├── templates/
    │   ├── base.html           # Base layout (navbar, sidebar, footer)
    │   ├── landing/
    │   │   └── landing.html    # Public SaaS-style landing page
    │   ├── expenses/
    │   │   ├── dashboard.html
    │   │   ├── expense_list.html
    │   │   ├── expense_form.html
    │   │   ├── expense_confirm_delete.html
    │   │   ├── import_csv.html
    │   │   └── profile.html
    │   └── registration/
    │       ├── login.html
    │       └── register.html
    └── static/
        └── css/
            └── style.css       # Global styles (dark theme, glassmorphism, animations)
```

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.10+**
- **pip** (Python package manager)
- (Optional) A virtual environment tool — `venv`, `virtualenv`, or `conda`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Athexdev/pocket-finance.git
cd pocket-finance

# 2. Create & activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
cd backend
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. (Optional) Create a superuser for the admin panel
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

### Access the App

| URL                              | Description                 |
|----------------------------------|-----------------------------|
| `http://127.0.0.1:8000/`        | Landing page                |
| `http://127.0.0.1:8000/register/`| Create a new account       |
| `http://127.0.0.1:8000/dashboard/`| Dashboard (login required)|
| `http://127.0.0.1:8000/admin/`  | Django admin panel          |

---

## 📄 CSV Import Format

To bulk-import expenses, prepare a `.csv` file with the following columns:

```
Date,Title,Category,Amount,Description
28-03-2026,Coffee,Food,150,Morning latte
27-03-2026,Uber Ride,Travel,320,Office commute
```

- **Date** format: `DD-MM-YYYY`
- **Category** is auto-created if it doesn't already exist
- **Amount** may include `₹` symbol or commas — they are stripped automatically
- **Description** is optional

---

## 🗺️ URL Routes

| Route                        | View              | Auth Required |
|------------------------------|-------------------|:------------:|
| `/`                          | Landing Page      | ❌           |
| `/register/`                 | Registration      | ❌           |
| `/accounts/login/`           | Login             | ❌           |
| `/dashboard/`                | Dashboard         | ✅           |
| `/expenses/`                 | Expense List      | ✅           |
| `/expenses/add/`             | Add Expense       | ✅           |
| `/expenses/<id>/edit/`       | Edit Expense      | ✅           |
| `/expenses/<id>/delete/`     | Delete Expense    | ✅           |
| `/expenses/export/`          | Export CSV         | ✅           |
| `/expenses/import/`          | Import CSV         | ✅           |
| `/profile/`                  | Profile Settings  | ✅           |

---

## 🧩 Dependencies

```
Django==6.0.2
whitenoise==6.12.0
sqlparse==0.5.5
tzdata==2025.3
asgiref==3.11.1
gunicorn==23.0.0
```

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ by <strong>Nayak</strong>
</p>
]]>
