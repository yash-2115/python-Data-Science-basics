x = int(input("enter the number: "))
y = input("enter the number: ")

try:
    z = x/y

except ZeroDivisionError as e:
    print(str(x)+"/"+str(y)," is not possible")
    z = None

except TypeError as e:
    print("Type error exception")

print("Division is: ", z)