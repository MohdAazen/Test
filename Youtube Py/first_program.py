# https://letsupgrade.notion.site/Notes-Python-Zero-to-Hero-in-5-Days-538a9230118f48d2ba9523187ea57c07
# print("Hello")
# a = 10
# print(type(a))

"""no initialization with num, no spaces, no special character"""

# a= input("Enter a number: ");
# print(a);

"""List""" # similar to array # create read update delete
# my_list = ['toothpaste','toothbrush','milk','cookies'] # create 
# print(my_list[3])
# print(len(my_list))

# print(my_list[-2])
# Access
# print(my_list[1:3])
# print(my_list[::1])
# print(my_list[::-2])
# Slice

# my_list.append('color')
# my_list.insert(1,'pen')
# my_list.remove('milk')
# print(my_list)

# po=my_list.pop(2)
# po=my_list.pop()

# print(my_list)
# my_list.reverse()
# print(my_list)
# print(len(my_list))
# results = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 6)]
# print(results)
# squares = [x **2 for x in range(1,11)]
# # print(squares)
# my_list2=[23,'Sayyed Mohd Aazen',99]

# pairs=[(x,y) for x in my_list for y in my_list2]
# print(pairs)

# print(my_list2)
# my_list2.append("sayyedaazen81@gmail.com")
# print(my_list2)

# list1 =[1,2,3,4,5]
# list2 =[15,24,33,42,51]
# print(list2+list1)

# del list1[3]
# print(list1)

# list2.sort()
# list2.reverse()
# print(list2)


# append


"""five point about PEP8"""

"""Dictionary""" # key value format
# my_aadhaar_data = {'name':'Sayyed Mohd Aazen', 
#                    'address':'xyz',
#                    "fathers_name":'my_dad',
#                    'mothers_name':'my_mom',
#                    }
# print(my_aadhaar_data)

'''Set''' # gives a unique value # unordered sequence
# my_set={1,'a','f',6,4,2,'f',6,'d'}
# print(my_set)

"""Tuple""" # immutable
# my_tup=('sayyed','mohd','aazen')
# print(my_tup)
# print(my_tup.count('s'))

# Tuple(), List [], Set {}, Dictionary{:} 
"""Assignment: Try Built in Function for Tuple, List, Set, Dictionary"""

# Operators => Weapons
"""Arithmetic """

# var1 = 45 
# var2 = 33
# print(var1+var2)
# print(var1-var2)
# print(var1*var2)
# print(var1/var2)
# print(var1%var2)

# """Comparison """
# result = 5==3
# print(result)

"""Logical """
# num = 20 
# condition = "hot"

# buy = (num == 21) and (condition == "hot")
# print(buy)

# buy = (num == 21) or (condition == "hot")
# print(buy)

# buy = not(num ==21)
# print(buy)

"""Conditionals"""
# a = 20 
# b= 50
# print(a<b)

# five_star = False
# if(five_star):
#     print("Give 5 star")
# else:
#     print("Give anything")

# five_star = True
# dm=False
# if(five_star):
#     print("Give 5 star")
# elif(dm):
#     print("Give Dairy Milk")
# else:
#     print("Give anything")

# res12 = 85.5
# respcm = 90.5
# resjee = 85
# if(res12 >= 80):
#     if(respcm >= 90):
#         if(resjee >=85):
#             print("You r selected")
#         else:
#             print("good try for jee")
#     else:
#         print("good try for pcm")
# else:
#     print("good try for 12")
   
# lst1 = list(range(1,21))
# print(lst1)  
"""Loops"""   
# for loop

# for x in lst1:
#     print(x)

# num=input("Enter num:")
# for i in range(1,11):
#     print(num,"*",i,"=",int(num)*i)

# while loop

# i=1
# while i<11:
#     print(i)
#     i+=1

# for i in range(1,201):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)

# file = open("aazen.txt","w")
# file.write("This is Sayyed Mohd Aazen")
# file.write("\nThis is Sayyed Mohd Aazen")
# file.close

# file=open("aazen.txt","r")
# file_data = file.read()
# file.close()
# print(file_data)
    
# file = open('aazen.txt',"a")
# file.write(" I am an Engineer")
# file.close()

