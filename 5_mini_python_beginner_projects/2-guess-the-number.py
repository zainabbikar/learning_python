import random

# randrange DOES NOT INCLUDE UPPER NUMBER 101
# r = random.randrange(0, 101)
# print(r)

# randint INCLUDES 101
# random_number = random.randint(0,11)
# print(random_number)

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('Type number larger than 0.')
        quit()
else:
    print('Type a number')
    quit()
random_number = random.randint(0, top_of_range)

while True:
    user_guess = input('make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Type a number.')
        continue
    
    if user_guess == random_number:
        print('you go it!')
    else:
        print('you got it wrong!')