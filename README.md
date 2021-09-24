## Create a platform for Nutella lovers

The startup Pur Beurre, with which you have already worked, wishes to develop a web platform for its customers. This site will allow anyone to find a healthy substitute for a food considered "Too fatty, too sweet, too salty"

### Specifications
#### Features
- Display the search field on the home page
- The search must not be done in AJAX
- Responsive interface
- User authentication: account creation by entering an email and a password, without possibility to change the password for the moment.

### Technologies
* [Python](https://www.python.org/downloads/): Version 3.8
* [Django](https://docs.djangoproject.com/fr/3.2/): Version 3.2

### Installation
1. Clone the repository
```
git clone https://github.com/Ghazi92e/P8_OC_atie_ghazi.git
```
2. Create a virtual env
```
python -m venv env
```
3. Activate the virtual env
```
source env/bin/activate
```
4. Install packages from requirements.txt
```
pip install -r requirements.txt
```
5. Create a .env file in folder purbeurre_project(with file settings)
```
touch .env
```
6. Set up .env file
```
SECRET_KEY=''
DATABASE_NAME=''
DATABASE_USER=''
DATABASE_PASS=''
```
7. Add categories products from OpenFoodFacts API
```
python manage.py addcategories
```

8. Add products from OpenFoodFacts API
```
python manage.py addproducts
```

9. Run application
```
python manage.py runserver
```