# file = open('aazen.txt',"r")
# read = file.read()
# file.close()

# # print(read)

# import os 

# if os.path.exists('aazen.txt'):
#     os.remove("aazen.txt")
#     print("File Deleted")
# else: 
#     print("File does not exists")
      
"""Functions"""

# def checkEven(num):
#     if num%2 == 0:
#         print("It's Even")
#     else:
#         print("It's Odd")

# checkEven(22)

# def sum(a,b):
#     print(a+b)
# sum(10,11)

# def add(a,b,c,d,e,f):
#     sum = a+b+c+d+e+f
#     return sum
# print(add(1,2,3,4,5,6))

# def addNNumbers(*nums):
#     sum = 0 
#     for i in nums:
#         sum+=i
#     return sum
# print(addNNumbers(1,2,3,4,5,6,7,8,9,10))

# def printFormattedData(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# printFormattedData(name = "Sayyed",age = 20,email = 'sayyedaazen81@gmail.com')
    
# def printFormattedData(**kwargs):
#     print(kwargs)
#     for i in kwargs.keys():
#         print(i,': ',kwargs[i])

# printFormattedData(name = "Sayyed",age = 20,email = 'sayyedaazen81@gmail.com',address='Thane')

# """Fibonacci Series"""
# def fib(n):
#     num1 = 0
#     num2 = 1
#     for i in range(0,n):
#         print(num1)
#         num3 = num1+num2
#         num1 = num2
#         num2=num3
# fib(9)

import random
import xlrd3 as xlrd

# rn=random.randint(1,100)
# print(rn)

# lst =["Sayyed","Ibrahim", "Shuaib", "Mohd", "Adam","Aazen", "Musa", "Kalim", "Ali", "Isa"]
# name = random.choice(lst)
# print(name)

# book = xlrd.open_workbook("Python_read.xlsx")
# print("The number of worksheet is: {0}".format(book.nsheets))
# print("Worksheet names: {0}".format(book.sheet_names()))
# sh = book.sheet_by_index(0)
# print("{0} {1} {2}".format(sh.name,sh.nrows,sh.ncols))
# for  i in range(sh.nrows):
#     print(sh.row(i))

import pyowm

# API_KEY = '517526fa851bd6a21cc63d53ffc7c617'

# owm = pyowm.OWM(API_KEY)

# def get_weather(city_name):
#     try:
        
#         weather = (owm.weather_manager().weather_at_place(city_name)).weather
        
#         temperature = weather.temperature('celsius')['temp']
#         humidity = weather.humidity
#         wind_speed = weather.wind()['speed']
#         weather_status = weather.status

#         print(f"Weather in {city_name}:")
#         print(f"Temperature: {temperature}°C")
#         print(f"Humidity: {humidity}%")
#         print(f"Wind Speed: {wind_speed} m/s")
#         print(f"Status: {weather_status.capitalize()}")
#     except pyowm.exceptions.api_response_error.NotFoundError:
#         print("City not found or an error occurred.")


# city_name = input("Enter a city name: ")
# get_weather(city_name)

# class car:
#     def __init__(self,seats,fuel,color,speed):
#         self.seats = seats
#         self.fuel_type =  fuel
#         self.color = color
#         self.max_speed = speed
        
#     def printColor(self):
#         return self.color
    
#     def get_fuel_type(self):
#         return self.fuel
    
#     def get_seats(self):
#         return self.seats
    
# alto = car(5,"petrol","blue",120)
# seltos = car(5,"petrol","black",130)
# thar = car(4,'diesel','black',140)

# print(alto.color)
# print(thar.get_fuel_type)

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         pass

# class lion(Animal):
#     def speak(self):
#         print(self.name,"roar")
        
# class duck(Animal):
#     def speak(self):
#         print(self.name,"quack")


# duck1 = duck("ducky")
# duck1.speak()
# sheru = lion("shera")
# sheru.speak()


class shape:
    def area():
        pass

class triangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b
        
    def area(self):
        return 1/2* self.l *self.b
    
class square(shape):
    def __init__(self,side):
        self.side = side
        
    def area(self):
        return self.side**2

s1 =square(3)
print(s1.area())
t1 =triangle(3,4)
print(t1.area())
