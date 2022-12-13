#Password Generator Project
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
pw_letter = []
print(letters[random.randint(0,len(letters))])
for pw_counter in range(0,nr_letters):
  pw_letter.append(str(letters[random.randint(0,len(letters)-1)]))
for pw_counter in range(0,nr_numbers):
  pw_letter.append(str(numbers[random.randint(0,len(numbers)-1)]))
for pw_counter in range(0,nr_symbols):
  pw_letter.append(str(symbols[random.randint(0,len(symbols)-1)]))

pw_letter_str=""
for sign in pw_letter:
  pw_letter_str+=sign
print(pw_letter_str)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


pw_letter_str_random=""
i=0
for i in range(0,len(pw_letter)):
  length_pw_letter=len(pw_letter)-1
  position=random.randint(0,length_pw_letter)
  pw_letter_str_random += pw_letter[position]
  pw_letter.remove(pw_letter[position])
  i+=1
print(pw_letter_str_random)
