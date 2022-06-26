#Password Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#get length of letters, numbers, symbols lists
len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)

#randomly select numbers within each list based on user input
selection = ""

for i in range(1,nr_letters+1):
    rand_letter = random.randint(1,len(letters)-1)
    selection = selection + letters[rand_letter]

for i in range(1,nr_symbols+1):
    rand_symbol = random.randint(1,len(symbols)-1)
    selection = selection + symbols[rand_symbol]

for i in range(1,nr_numbers+1):
    rand_numbers = random.randint(1,len(numbers)-1)
    selection = selection + numbers[rand_numbers]
print(f"Your randomly generated password is {selection}")

#---------------------------------------------------------------------#
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#shuffle password

#convert string to list
original_password = selection
password_list = list(original_password)
random.shuffle(password_list)


#convert list back to string
password = ""
for char in password_list:
    password = password + char
print(f"Your improved randomly generated password is {password}")