# Program 1
# course={
#                "php": 2000,
#                "python":3000,
#                "Html": 1000,
#                "Angular": 4000,
#                "Company": "Pninfosys"            
# }
# print("Option Course", course.keys())
# a = input("Enter the course : ")
# # either This
# print("The course fees is:",course[a])
# # or that
# print("The course fees is:", course.get(a))
# Program 2
# num1=int(input("Enter the number 1: \n"))
# num2=int(input("Enter the number 2: \n"))
# num3=int(input("Enter the number 3: \n"))
# num4=int(input("Enter the number 4: \n"))
# num5=int(input("Enter the number 5: \n"))
# num6=int(input("Enter the number 6: \n"))
# num7=int(input("Enter the number 7: \n"))
# a={num1, num2, num3, num4, num5, num6,num7}
# print(a)
# Program 3
favlang= {}
# Input
a = input("Enter your favourite language Aditya: \n")
b = input("Enter your favourite language Rishav: \n")
c = input("Enter your favourite language Ankit: \n")
d = input("Enter your favourite language Robin: \n")
# Insert into dictionary
favlang["Aditya"]=a
favlang["Rishav"]=b
favlang["Ankit"]=c
favlang["Robin"]=d
print(favlang)

