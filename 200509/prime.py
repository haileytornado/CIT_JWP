number=3
print("2")
while number<=100000:
    divider=2
    isprime=True
    while (divider<number) and (isprime):
        if number%divider==0:
            isprime=False
        elif divider == number-1:
            print(number)
        divider=divider+1
    number=number+1
