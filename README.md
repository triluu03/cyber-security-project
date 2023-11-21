# Cyber Security 2023 - Project I

## Description

This Django project is an insecure web app that contains many security flaws according to [OWASP top ten list](https://owasp.org/www-project-top-ten/). The fix for each flaw is under the comment section that specifies the flaw the fix aims for.

The project is built as a simple book sharing platform where logged users can suggest and delete books, or view books suggested by other users. First-time user of the application has to create a new account (new user) and log in with those credentials to use the application.

## How to run the app

### Setup

-   `git clone` the repository
-   Navigate to the root of the repository
-   Run `python manage.py migrate`
-   Run `python manage.py makemigrations`

### Start the server

-   Run `python manage.py runserver`

## List of Security Flaws and Their Fixes

### FLAW 1: Injection

-   LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L117
-   **Description**: The function used to handle deleting books request is vulnerable to SQL Injection. This is because the function constructs a SQL query as a string object and execute it with direct established connection to the backend SQL server. Using a string as the SQL query is not secure since users can extend the parameter input (book_author) to execute an additional SQL query with a different purpose. For example, if the book_author is sent as the string: “Dang Hoang Giang' UNION DELETE FROM books_book WHERE author LIKE 'Other Author”, the SQL query will delete another book in addition to the targeted book with author: "Dang Hoang Giang".
-   **How to fix**: We will replace the old function with a new function to handle deleting books. In the new function, the method "delete()" of Django's class Model will be used instead of starting a direct connection to the database and executing a SQL query. Hence, even though malicious users attempt to exploit SQL Injection flaw, such as using the string mentioned above, the new function will return an error code of 404 since no such book can be found with the provided string as "author". Therefore, the application is saved from SQL injection.
-   FIX LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L133

### FLAW 2: Broken Authentication (or Identification and Authentication Failures)

-   LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L87
-   **Description**: A first-time user is required to create an account and log in with the newly created credentials to start using the application. However, when an user creates a new account, the application still allows weak and simple passwords, such as "12345" or "password", to be used. This makes the user's account with such a simple password easy to be guessed and compromised by malicious hackers.
-   **How to fix**: In the function that handles creating new users, we implement some new conditions on the passwords given by new users to prevent weak passwords creation. For example, such conditions are minimum length, uppercase and lowercase characters' existence, or digits existence. If the passwords provided by new users do not meet the above requirements, an error will be raised and the new user will not be created. This forces new users to create strong enough passwords for their account. Morever, we, as developers, can easily enforce new requirements for users' passwords by implementing more conditions as above.
-   FIX LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L87

### FLAW 3: Sensitive Data Exposure (or Cryptographic Failures)

-   LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L34
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L105
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/models.py#L12
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/templates/books/users.html#L19
-   **Description**: In addition to suggesting new books or deleting them, a logged-in user can view the information about other users. However, sensitive information, such as passwords, is available. The reason is that when a new account is created, information of the new user (username, password, and email) is stored in a separate model "UserInfo", so the password field of this model is not hashed the same way as the design of "User" model from Django. Providing such sensitive information about users' passwords is dangerous in terms of cyber security. Malicious attackers can utilize this flaw to compromise users' accounts in the application.
-   **How to fix**: First, remove the model "UserInfo" that stores the information of newly created accounts. Second, in the function that provides the view regarding information about other users, instead of returning objects from "UserInfo" model, we return the objects from "User" model of Django auth models. Finally. restricting the Django template to provide only username and email. Therefore, sensitive data like passwords is not exposed, avoiding the risks of users' accounts being compromised.
-   FIX LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L42
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L105
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/models.py#L12
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/templates/books/users.html#L19

### FLAW 4: Insecure Design

-   LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L117
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/templates/books/home.html#L23
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/urls.py#L9
-   **Description**: In the function that handles deleting books requests, the query uses "author" to find the targeted book and delete it. However, this design is insecure since different books with the same author will get deleted even though the user just aims to delete one of them.
-   **How to fix**: The database query should use "id" to find the targeted book to delete instead of "author" of the book. First, replace the view function that handles deleting books requests with the new one that uses "id" instead of "author" field. Second, replace the "url" that receives POST request to delete the book with the new one that receives "id" of the book instead of "author" of the book. Finally, modify the HTML template to send book's "id" in the request instead of book's "author".
-   FIX LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L134
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/templates/books/home.html#L29
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/urls.py#L10

### FLAW 5: Inefficient Logging and Monitoring (or Security Logging and Monitoring Failures)

-   **Description**: The application does not provide errors or warnings for the user. Moreover, there are no security logging messages about, for example, malicious activities. Therefore, it is very difficult for developers (or admins) to keep track of users' activities and notice any possible malicious attacks.
-   **How to fix**: Using a library "logging", we will send the messages as notifications, warnings, and errors to provide developers and admins mode details about users' and application's activities.
-   FIX LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L13
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L36
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L60
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L66
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L100
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L126

### FLAW 6: CSRF Attacks

-   **Description**: The application is vulnerable to attacks targeting users' browsers. More specifically, malicious attackers can utilize the users' cookies to send a request, so the server thinks that it is receiving requests from the users.
-   **How to fix**: Django framework provides a straightforward way to resolve this issue. Developers just need to add the decorator "csrf_protect" above the views that need protection against cross site request forgery.
-   FIX LINK:
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L19
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L29
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L50
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L75
    -   https://github.com/triluu03/cyber-security-project/blob/main/books/views.py#L112
