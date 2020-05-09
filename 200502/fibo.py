#더하는 숫자 1씩 키우기
# add=1
# number=1
# while(number<=1000):
#     print(number+add)
#     number=number+add
#     add=add+1

#더하는 숫자가 1의 제곱, 2의 제곱, 3의 제곱, 4의 제곱...
# hailey=1
# number=1
# while(number<=1000):
#     add=hailey**2
#     print(number+add)
#     number=number+add
#     hailey=hailey+1

#피보나치
# number1=1
# number2=1
# while(number1<10000):
#     hailey=number1
#     number1=number2
#     number2=hailey+number2
#     print(number1)
first=1
second=1
#limit=20
# while(limit>0):
#     temp=first
#     first=second
#     second=first+temp
#     print(first)
#     limit=limit-1
for jiwon in [7, 6, 5, 4, 3, 2, 1]:
    temp=first
    first=second
    second=first+temp
    print(first)
