from ast import Try


a = {
     "name" : "pn Infosys Aditya",
     "college": "SOS JIWAJI",
     2 : [1,2,3,4,1,1,(2,4,5)], #list
     4 : ("Aditya", "rishav"), #key:value
     "education": {'Aditya' : 'MCA' },
     "city" : "Gwalior"
     }
# print(a["name"])
# GET is used to find key and print if present
# print(a.get("name"))
# keys(is used to print all the keys of dictionary)
# print(a.keys())
# Values() is used to print value of dictionary
# print(a.values())
# print(type(a.keys()))
# print(list(a.keys()))
# print(list(a.values()))
# list is used to print data in list form
updatedict ={
"branch" : "IT",
"phone" : 7354712807,
"salary": 45000,
"name": "ADITYA", 
}
a.update(updatedict)
print(a)
# try:
#                print(a["name123"])
# except Exception as error:
#                print(error)
# print(a["college"])
