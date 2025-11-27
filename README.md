# I_Scream Store

A Django web application for I-Scream Store — an ice cream shop's digital presence. This project demonstrates modern web development practices with Django, featuring a public-facing storefront with company information and contact capabilities, alongside a protected blog platform for authenticated users. Built with two distinct Django apps `store` and `blogs`, it showcases user authentication, form handling, and responsive design with Bootstrap.

## Features

- Built with Django
- Two apps:
  - `store`
  - `blogs`
- User authentication system (signup, signin, signout)
- Contact form for user messages
- Responsive design with Bootstrap

## Screenshots

### Home
![Home](assets/img_1.png)

### Signin Page
![Signin Page](assets/img_2.png)

### Blogs Page
![Blogs Page](assets/img_3.png)

## Project Structure

- `i_scream_store/` — Django project settings and URLs.
- `store/` — store app: views, templates, static files.
  - Home page
  - About Us page
  - Careers page
  - Contact Us page
- `blogs/` — blog app: views, templates, static files.
  - Authentication-protected blog posts
  - User signup and signin functionality
- `db.sqlite3` — Database
- `requirements.txt` — Python Dependencies

## Tech Stack

- **Language:** Python (3.8+ recommended)
- **Framework:** Django (see `requirements.txt` for the pinned version)
- **Database:** SQLite
- **Templates / Static:** Django templates and app-level static files
- **Bootstrap:** For prebuilt CSS and JS
- **Authentication:** Django's built-in authentication system

## Installation & Usage

- Windows (PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- macOS / Linux / WSL

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 0.0.0.0:8000
```
Visit http://127.0.0.1:8000/ to view the store and http://127.0.0.1:8000/blogs/ for the blog section (requires login).

##

<div align="center">I-Scream Store. Enjoy! 🍦</div>
