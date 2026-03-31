# 💸 Pocket Finance

### *Feel the rhythm of your finances.*

![Django](https://img.shields.io/badge/Django-6.0-green?style=for-the-badge\&logo=django)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A modern, full-stack **expense tracking web application** built with Django — featuring a premium dark UI, interactive analytics, and powerful data management tools.

---

## ✨ Highlights

* 🔐 Secure authentication system
* 📊 Interactive analytics dashboard
* 💰 Full expense management (CRUD)
* 📥 CSV import & export
* 🎨 Premium dark-mode UI with glassmorphism
* 📱 Fully responsive design

---

## 📸 Preview

> *(Add screenshots here — this will instantly boost your repo quality)*

---

## 🧠 Features

### 🔐 Authentication & User Management

* Secure Registration, Login, Logout
* Profile settings (update username & password)

### 📊 Dashboard & Analytics

* Summary cards (total + monthly spending)
* Category-wise expense breakdown (Chart.js)
* 30-day spending trend graph
* Recent expenses quick view

### 💰 Expense Management

* Add, edit, delete expenses
* Custom categories (Food, Travel, etc.)
* Advanced filtering & search
* Pagination support

### 📥 Import & Export

* Bulk CSV import
* Automatic category creation
* Export filtered data to CSV

### 🎨 UI/UX

* Dark-mode admin panel aesthetic
* Glassmorphism cards
* Smooth animations & micro-interactions
* SaaS-style landing page

---

## 🛠️ Tech Stack

| Layer        | Technology                  |
| ------------ | --------------------------- |
| Backend      | Python, Django 6.0          |
| Database     | SQLite                      |
| Frontend     | HTML, CSS, Django Templates |
| Charts       | Chart.js                    |
| Fonts        | Google Fonts (Montserrat)   |
| Static Files | WhiteNoise                  |
| Deployment   | Gunicorn + Heroku           |

---

## 📁 Project Structure

```bash
expense-tracker/
│
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── expense_tracker/
│   ├── expenses/
│   ├── templates/
│   └── static/
```

---

## 🚀 Getting Started

### ⚙️ Prerequisites

* Python 3.10+
* pip
* (Optional) virtual environment

---

### 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/Athexdev/pocket-finance.git
cd pocket-finance

# Create virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver
```

---

## 🌐 Access

| URL           | Description  |
| ------------- | ------------ |
| `/`           | Landing page |
| `/register/`  | Register     |
| `/dashboard/` | Dashboard    |
| `/admin/`     | Admin panel  |

---

## 📄 CSV Import Format

```csv
Date,Title,Category,Amount,Description
28-03-2026,Coffee,Food,150,Morning latte
27-03-2026,Uber Ride,Travel,320,Office commute
```

---

## 📦 Dependencies

* Django
* Gunicorn
* WhiteNoise

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Made with ❤️ by **Debesh Nayak**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 🧠 Contribute

---

