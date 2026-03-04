import random
words=["CAT","BAT","DOG","SONG"]
word=random.choice(words)
total_chances=5
guessed_word="-"*len(word)
while total_chances !=0:
     print(guessed_word)
     letter=input("guess a letter:").upper()
     if letter in word:
          for index in range(len(word)):
              if word[index]==letter:
                  guessed_word=guessed_word[:index]+letter+guessed_word[index+1:]
               #print(guessed_word)
          if guessed_word==word:
               print("congratualtions you won!!!")
               break
     else:
          total_chances-=1
          print("incorrect guess")
          print("the remaining chances are:",total_chances)
else:
     print("game over")
     print("you lose")
     print("all the chances are exhausted")
     print("the correct word is",word)