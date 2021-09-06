
# 1.Get two number first like shown below
first_num = int(input("Enter first num :"))
Second_num = int(input("Enter second num :"))

# 2.then add the number

def add(first_num,Second_num):
    return first_num + Second_num

def minus(first_num,Second_num):
    return first_num - Second_num

def multi(first_num,Second_num):
    return first_num * Second_num

def divide(first_num,Second_num):
    return first_num / Second_num


sum = add(first_num, Second_num)
minus = minus(first_num, Second_num)
multi = multi(first_num, Second_num)
div = divide(first_num, Second_num)

print(sum)
print(minus)
print(multi)
print(div)

# adding it to a text file
