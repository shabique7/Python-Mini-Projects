print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill=0
if size=="s":
   bill +=15
elif size =="m":
    bill +=20
elif size=="l":
    bill += 25
else :
    print("You Typed Worng")

if pepperoni=="y":
    if size=="s":
        bill+=2
    elif size == "m":
        bill += 3
    elif size == "l":
        bill += 3
    else:
        print("You Typed Worng")
elif pepperoni=="n":
    bill+=0
else:
     print("You Typed Worng")

if extra_cheese=="y":
    bill+=1
elif extra_cheese=="n":
    bill+=0
else:
     print("You Typed Worng")

print(f"Your final Bill is :${bill}.")
