x = int(input("enter a value: "))
if (x%2==0):
    print("even")
else:
    print("odd")
    




for i in range(-100, 0, 2):
    print(i)
for i in range(1, 6):
    for c in range(i):
        # (0, [1, 2, 3, 4, 5]
        print(i, end="")
    print()





count = 0
while count < 5:
    if count == 2:
        count += 1
        continue
    print(count)
    count += 1






i = 3
while i <= 7: # true
    # print(i,)
    j = 2
    while j <= i:
        print(i, end=" ")
        j = j + 1
    print()
    i +=1






y = int(input("Enter 1st Number: "))
x = int(input("Enter 2st Number: "))
res = y**x
print("res: ", res)
def sum(start, end):
    result = 0
    for i in range(start, end+1):
        print("i =", i)
        result += i
        print("res: ", result)






sum(10, 50)
def greet_user(name):
    """Greets the user and exits."""
    print(f"Hello, {name}!")
    # return
#     # No explicit value is returned
# Calling the function
greet_user("John")





import math
print(sum([2, 3]))
import random
# print(random.(90, 100))




def multiply_and_divide():
    numerator = 3 * 5 * 7
    denominator = 9 * 11 * 13 * 15
    return numerator / denominator

def subtract_and_divide():
    numerator = 7 - 9
    denominator = sum(range(10, 41, 5))
    return numerator / denominator

def calculate_equation():
    return multiply_and_divide() - subtract_and_divide()
# Call the function to calculate the equation
result = calculate_equation()
print("The result of the equation is:", result)





def rs(x):
    if x %2!=0 and x>0:
        print("positive odd: ", x)
    else:
        print("Null: ", x)
x = random.randint(-40, 40000)
rs(x)








def n_n():
    res = []
    for i in range(1, 8):
        power = i**i
        res.append(power)
    print("The result of the equation is:", sum(res))
n_n()