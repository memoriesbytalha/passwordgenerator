import random

Alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Symbol = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '[', ']', '{', '}', '<', '>', '?', ',', '.', ':', ';', '/', '\\', '|', '`', '~', '+', '=', '-', '_', '^']
Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

password = ""

print("Welcome to Python Generator")
no_of_alpha = int(input("How many Alphabets you want to have in passwords\n"))
no_of_symbol = int(input("How many Symbol you want to have in passwords\n"))
no_of_number = int(input("How many Number you want to have in passwords\n"))

for char in range(1, no_of_alpha + 1):
    random_alpha = random.choice(Alpha)
    password = password + random_alpha

for char in range(1,no_of_symbol+1):
    random_sym=random.choice(Symbol)
    password += random_sym

for char in range(1,no_of_number+1):
    random_no=random.choice(Numbers)
    password += str(random_no)


password_list = list(password)
random.shuffle(password_list)

shuffled_password = ''.join(password_list)

print("Your random password is:", shuffled_password)
