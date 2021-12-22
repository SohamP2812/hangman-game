import random

def reveal(letter, original, arr):
    for i in range(len(word)):
        if(original[i] == letter):
            arr[i] = letter
    return arr

print(('-'*13) + ' Hangman ' + ('-' *13))

words = ["python", "difficult", "manipulate", "piano", "canada",  "television", "puppy", "basketball", "insulator", "government", "important"]

word = random.choice(words)
original = list(word)
l = list(word)
for i in range(len(l)):
    l[i] = '*'

chances = 8
won = False
while chances > 0:
    won = True

    if(chances == 1):
        print("You have " + str(chances) + " chance left")
    else:
        print("You have " + str(chances) + " chances left")

    print(''.join(l))
    letter = input('Guess -> ')
    tmp = list(l)
    l = reveal(letter, word, l)
    for i in range(len(l)):
        if(l[i] == '*'):
            won = False
    if won == True:
        break
    if(tmp == list(l)):
        chances -= 1

if won == True:
    print('You won!')
else:
    print('You lost')
    print('The word was ' + word)




