secret_code=5
guess_count=0
guess_limit=3
while guess_count < 1:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess == secret_code:
        print("You win!!")
    elif guess != secret_code:
        print("Two more chance")
while guess_count < 2:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess == secret_code:
        print('You win')
    elif guess != secret_code:
        print('Last chance')
while guess_count < 3:
    guess=int(input('Guess: '))
    guess_count+=1
    if guess == secret_code:
        print("You win!!")
        break
else:
    print("Wasted")
