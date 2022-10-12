import json

def uploadFIBQuestions():
 with open("D:\VSProject\Python\Exam\JAVA_fib.txt", 'r') as  f:
    i=0
    str0='{"question6": "debug",'
    f1=f.readlines()

# {
#   "1": "1.Interface can have only _____________________ variables",
#   "2": "2.The implicit return type of a constructor is___________________"
# }
    for line in f1:
        i=i+1
        str1='"'+str(i)+'":"'+line.strip()+'",'
        # print(str1)
        str0+=str1
    str0=str0.strip(',')
    str0+='}'
    print(json.loads(str0))
# uploadFIBQuestions()
