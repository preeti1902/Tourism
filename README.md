
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

If there is no `requirements.txt` file yet, you can generate one by running:

```bash
pip freeze > requirements.txt
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
├── destinations/           # Main app containing views, models, etc.
├── tourism_website/        # Main Django project settings and configurations
├── manage.py               # Django's command-line utility
├── requirements.txt        # Python dependencies (if available)
└── templates/              # HTML templates for the front-end
```
