number=15
divider=2
isntprime=False
while (divider<number) and (not isntprime):
    if number%divider==0:
        print(divider)
        print("로 나누어떨어지므로 소수가 아님")
        isntprime=true
    elif divider == number-1:
        print("소수로구나!")
    divider=divider+1
