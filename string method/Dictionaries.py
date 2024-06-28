#Dictonaries are used to store data values in key:value pairs
# Duplicates are not allowed in doctionary
a = {
     "name" : "pn Infosys Aditya",
     "college": "SOS JIWAJI",
     2 : [1,2,3,4,1,1,(2,4,5)], #list
     4 : ("Aditya", "rishav"), #key:value
     "education": {'Aditya' : 'MCA' },
     "city" : "Gwalior"
     }
# print(a)
# print(a["name"])
# print(a[2])
# # print(a[0])
# print(a[2][6])
# print(type(a[4]))
# print(a["education"] ['Aditya'])
# print(a[2][6][1])
# print(a["education"]["Aditya"][1])
# print(type(a["education"]))


#dictionary items can be changed and new items can also be added.
a[4] = (45,50,55,60,47)
a["name"]= "Yoshita"
a["team"]= ["Yoshita","Aditya"]
print(a)
