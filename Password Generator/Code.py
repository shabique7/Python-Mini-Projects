import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for easy version
password=""
for char in range(0,nr_letters):
    random_char=random.choice(letters)
    password+=random_char
for char in range(0,nr_letters):
    random_char=random.choice(symbols)
    password+=random_char
for char in range(0,nr_letters):
    random_char=random.choice(numbers)
    password+=random_char
print("Easy Password:\n"+password)

#for hard version
password_list=[]
for char in range(0,nr_letters):
    random_char=random.choice(letters)
    password_list.append(random_char)
for char in range(0,nr_letters):
    random_char=random.choice(symbols)
    password_list.append(random_char)
for char in range(0,nr_letters):
    random_char=random.choice(numbers)
    password_list.append(random_char)
random.shuffle(password_list)

password=""
for char in password_list:
    password+=char
print("Hard Password:\n"+password)
