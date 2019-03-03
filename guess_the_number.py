import random
oneMore = 'Yes'

while oneMore.lower() == 'Yes'.lower():

    num = random.randint(1, 100) 
    for i in range(10):
        guess = input('I\'m thinking in a number between 1 and 99, can you guess it? ') 
        if i == 9:
            print('I was thinking in ' + str(i) + '. You\'ve lost.')
            break
        elif int(guess) > num:
            print('I was thinking in a smaller number.')
        elif int(guess) < num:
            print(str('I was thinking in a bigger number'))
        else:
            print('Yep, I was thinking in {}, you\'ve guessed it in {} tries!'.format(num, i + 1))
            break
    print('Do you want to play again?')
    oneMore = input()

print('Thank you for playing with me.')
