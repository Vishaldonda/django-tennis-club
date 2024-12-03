# Django Tennis Club

This is a web application for managing a tennis club's activities, members, and more, built using the Django framework.

## Features

- **Dynamic Website**: HTML, CSS, and JavaScript for frontend design.
- **Database Integration**: Uses `db.sqlite3` for database management.
- **Admin Interface**: Django's built-in admin panel for managing members and other data.
- **Responsive Design**: Works across various devices.

## Live Demo

You can view the deployed application here:  
**[Tennis Club](https://vishaldonda.pythonanywhere.com/)**

## Installation

To run this project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Vishaldonda/django-tennis-club.git
    cd django-tennis-club
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the development server**:
    ```bash
    python manage.py runserver
    ```

6. Visit the application at: `http://127.0.0.1:8000/`

## Deployment

This application has been deployed to **PythonAnywhere**. For similar deployment:

1. Set up a PythonAnywhere account.
2. Clone the GitHub repository to your PythonAnywhere file system.
3. Install dependencies in your virtual environment.
4. Set up a WSGI file to link PythonAnywhere to your project.
5. Configure static files and database.

## Static Files

Static files are collected into the `productionfiles` directory using:
```bash
python manage.py collectstatic
