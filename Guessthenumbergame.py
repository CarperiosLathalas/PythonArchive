import random

playAgain = "y"

def guessingGame():
   guessesTaken = 0
   print ("Hello, what is your name?")
   myName = input()
   print ("Well, hello, ",myName,". I am thinking of a random number bewteen one and one-hundred. Your job is to guess my number. Are you ready?")
   number = random.randint(1,101)
   while (guessesTaken < 10):
       print ("Take a guess.")
       guess = input()
       guess = int(guess)
       guessesTaken = guessesTaken + 1
       if guess < number:
           print ("Your guess is too low.")
       if guess > number:
           print ("Your guess is too high.")
       if guess == number:
           break
   if guess == number:
       guessesTaken = str(guessesTaken)
       print ("Good job, ",myName,". You guessed my number in ",guessesTaken," guesses. Impressive but you can do better. Play again?")
   if guess != number:
       number = str(number)
       print ("You've done messed up. The number I was thinking of was ",number,)
   playAgain == input("Play again (y/n)")
while playAgain == "y":
   guessingGame()

