# number=1
# while number<1000:
#     if number%10==3:
#         print("CLAP", number)
#     elif number%10==6:
#         print("CLAP", number)
#     elif number%10==9:
#         print("CLAP", number)
#     number=number+1
# number=0
# digit1=0
# digit2=0
# digit3=0
# while number<100:
#     digit1=number%10
#     digit2=(number%100-digit1)/10
#     if digit1%10==3:
#         print("Clap")
#     elif digit1%10==6:
#         print("Clap")
#     elif digit1%10==9:
#         print("Clap")
#     elif digit2%10==3:
#         print("Clap")
#     elif digit2%10==6:
#         print("Clap")
#     elif digit2%10==9:
#         print("Clap")
#     else:
#         print(number)
#     number=number+1

number=1
limit=2000

while number<limit:
    exponent=1
    count=0
    while number>10**(exponent-1):
        determinant=((number%(10**exponent))-(number%10**(exponent-1)))/(10**(exponent-1))
        if((determinant%3==0) and (determinant!=0)):
            count=count+1
        exponent=exponent+1

    if (count==0):
        print(number)
    else:
        countChak=0
        while countChak<count:
            print("Clap", end="")
            countChak=countChak+1
        print("")

    number=number+1
