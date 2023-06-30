from helper import *                 #importing functions from helper
array=[]                             #array declaration
num=int(input("Enter the number of elements you want to enter"))

for i in range(num):                 #loop to take value to enter in array
    x=int(input("Enter a number"))   #taking input from user
    array.append(x)                  #to enter numbers in array
sortarray(array,num)                 #function imported from helper
    