# Perfume World Bangladesh - E-Commerce Web Application

This is a premium, luxury perfume e-commerce web application inspired by the design and structure of [Perfume World Bangladesh](https://perfumeworld.com.bd/), built using Django, HTML, CSS, and JavaScript.

---

## Key Features
- **8 Distinct Pages**: Home, Shop/Listing, Product Details, Cart, Checkout, Mock SSLCommerz Payment Portal, Order Confirmation (Invoice), and Contact Us.
- **Full Authentication**: User Registration, Login, and Session-based login states.
- **Session-Based Cart**: Add, update, and remove products dynamically.
- **Mock SSLCommerz Gateway**: Simulates payment processing using bKash, Nagad, Rocket, and cards, updating order payment status on success.
- **Interactive UI Components**: Banner slider, brand logos scroll, community polls, reviews section, and newsletter subscription forms.
- **Self-Seeding Database**: Installs original product names, descriptions, pricing, and original website image links out-of-the-box.

---

## How to Run the Project in VS Code

Follow these simple steps to set up and run the application on your computer:

### Step 1: Open the Project in VS Code
1. Launch **Visual Studio Code (VS Code)**.
2. Go to **File** -> **Open Folder...**
3. Navigate to and select this project directory:
   `C:\Users\ASHIK\.gemini\antigravity\scratch\perfume_world`

### Step 2: Open the Terminal in VS Code
1. Open the built-in terminal by pressing **Ctrl + `** (backtick) or selecting **Terminal** -> **New Terminal** from the top menu bar.

### Step 3: Set Up a Virtual Environment (Recommended)
Creating a virtual environment ensures Python dependencies are isolated:
```powershell
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# (On Windows Powershell)
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies
Install Django inside your environment:
```powershell
pip install django
```

### Step 5: Setup the Database
Run migrations to generate the database schema and SQLite database file (`db.sqlite3`):
```powershell
# Create migrations for the store app
python manage.py makemigrations store

# Apply migrations to the database
python manage.py migrate
```

### Step 6: Seed Database with Original Products
We have created a database seeder script that populates categories, brands, and premium products with actual images from Perfume World:
```powershell
python seed_db.py
```

### Step 7: Create an Admin Account (Superuser)
Create an admin account to log in to the Django back-end admin dashboard and manage products/orders:
```powershell
python manage.py createsuperuser
```
*(Follow the prompts to enter a username, email, and password. Note: password characters won't be visible while typing).*

### Step 8: Start the Django Server
Launch the development server:
```powershell
python manage.py runserver
```

### Step 9: Access the Website
Once the server is running:
- Open your browser and navigate to: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
- Access the admin panel to view orders and manage products at: **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## File Structure Overview
- `perfume_shop/`: Main Django project configuration folder (settings, URLs, and WSGI/ASGI settings).
- `store/`: Main e-commerce application logic folder.
  - `models.py`: Database schema (Product, Category, Brand, Order, UserProfile).
  - `views.py`: Application views handling business logic.
  - `cart.py`: Helper class managing session-based carts.
  - `templates/`: HTML structures with embedded luxury styling.
  - `static/`: Extra static assets (custom CSS and JS placeholders).
- `seed_db.py`: Quick seeder script to populate database records.
- `db.sqlite3`: The SQLite database file (generated after migrations).
