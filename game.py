import random
top=count=0
while True:
    if top ==100:
        print("Game completed")
        break
    input("to roll a dice for that ,click in enter button")
    val=random.randint(1,6)
    print(val)
    if top +val <=100:
        top += val
    else :
        print(f"to reach top ,for that you need {100-top}")
    count +=1
    print(f"your at the position {top} and it types {count} rolls")




