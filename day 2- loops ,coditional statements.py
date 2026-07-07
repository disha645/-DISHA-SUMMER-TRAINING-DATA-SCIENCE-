for i in range(1,11):
     print("2 x", i, "=", 2*i)

     sum=0
for i in range(2,11,2):
     # if i%2==0:
          print(i)
         sum=sum + i
         print("sum of even numbers is", sum)

#grading system
for i in range(0,101):
    print("grade: A")
for i in range(60,81):
     print("grade: B")
for i in range(40,61):
     print("grade: C")
 i = int(input("enter your marks:"))
 for i in range(0,101):  
  if i>=80:
      print("grade: A") 
  elif i>=60:
     print("grade: B")
  elif i>=40:
     print("grade: C")
  else:
     print("grade: D")

#factorial
 fact=1
 for i in range(1,6):
    fact=fact*i
 print("factorial of 5 is:", fact)

#finding largest number
 n=int(input("enter numbers:"))
 for i in range(1,n):
     num=int(input("enter number:"))
 if num>largest:
         largest=num
         print("largest number is:", largest)

 n=(20,21,70,80,64,36)
 print("largest number is:", max(n))
 print("average is:", sum(n)/len(n))

#pattern forming
 for i in range(1,8):
     print("*" *i)

 for i in range(1,6):
     print(" " * (5-i) + "*" * (2*i-1))

 for i in range(1,7):
         print("*" *i)
 for i in range(5,0,-1):
 
