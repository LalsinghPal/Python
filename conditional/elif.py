a = 14

if(a<3):
    print("The value of a is greater then 3")
elif(a<12):
      print("The value of a is greater then 12")
elif(a<11):
      print("The value of a is greater then 11")
elif(a<10):
      print("The value of a is greater then 10")
else:
       print("The value of a is greater then 3 or 7")


username ="admin"
password =123
#role ="students"
#table :role (admin),hr ,students

if(username=="raj" and password==123):
      print("student login")      
elif(username=="admin" and password==123):
      print("admin login")
elif(username=="hr" and password==123):
      print("hr login")
else:
      print("check username or password")