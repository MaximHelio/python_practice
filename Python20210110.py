array = [0]*10
num = int(input())
result = ""  #빈 str 저장

while num:
   array[num%10] += 1
   num //= 10
   print(array)
