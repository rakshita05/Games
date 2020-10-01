import time
name=input("Enter your Name to continue:")
print("Welcome "+name+"!Let's play Hangman.")
time.sleep(1)
print("Start Guessing...")
time.sleep(0.5)
word="Secrets"
Guesses=' '
turns=10
while turns>0:
    failed=0
    for char in word:
        if char in Guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You Won!") 
        break
    guess=input("Guess a character:")
    Guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong guess.You have "+str(turns)+"  guesses left")
    if turns==0:
        print("You Lose.")