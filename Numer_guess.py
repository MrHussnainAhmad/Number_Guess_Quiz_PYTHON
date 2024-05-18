import random

top_range = input("Please Type a Number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please Enter a Numer greater then 0 Next time! ")
        quit()
else:
    print("Please type a number next time! ")
    quit()

random_num = random.randint(0, top_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Please make a guess! ")

    if user_guess.isdigit():
       user_guess = int(user_guess)
    else:
       print("Please type a number next time! ")
       continue

    
    if user_guess == random_num:
        print("you Got It ")
        break
    else:
     print("Alas, Wrong!")

print("Your total Guesses are ",guesses)
