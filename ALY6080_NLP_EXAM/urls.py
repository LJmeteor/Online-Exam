"""ALY6080_NLP_EXAM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from telnetlib import LOGOUT
from django.contrib import admin
from django.urls import path
from exam import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentHub/', views.studentHub),
    path('test/', views.test),
    path("queryQuestions/",views.queryQuestions),
    path("submitAnswers/",views.submitAnswers),
    path("login/",views.login),
    path("loginForAdmin/",views.loginForAdmin),
    path('tensorflow/',views.tensorflow)
    # path("logout/",views.logout),
    # path("uploadExam/",views.uploadExam),
    # path("uploadTestPaper/",views.uploadTestPaper),
    # path("uploadTestAnswer/",views.uploadTestAnswer),
]
