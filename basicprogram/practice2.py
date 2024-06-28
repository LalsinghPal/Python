print("Question1")
# Question1
num1= 5
num2 = 6
print(num1<num2)
print(num1<=num2)
print(num1>num2)
print(num1>=num2)
print(num1!=num2)
print("Question2")


#Question2
var1=7
var2=6
var3=3
print((var1+var2>var3) and (var1*var2)+var3>=(var3+var1))
print((var1*var2)>(var3*var1) and (var1*var2)<=(var1*var2*var3))
print((var1*var3)>(var1*var2*var3) or (var1*var3)<=(var2*var3))
print(not((var1*var3)>(var3*var1) and (var1*var3)<=(var2*var3)))

print("Ques3")
# Question3
num1=10
num2=5
num3=0
num4=2
num5=10
print((num1==num5) and ((num2-num4*num3) == (num2-num3)))
print((num2*num4*num3) <= ((num2-num4)*num3))
print(not(num3>=num4) and (num5/num2 == num4))
print(not(num5>num4) or (num4+num2)>num1)
print((num1 == num5) and (not(num5/num2 == num1/num2)))
print("Question4")
# Question4
list1 = ["e","d","u","c","a","t","i","o","n"]
print(list1[3:6])

print("Ques5")
# Question5
num_list = [100.5,30.456,-1.22,20.15]
num_list.insert(-1,-100.5)
num_list.pop(0)
num_list.sort()
print(num_list[0])
print("Ques6")
# Question6
tuple1=[5,10,15,20,25]
print(len(tuple1))
tuple1[2]=100
# print(tuple1[5])error
# tuple1=tuple1(8,6,"h")error
print("Ques7")
# Question7
pancard_list=["AAbGT6715H","UFFAC43521","IFSBD9163K","JOOEC1225H","RWXAFE187B"]
print(pancard_list[3][6], end="")
print(pancard_list[4][3:])

