number = int(input())

x = '*'
result = str()
while x == number * '*':
    result = result + str(x)
    print(result)
    x += '*'