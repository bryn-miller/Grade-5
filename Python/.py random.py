import random
number = random.randint(1, 100)
while True:
    print('Guess a number 1 to 100')
    guess = input()
    i = int(guess)
    if i == num:
            print ('You guessed the number!')
            break
    elif i < num:
            print('Try higher')
    elif i > num:
            print('Try lower')
               
