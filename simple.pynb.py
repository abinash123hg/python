
# while(True):
#  a =int(input("Enter ur number"))  
#  b =int(input("Enter ur another number"))  
#  if(a==b):
#     print("ur numbner r equal")
# else:
#       print("not equal")

# students = [
#     students_1:= input("enter ur first student name: "),
#     students_2:= input("enter ur first student name: "),
#     students_3:= input("enter ur first student name: ")
# ]

# marks =[
#     float(input("Enter ur 1st student marks: ")),
#     float(input("Enter ur 2nd student marks: ")),
#     float(input("Enter ur 3rd student marks: "))
# ]

# for i in range(3):
#     print("student name is:",students[i],"marks are: ",marks[i])
# str ="Abinash"
# print(str[2:5:2])
# while(True):
#     signal =input("Enter ur colour: ")
#     if(signal=="red"):
#         print("pls stop imidiate!!")
#     elif(signal=="green"):
#         print("pls ride ur vechile")
#     elif(signal=="yellow"):
#         print("pls start ur engine")
#     else:
#         print("pls check ur colour")
# while True:
#    a = int(input("Enter ur 1st number: "))
#    b = int(input("Enter ur 2nd number: "))
#    c = int(input("Enter ur 3rd number: "))
#    if(a>b):
#       print("A is bigeest among 3 number")
#    elif(b>c):
#       print("B is the greatest number among 3 numbner")
#    elif(c>a):
#       print("C is greatest number")
#    else: 
#       print("plrs cherck eagain")
#           user input the movies and that put in a list and print the wholle list
# movies = []
# mov1 = input("enter ur 1st movies: ")
# mov2 = input("enter ur 2nd movies: ")
# mov3= input("enter ur 3rd movies: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# list1 = [12,4,3,4,12]
# copy_list1 = list1.copy()
# list1.reverse()
# if(copy_list1==list1):
#     print("ur list is pallindrome")
# else:
#     print("not pallinrome")

# data = (1,4,9,16,25,36,68,5467,43)

# key = int(input("Enter your number: "))

# found = False
# for i in data:
#     if i == key:
#         found = True
#         break

# if found:
#     print("Found")
# else:
#     print("Not Found")
# n=int(input("Enter ur number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
#     print("fact of ",i,"is" ,fact)
# avg of 3 number 
# def avg_num(a,b,c):
#     d=(a+b+c)/3
#     return d

# print("Now ur execution willbe started")
# op=avg_num(34,45,56765)
# print(op)
#                                     len of a list print(list is our psrameter)
# def lenfth_list(list):
#     num=len(list)
#     return num
# print("Execution will be started")
# op=lenfth_list(list=[23,34,4,56,67,8,7])
# print(op)

#                       print elments of a list in  single lines(list is our parameter)
# def print_list(list):
#     for i in list:
#         print(i)
# print_list(list=[34,32,3,34,4,32,234,])

# factorial calculate
# def fact_num(n):
#     fact=1
#     for i in  range(1,n+1):
#         fact=fact*i
#     return fact
# op=fact_num(5)    

# def converet(inr):
#     usd=91.46
#     dheram=24.546
#     inr_usd=inr*usd
#     inr_dheram=inr*dheram
#     return inr_usd,inr_dheram

# inr=int(input("enter ur number"))
# op=converet(inr)
# print(op)
#                               oops
# classes and objects
# class animal:
#     name="monkey"
#     colour="slight yellow"
#     address="saudi"
# ob1=animal()
# print(ob1.name)
# print(ob1.colour)
# print(ob1.address)
#               constructor

# class student:
#     def __init__(self,marks,name,roll,adress):
#         self.marks=marks
#         self.name=name
#         self.roll=roll
#         self.adress=adress
# s1=student(23,"abinash",2003,"kendrapara")
# print(s1.name)
# print(s1.roll)
# print(s1.marks)
# print(s1.adress)


# class student:
#     def __init__(self,name,marks):
#           self.name=name
#           self.marks=marks

#     def avg(self,subj1,subj2,subj3):
#          c= (subj1+subj2+subj3)/3
#          return c
# s1=student("kulu",23)        
# print(s1.name)
# print(s1.marks)
# op=s1.avg(23,34,45)
# print(op)
# class account:
#     def __init__(self,acc_no,acc_pas):
#         self.acc_no=acc_no
#         self.acc_pas=acc_pas
      
#     def reset_pass(self):
#         print(self.acc_pas)  
# s1=account(122,"abc")
# print(s1.acc_no)        
# print(s1.reset_pass())        
    #                                           inheritance
# class car:
#     @staticmethod
#     def start():
#         print("start car noe")             
#     @staticmethod
#     def stop():
#         print("stop car now")    
# class toyotacar(car):
#     def __init__(self,name):
#         self.name=name
# car1=toyotacar("fortuner")
# car2=toyotacar("prious")
# car1.start()
# car2.stop()



# class animal:
#     def sound(self):
#         print("they r create sound,")
#     def bark(self):
#         print("bhoubhou")
# class dog(animal):
#     def eat(self):
#         print("eat both veg and nonveg")        

# d=dog()
# d.bark()
# d.eat()
# d.sound()     


# polymrphism
# class sum:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         return self.x+other.x    
# s1=sum(23)    
# s2=sum(24) 
# print(s1+s2)   

# class sub:
#     def __init__(self,x):
#         self.x=x
#     def __sub__(self,other):
#         return self.x-other.x
# s1=sub(50)    
# s2=sub(30)    
# print(s1-s2)

# mehod overriding(method body same but body different so when we print the body in child class only print not print the parent class if we access them simple use in child clss method super().methodname,)
# class anmal:
#     def sound(self):
#         print("animals makes sound")
# class dog(anmal):
#     def sound(self):
#         super().sound()->  simple use to print the parent class method
#         print("dogs are bark loudly")
# d1=dog()
# d1.sound() 
# 
            #    abstraction(means hide the unnesssarybthings to the user,parenct class method definr the child class body)
# from abc import ABC,abstractmethod
# class animal:
#     def sound(self):
#         pass
# class dog(animal):
#     def sound(self):
#         print("hlo i am dog class method ")
# d1=dog()
# d1.sound()            