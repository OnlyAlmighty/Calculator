#Step 1
#add 
def add(x,y):
   return x + y
#subtraction 
def subtract(x,y):
  return x - y
#multiplication 
def multiply(x,y):
    return x * y
#divide 
def divide(x,y):
    return x / y
#Step 2
#choice 
print("Select operation")
print("A, Add")
print("B, Subtraction")
print("C, Multiplication")
print("D, Divide")
#Step 3
#choice_2
choice = input('Enter choice(A/B/C/D):')
if choice in ('A','B','C','D'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
#Step 4
if choice =='1':
    print(num1, "+",num2, "=",add(num1,num2))
elif choice =='2':
    print(num1,"-",num2, "=",subtract(num1,num2) )
elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
