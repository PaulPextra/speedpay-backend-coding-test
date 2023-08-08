# SPEEDPAY’S BACKEND CODING TEST

## Instructions:

write an API with the following:
1. Authentication for Admin and User
2. When a user creates an account, a 6 digit account number should be automatically generated.
3. A Deposit and Withdraw endpoint for a user to make deposit and withdraw
4. An endpoint to for a user to check his balance
5. A transfer endpoint to transfer to another user’s account

Kindly ensure that:
a. All endpoints are secured with a JWT token
b. A user cannot access another user’s account
c. Admin can retrieve all user’s information and account balances

## Submission

1. Write the steps to run your code locally in the README.md
2. Push your code to your GitHub account and send the link to **tunmbi@speedpay.ng** and **ebebejames@speedpay.ng**
3. Optionally, deploy your code to a free hosting and provide the URL.
4. Document the endpoints in the README.md file also.



## Technologies & Frameworks

- Python programming Language (latest version)
- Django & Django REST Framework (latest version)
- SQLite Database
- Simple JWT

## Installation

- Clone this project repository to your local machine.
- Open the project folder in your code editor
- Create and activate a *virtual environment* with the command: `pipenv shell`
- Install the requirements for this project from the *requirements.txt* file with the command: `pip install -r requirements.txt`
- Run the development server with the command: `python manage.py runserver`

**NOTE:** You must have **Python** installed on your local machine to run this program.

## API Test

### User Sign-up

- Endpoint: `http://localhost:8000/users/signup/`
- Request Method: `POST`
- Request Data: 
```
{
	"first_name": "John",
	"last_name": "Doe",
	"username": "user", *(Required!)
	"password": "****", *(Required!)
	"email": "johndoe@example.com",
	"gender": "Male",
	"phone": "",
	"address": "Lagos, Nigeria"
}
```

### Get Access Token

- Endpoint: `http://localhost:8000/api/token/`
- Request Method: `POST`
- Request Data: 
```
{
	"username": "user", *(Required!)
	"password": "****" *(Required!)
}
```
- Response Object:
```
{
	"refresh": "JWT Refresh Token",
	"access": "JWT Access Token"
}
```

### Refresh Token

- Endpoint: `http://localhost:8000/api/token/refresh/`
- Request Method: `POST`
- Request Data: 
```
{
	"refresh": "JWT Refresh Token"
}
```

### Create Account

- Endpoint: `http://localhost:8000/users/create-account/`
- Request Method: `POST`
- AUTH-TYPE: `Bearer`
- TOKEN: `JWT Access Token`
- Response Object:
```
{
	"account_number": "225631",
	"balance": "0.00"
}
```

### Deposite

- Endpoint: `http://localhost:8000/users/deposit/`
- Request Method: `POST`
- AUTH-TYPE: `Bearer`
- TOKEN: `JWT Access Token`
- Request Data: 
```
{
	"amount": 2000, *(Required!)
}
```

### Withdraw

- Endpoint: `http://localhost:8000/users/withdraw/`
- Request Method: `POST`
- AUTH-TYPE: `Bearer`
- TOKEN: `JWT Access Token`
- Request Data: 
```
{
	"amount": 2000, *(Required!)
}
```

### Check Balance

- Endpoint: `http://localhost:8000/users/check-balance/`
- Request Method: `GET`
- AUTH-TYPE: `Bearer`
- TOKEN: `JWT Access Token`

### Transfer

- Endpoint: `http://localhost:8000/users/transfer/`
- Request Method: `POST`
- AUTH-TYPE: `Bearer`
- TOKEN: `JWT Access Token`
- Request Data: 
```
{
	"to_account_number": "225632",
	"amount": 1000
}
```

### Transactions

- Endpoint: `http://localhost:8000/transactions/`
- Request Method: `GET`
- AUTH-TYPE: `Bearer`
- TOKEN: `JWT Access Token`

**NOTE:** Only a superuser or an admin can access this endpoint! To create a superuser account, run the command: `python manage.py createsuperuser` on your code editor terminal, and enter the required informations(i.e. username, email(optional), password).

### Retrieve All Active Users

- Endpoint: `http://localhost:8000/users/`
- Request Method: `GET`
- AUTH-TYPE: `Bearer`
- TOKEN: `JWT Access Token`

**NOTE:** Only a superuser or an admin can access this endpoint! To create a superuser account, run the command: `python manage.py createsuperuser` on your code editor terminal, and enter the required informations(i.e. username, email(optional), password).


### Swagger GUI Endpoints

- Endpoint: `http://localhost:8000/`
- Documentation: `http://localhost:8000/redoc/`



Author:[Paul Okoli](https://www.linkedin.com/in/paulokoli)