from distutils.command.upload import upload
import imp
from pickle import FALSE
from sre_constants import SUCCESS
from turtle import isvisible
from unittest import result
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pyrebase
import docx
import json
# initialize firebase
config = {
    'apiKey': "AIzaSyBiuYp3aVk7LmHV0wISACEBMKCvrWSYWeA",
    'authDomain': "aly6080-nlp.firebaseapp.com",
    'projectId': "aly6080-nlp",
    'storageBucket': "aly6080-nlp.appspot.com",
    'messagingSenderId': "723702609158",
    'appId': "1:723702609158:web:3b25a97d4c7ddc11219a87",
    'measurementId': "G-WFDSQG1FDC",
    'databaseURL': "https://aly6080-nlp-default-rtdb.firebaseio.com",
}
firebase = pyrebase.initialize_app(config)
database= firebase.database()
auth = firebase.auth()
user=None
# Create your views here.

# query all subjects
def studentHub(request):
     list=database.child('examList').get().val()
     isVisible="none"
     return render(request,"studentHub.html",{"list":list,"isVisible":isVisible})


# query all questions for a subject
def queryQuestions(request):
    examName=request.GET['examName']
    questions=database.child('question').child(examName).child("questions").get().val()
    # singleList=database.child('question').child(examName).child("questions").child('signle').get()
    mulList={}
    fibList=[]
    if(questions):
        singleList=questions['signle']
        mulList=questions['multiple']
        fibList=questions['fib']
    for item in singleList:
        print(item)
    return render(request,"index.html", {"single":singleList,"mulList":mulList,"fibList":fibList,"examName":examName})

## upload student answers to firebase
@csrf_exempt
def submitAnswers(request):
    if request.method == "POST":
            answerList = request.POST.get('answerList')
            examName=request.POST.get('examName')
            database.child("studentAnswers").child(examName).push(answerList) 
            result = {"status":"success!"}
    return JsonResponse(result)

## check whether need to login
@csrf_exempt
def login(request):
    ## if admin has login 
    id=request.GET.get("id")
    # info =auth.get_account_info(user['idToken'])
    # id=info['users'][0]['localId']
    if(id):
        list=database.child('examList').get().val()
        isVisible="block"
        return render(request,"studentHub.html",{"list":list,"isVisible":isVisible,"id":id})
    ## else forward to login page
    return render(request,"login.html")


## admin login
@csrf_exempt
def loginForAdmin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password=request.POST.get('password')
        result={}
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            info =auth.get_account_info(user['idToken'])
            id=info['users'][0]['localId']         
            result={"success":1,"id":id}
        except:
            result={"success":0,"id":""}
    return JsonResponse(result)







@csrf_exempt
def test(request):
    # user=auth.sign_in_anonymous()
    # info =auth.get_account_info(user['idToken'])
    # id=info['users'][0]['localId']
    # print(info['users'][0]['localId'])
    # data=['a','b',"","what","abc","ssssss"]
    # database.child("studentAnswers").child("JAVA").push(data)
    # if request.method == "POST":
    #         answerList = request.POST.get('answerList')
    #         examName=request.POST.get('examName')
    #         result = {"status":"success!"}
    if request.method == 'GET':
        return render(request,"test.html")
    elif request.method == 'POST':
         obj = request.FILES['testFile']
         with open("./exam/testpaper/%s" % obj.name, 'wb+') as  f:
                for chunk in obj.chunks():
                    f.write(chunk)
         f.close()
         data=uploadSingleQuestions1(obj.name)
         examName="JAVA"
         type="signle"
         database.child("question").child(examName).child("questions").child(type).set(data)
         return JsonResponse({"code":1})

    
def uploadSingleQuestions1(name):
 with open("./exam/testpaper/%s" % name, 'r') as  f:
    sum=0
    str0='{"question6": {"choices": {"A": "","B": "","C": "","D": ""},"description": ""},'
    f1=f.readlines()
    for f0 in f1:
       sum=sum+1
    for i in range(0,sum):
        str1=''
        if i%5==0:
            qnum=i//5+1
            str1+='"'+str(qnum)+'":{"description":"'+f1[i].strip()
            str1.replace('\n','')
            str1+='",'
        elif i%5==1:
            choiceList=f1[i].split(')',1)
            str1+='"choices":{"'+choiceList[0].upper().strip()+'":"'+choiceList[1].strip()+'",'
        elif i%5==2:
            choiceList=f1[i].split(')',1)
            str1+='"'+choiceList[0].upper().strip()+'":"'+choiceList[1].strip()+'",'
        elif i%5==3:
            choiceList=f1[i].split(')',1)
            str1+='"'+choiceList[0].upper().strip()+'":"'+choiceList[1].strip()+'",'

        elif i%5==4:
            choiceList=f1[i].split(')',1)
            str1+='"'+choiceList[0].upper().strip()+'":"'+choiceList[1].strip()+'"}},'
        str0+=str1
    str0=str0.strip(',')
    str0+='}'
    return json.loads(str0)



# def convertToJson(list):
    
#     for item in list:
def tensorflow(request):
    return render(request,"tensorflow.html")
        
