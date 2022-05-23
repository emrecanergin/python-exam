import random
capitals = {
            'France':'Paris',
            'Finland':'Helsinki',
            'Germany':'Berlin',
            'Russia':'Moscow',
            'Hungary':'Budapest'
            }

trueAnswers = 0
falseAnswers = 0
c = random.choice(list(capitals.keys()))
print('wht is the capital of ' + c)
answer = input('Your answer?')
if answer == capitals.get(c):
    print('correct')
    trueAnswers +=1
else:
    print('incorrect')
    falseAnswers +=1
    
