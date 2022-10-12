# NLP-Online Exam#

## development environment ##
- Django
- FireBase
- VSCode (verson 1.68.1)
## technologies ##
- HTML/CSS, JS
- Python ( verson 3.10.5)
- bootstrap

## Installation ##
Follow the steps below to get started with this project's development envionment.
1. install Django in VSCODE
 1.1 pip3 install django
 1.2 Close vscode, right-click in the folder where you want to create the project and open it with vscode, or use terminal input in vscode
  cd The absolute path to the project file
 1.3 Create a django project
 django-admin startproject projectName
 1.4Create an empty development database by running the following command:()  sqlite database is used to create session to maintain the status of Login
     python manage.py migrate
 1.5 Create a Django app
  python manage.py startapp appName

More details https://code.visualstudio.com/docs/python/tutorial-django

## Python package dependencies##
- pyrebase (firebase API for Python)  More details https://libraries.io/pypi/Pyrebase
- spacy (NLP)




<h2 id="outline">Basic project modules</h2>
- [StudentHub]
- [AdminHub]

## Description of each module ##

<h3 >StudentHub</h3>
-using HTML/CSS. This will comprise of the types of exams, questions students need to answer, and student answers.


<h3 id="class">AdminHub</h3>
-using HTML/CSS. This will comprise of admin login, exam details, questions, expected or correct answers (stored in firebase) and student answers. 

## Backend##
```
ALY6080_NLP_EXAM
├─ .vscode
│  ├─ launch.json
│  └─ settings.json
├─ ALY6080_NLP_EXAM
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ settings.cpython-310.pyc
│     ├─ urls.cpython-310.pyc
│     ├─ wsgi.cpython-310.pyc
│     └─ __init__.cpython-310.pyc
├─ db.sqlite3
├─ exam
│  ├─ admin.py
│  ├─ apps.py
│  ├─ dataUtils.py
│  ├─ fileUtils.py
│  ├─ migrations
│  │  ├─ __init__.py
│  │  └─ __pycache__
│  │     └─ __init__.cpython-310.pyc
│  ├─ models.py
│  ├─ Readme.md
│  ├─ static
│  │  ├─ css
│  │  │  ├─ card.css
│  │  │  ├─ login.css
│  │  │  ├─ nguyen-dang-hoang-nhu-Wp3sgCHoawg-unsplash.jpg
│  │  │  └─ style.css
│  │  ├─ image
│  │  │  ├─ 1.jpg
│  │  │  ├─ nguyen-dang-hoang-nhu-Wp3sgCHoawg-unsplash.jpg
│  │  │  └─ title.png
│  │  ├─ js
│  │  │  ├─ database
│  │  │  │  ├─ connect.js
│  │  │  │  └─ load.js
│  │  │  ├─ jquery-1.11.1-min.js
│  │  │  └─ main.js
│  │  ├─ plugins
│  │  │  └─ bootstrap_3.3.0
│  │  │     ├─ css
│  │  │     │  ├─ bootstrap-theme.min.css
│  │  │     │  └─ bootstrap.min.css
│  │  │     ├─ fonts
│  │  │     │  ├─ glyphicons-halflings-regular.eot
│  │  │     │  ├─ glyphicons-halflings-regular.svg
│  │  │     │  ├─ glyphicons-halflings-regular.ttf
│  │  │     │  └─ glyphicons-halflings-regular.woff
│  │  │     └─ js
│  │  │        ├─ bootstrap.min.js
│  │  │        └─ npm.js
│  │  └─ templateFile
│  │     ├─ template_answer.txt
│  │     ├─ template_fib.txt
│  │     └─ template_single.txt
│  ├─ templates
│  │  ├─ index.html
│  │  ├─ login.html
│  │  ├─ studentHub.html
│  │  ├─ test.html
│  │  └─ test1.html
│  ├─ test
│  │  └─ test.py
│  ├─ testpaper
│  │  ├─ CN_fib.txt
│  │  ├─ CN_single.txt
│  │  ├─ COMPILER DESIGN_answer.txt
│  │  ├─ COMPILER DESIGN_fib.txt
│  │  ├─ COMPILER DESIGN_single.txt
│  │  ├─ FLAT_fib.txt
│  │  ├─ JAVA.txt
│  │  ├─ JAVA_answer.txt
│  │  ├─ JAVA_fib.txt
│  │  ├─ OS_fib.txt
│  │  └─ OS_single.txt
│  ├─ tests.py
│  ├─ views.py
│  ├─ __init__.py
│  └─ __pycache__
│     ├─ admin.cpython-310.pyc
│     ├─ apps.cpython-310.pyc
│     ├─ models.cpython-310.pyc
│     ├─ views.cpython-310.pyc
│     └─ __init__.cpython-310.pyc
├─ manage.py
├─ out
│  ├─ exam
│  │  └─ readme.html
│  └─ README.html
└─ README.md

```