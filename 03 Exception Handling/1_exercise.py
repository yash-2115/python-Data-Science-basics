x = int(input("enter the number: "))
y = int(input("enter the number: "))

try:
    z = x/y

except ZeroDivisionError as e:
    print(str(x)+"/"+str(y)," is not possible")
    z = None

print("Division is: ", z)