#if a number is even or odd number
#num=int(input("Enter a number "))
#if num%2==0:
  #  print("even number")
#else:
  #  print("odd number")

#program that prints the largest of three numbers
v=int(input("Enter the first number "))
x=int(input("Enter the second number "))
z=int(input("Enter the third number "))

if v>x and v>z:
    print(f"{v} is the largest number")

elif x>z and x>v: 
    
    print(f"{x} is the largest")
elif z>v and z>x:
    print(f"{v} is the largest")
else:
    print("They are equal")

