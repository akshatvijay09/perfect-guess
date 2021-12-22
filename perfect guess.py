import random
num = random.randint(1,100)
score = 0
plyr = None
print('Guess a number between 1 to 100 : ',end='')
while(plyr != num):
    plyr = int(input())
    score += 1

    if plyr == num:
        print('Hurray!!!! You guess it right....')
        print(f'Your score is {score} moves')

    elif plyr>num:
        if (plyr-num)>15:
            print("You guess it too high!!! try smaller number....")
        elif (plyr-num)<5:
            print("Just over it!!! try smaller number....")
        else:
            print("Very close!!! try smaller number....")

    elif plyr<num:
        if (num-plyr)>15:
            print("You guess it too low!!! try larger number....")
        elif (num-plyr)<5:
            print("Just over it!!! try larger number....")
        else:
            print("Very close!!! try larger number....")

with open('high score.txt') as f:
    hiscore = int(f.read())
    print(f'Current high score is {hiscore} moves')

if score<=hiscore:
    print('Congatulations!!!!\nYou set new record....')
    with open('high score.txt','w') as f:
        hiscore = f.write(str(score))
        print(f'New high score is {score} moves')