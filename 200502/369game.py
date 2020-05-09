# number=1
# while number<1000:
#     if number%10==3:
#         print("CLAP", number)
#     elif number%10==6:
#         print("CLAP", number)
#     elif number%10==9:
#         print("CLAP", number)
#     number=number+1
number=0
digit1=0
digit2=0
digit3=0
while number<100:
    digit1=number%10
    digit2=(number%100-digit1)/10
    if digit1%10==3:
        print("Clap")
    elif digit1%10==6:
        print("Clap")
    elif digit1%10==9:
        print("Clap")
    elif digit2%10==3:
        print("Clap")
    elif digit2%10==6:
        print("Clap")
    elif digit2%10==9:
        print("Clap")
    else:
        print(number)
    number=number+1
