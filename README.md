# E-commerce Store Project

A fully functional e-commerce store built with Python and Django.

## Features

- User Authentication (Registration, Login, Logout)
- Shopping Cart
- Order Management
- PayPal Payment Integration
- Shipping Address Management
- Product Categories and Listings
- Responsive Design with Bootstrap
- Admin Dashboard for Product and Order Management
- Email Notifications for Orders

## Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, Bootstrap, JavaScript
- **Database**: SQLite (can be switched to PostgreSQL or MySQL)
- **Payment Gateway**: PayPal
- **Deployment (Optional)**: AWS or Render (not implemented)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git

2. Navigate to the project directory:
   ```bash
   cd your-repo-name

3. Create a virtual environment:
   ```bash
   python -m venv venv

4. Activate the virtual environment:
   On macOS/Linux:
   ```bash
   source venv/bin/activate

   On Windows:
   ```bash
   venv\Scripts\activate

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
6. Apply migrations:
   ```bash
   python manage.py migrate

7. Run the server:
   ```bash
   python manage.py runserver


## Usage

1. Navigate to http://127.0.0.1:8000/ in your browser.
2. Register a new user or login to access the store.
3. Add products to your cart, manage shipping, and complete your orders.


## License

This project is licensed under the MIT License.
