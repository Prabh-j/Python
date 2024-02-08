import random

ans = input('Rock, Paper, Sicssors\n: ').capitalize()
com = ['Rock', 'Paper', 'Sicssors']
comc = random.choice(com)
print(comc)

if comc == ans:
    print('Its a Draw')
elif (ans == 'Rock' and comc == 'Sicssors') or ((ans == 'Paper' and comc == 'Rock') or ((ans == 'Sicssors' and comc == 'Paper'))):
    print('You Win')
elif (comc == 'Rock' and ans == 'Sicssors') or ((comc == 'Paper' and ans == 'Rock') or ((comc == 'Sicssors' and ans == 'Paper'))):
    print('You Loose')
else:
    print('Please enter a valid response.')



