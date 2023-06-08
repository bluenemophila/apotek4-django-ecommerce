# Apotek K4 Django Ecommerce

This is our final project for Django and Cybersecurity course from Digitalent Kominfo. By the end of the program, we worked on a ecommerce website task by groups on a Hackathon format.
Our project, Apotek K4, was a wordplay on our team name, K4, based on an already existing and popular drugstore.

## Installation
Do this following to run the server on your local
- Download the ZIP of this repository or clone using Git
- Create environment and install the requirements.txt
  ```py -m venv env_ecom
  env_ecom/Scripts/activate  
  pip install -r requirements.txt
- Migrate the manage.py and runserver
  ```py manage.py makemigrations
  py manage.py migrate
  py manage.py runserver
- Open the server link on your browser
- Done!

## Functionality
This website has some of this functionality:
- User login & signup
- Product listing and catalogues
- Cart and checkout mechanism
- User dashboard (profile, invoices and order history, change password mechanism)
- Filter by price, category, and brand using Ajax
- Wishlist, review
- Discount on sale items and coupon functionality
- Database system with PostgreSQL and Django admmin configuration using Jet

## Cybersecurity
For security measures, this website is also equipped with:
- SQL injection prevention
- XSS prevention
- CSRF prevention
- Login rate limiting
- Access control
- Parameter tempering prevention
- IDOR prevention

## Demo
Here are some of the demo for the website. (To be added)

For more info and future updates, kindly check my github [bluenemophila](https://github.com/bluenemophila).
