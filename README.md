# EchoShare

EchoShare is a simple article-posting platform developed with django following MVT(Model-View-Template) architecture.

## Features

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

# Create superuser

python manage.py createsuperuser

# Start development server

python manage.py runserver
```

