# ✨ Restaurant Kitchen Service site ✨

The kitchen of every restaurant needs a responsible division of duties and subordination. 
This Django project is designed to facilitate internal managing processes and provide web interface where you can easily add, change or delete any data.
Each Cook of your restaurant has own profile with corresponding information and Dishes he/she is assigned to prepare. 
---

## 🌐 Visit my project deployed to Render: 🌐 
### [Restaurant Kitchen Service site](https://restaurant-kitchen-site.onrender.com)

Be aware that website is working very slowly only due to free server usage in deployment👆. (Page can load 10 seconds)
Thank you for understanding!

---
### 🗝 Welcome to log in and test the website, use the next test-user data for full access: 🗝
```python
username: Test-With-Love
password: Welcome-There_1
```

## 💾 Installation using GIT: 💾 

NOTE PLEASE: Python3 must be already installed. 

```python
git clone https://github.com/bohdan-yatsyna/kitchen-service-site.git
cd kitchen-service-site
python3 -m venv venv

venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)

pip install -r requirement.txt
python manage.py migrate
python manage.py runserver
```

Open preferable web-browser and enter the next link "http://127.0.0.1:8000/"

---
## 🚀  Features 🚀 
- Customizable Django admin pannel (for superusers)
- Reliable Django Authentication functions and Validations
- Intuitive managing system for Restaurant Kitchen with website interface
- Ability for easily access to your recipes and cooks profiles with opportunity of add, change or delete any data.
- Possibility to assign a responsible cook for preparing a dish or dishes.
- Made with love ;-)

---
## 💾 DB Structure: 💾 
![DB_STRUCTURE.png](static/assets/img/samples_for_readme/DB_STRUCTURE.png)

---
## ✨ PREVIEWS OF WEBPAGES ARE BELOW: ✨

### Home page:
![HOME PAGE.png](static/assets/img/samples_for_readme/HOME PAGE.png)

### Login page:
![LOGIN_PAGE](static/assets/img/samples_for_readme/LOGIN_PAGE.PNG)

### Detail views and List pages (Cook, Dish, DishType):
![_DISH_SAMPLE.PNG](static/assets/img/samples_for_readme/_DISH_SAMPLE.PNG)

![_COOK_SAMPLE.PNG](static/assets/img/samples_for_readme/_COOK_SAMPLE.PNG)

![_DISH_TYPES.PNG](static/assets/img/samples_for_readme/_DISH_TYPES.PNG)

![_COOKS.PNG](static/assets/img/samples_for_readme/_COOKS.PNG)

### Admin panel for superusers:
![_ADMIN_PANEL.PNG](static/assets/img/samples_for_readme/_ADMIN_PANEL.PNG)

### And more:
![_CREATE_DISH.PNG](static/assets/img/samples_for_readme/_CREATE_DISH.PNG)

![_UPDATE_PAGE.PNG](static/assets/img/samples_for_readme/_UPDATE_PAGE.PNG)

![_COOK_CONFIRM_DELETE.PNG](static/assets/img/samples_for_readme/_COOK_CONFIRM_DELETE.PNG)
