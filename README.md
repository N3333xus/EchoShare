# EchoShare

EchoShare is a simple article-posting platform built with Django, following the MVT (Model-View-Template) architecture.

## Features

- CRUD operations for articles via Django Admin.
- Article editing with CKEditor5.
- Image upload support for article covers.

## Running the project

### prerequisites


```bash
# Clone repostory

git clone https://github.com/N3333xus/EchoShare.git
cd EchoShare

# Create and active Virtual env

python -m venv my_env
source my_env/bin/activate  # Linux/Mac
my_env\Scripts\activate     # Windows

# Install dependencies

pip install -r requirements.txt

# Set up DB

python manage.py makemigrations
python manage.py migrate

# Create a superuser

python manage.py createsuperuser

# Start the development server

python manage.py runserver
```
![image](https://github.com/user-attachments/assets/fb51412c-f1cd-40f8-b179-da5077de0182)



