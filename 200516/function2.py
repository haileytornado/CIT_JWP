#555번째 홀수는?
#777번째
#999번째
num=int(input("숫자를 입력하세요"))
print(num)
def findOddNumber(bunzae, fav):
    count=1
    num=1
    print("지원이는"+fav+"좋아해요")
    while count!=bunzae:
        num+=2
        count+=1
    return num

print(findOddNumber(num-33), "딸기를"))
findOddNumber(3, "12를")
