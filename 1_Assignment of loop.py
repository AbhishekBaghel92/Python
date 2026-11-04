#while loop Assignment

   #1. Write a C program to print all natural numbers from 1 to n using while loop. 
# i=1
# while(i<=10):
#   print(i)
#   i=i+1
  
   #2. Write a C program to print all natural numbers in reverse (from n to 1) using while loop.
# i=10
# while(i>=1):
#     print(i)
#     i=i-1

  #3. Write a C program to print all alphabets from a to z using while loop.
# i="a"
# while(i<="z"):
#     print(i,end=" ")
#     i=chr(ord(i)+1)

   #4. Write a C program to print all even numbers between 1 to 100 using while loop.
# i=1
# while(i<=100):
#     if(i%2==0):
#         print(i)
#     i=i+1

   #5. Write a C program to print all odd numbers between 1 to 100.
# i=1
# while(i<=100):
#         print(i)
#         i=i+2

    # 8. Write a C program to print table of any number.
# n=int(input("enter the number: "))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

     #9. Write a C program to enter any number and calculate sum of all natural numbers between 1 to n.
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of natural numbers from 1 to", n, "is:", sum)


