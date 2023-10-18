# Cyber Security 2023 - Project I
This repository is used for Introduction to Cyber Security course at the University of Helsinki.

## How to run the app
### Setup
- `git clone` the repository
- Navigate to the root of the repository
- Run `python manage.py migrate`
- Run `python manage.py makemigrations`
### Start the server
- Run `python manage.py runserver`

## Description
This Django project is an insecure web app that contains many security flaws according to [OWASP top ten list 2017](https://owasp.org/www-project-top-ten/). The fix for each flaw is under the comment section that specifies the flaw the fix aims for.

#### 1. A01-2017: Injection
The function used to delete books in this application is vulnerable to SQL Injection. The fix aims to use Django models' methods to delete instead of directly using SQL queries.

#### 2. A02-2017: Broken Authentication
Weak passwords are allowed when creating new user that make easy for malicious users to hack into others' account. This fix aims to set constraints when new users create their passwords.

#### 3. A03-2017: Sensitive Data Exposure
Any logged-in user can view the passwords' hashes of every user of the application. The fix aims to hide the data regarding passwords from the users.

#### 4. A07-2017: Cross Site Scipting
Django provides an easy way to avoid this flaw: using CSRF token and `csrf_protection` decorators.

#### 5. A10-2017: Inefficient Logging and Monitoring
The application does not log enough information about the errors that users encounter, which makes debugging more difficult. The fix aims to log more information about the errors encountered in the application.
