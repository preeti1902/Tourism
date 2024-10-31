
# **Tourism Website Project**

This project is a Django-based tourism website that provides various features related to travel destinations. The project includes the **'destinations'** app, and it allows users to explore and learn more about different tourist spots.

## **Prerequisites**

Before you begin, ensure you have the following software installed on your system:

- Python 3.x
- Django 4.x
- Git

You can check the installation by running the following commands:

```bash
python --version
django-admin --version
git --version
```

If any of these are not installed, follow the official documentation for installation instructions.

## **Getting Started**

### 1. **Clone the Repository**

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace `<repository-url>` with the actual URL of the repository, and `<repository-folder>` with the folder name where you'd like to store the project.

### 2. **Install Dependencies**

After cloning, you need to install the necessary dependencies. It’s a good idea to use a virtual environment for this.

```bash
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```


### 3. **Set Up the Database**

To set up the database, follow these commands:

```bash
# Create migrations based on the models
python manage.py makemigrations

# Apply the migrations to the database
python manage.py migrate
```

### 4. **Run the Development Server**

To start the Django development server:

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/` by default. Visit this URL in your browser to see the application running.

### 5. **Create a Superuser (Optional)**

If your application has a Django admin panel, you can create a superuser by running:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up a username, email, and password.

### 6. **Access the Admin Panel**

Once you've created a superuser, you can access the admin panel at:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials.

## **Project Structure**

Here's a brief overview of the project structure:

```text
.
├── accounts/                   # Handles authentication: login, registration, password reset
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── base/                        # Base folder for shared resources and utilities
│   ├── models.py                # Shared abstract models (e.g., timestamped model)
│   ├── utils.py                 # Helper functions
│   └── views.py                 # Shared base views (mixins, generic views)
├── bookings/                    # Handles booking logic
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── destinations/                # Handles destinations details
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── home/                        # Homepage and other general site views
│   ├── views.py
│   └── urls.py
├── packages/                    # Travel packages logic
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── reviews/                     # Handles review and rating functionality
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── public/                      # Static and media files
│   ├── static/                  # Static files (CSS, JS)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── media/                   # User-uploaded media files
├── templates/                   # Centralized HTML templates for the entire site
│   ├── base/                    # Shared base templates like base.html
│   ├── accounts/                # Templates for accounts app (login.html, signup.html, etc.)
│   ├── bookings/                # Templates for booking-related views
│   ├── destinations/            # Templates for destination-related views
│   ├── home/                    # Homepage templates
│   ├── packages/                # Templates for package-related views
│   └── reviews/                 # Templates for review-related views
├── tourism/                     # Main Django project configuration
│   ├── settings/                # Split settings files 
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py                    # Django's command-line utility
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```
