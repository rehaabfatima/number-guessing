import random


num = random.randint(1,100)
is_running =True
guesses=0


while is_running:
      rand= int(input("Enter your guess:"))
      if rand.__int__():
           rand=int(rand)
           guesses += 1


           if rand < num :
            print("The number is too small!!.Please enter a larger number")

           elif rand > num:
            print("The number is too large!!!.Please enter a smaller number")

           elif rand < 0:
            print("Plese enter a positive")
           else:
             print("Correct guesss!!!!")
             print("The answer was",num) 
             is_running=False
      else:
         print("Invalid guess try another number")
   

