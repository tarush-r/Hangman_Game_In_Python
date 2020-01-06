from os import system, name
from time import sleep

def clear(): 
   
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear') 



def screen(space, length, mistakes, count):
	clear()
	print("\n-------------THIS PROJECT IS MADE BY TARUSH RAJPUT-------------")

	print("\n*************************HANGMAN GAME*************************\n\n")
	for i in range(length):
		print(space[i], end=" ")
	print("")
	for i in range(length):
		print("-", end=" ")
	print("\n")
	print("wrong guesses: ", end="")
	for i in mistakes:
		print(i, end=" ")
	print("")
	if count==1:
		print("\n")
		print("-----------\n7 lives remaining")
	if count==2:
		print("\n\n")
		print("-----------")
		print("     |    ")
		print("     |    \n6 lives remaining")
	if count==3:
		print("\n\n");
		print("-----------")
		print("     |    ")
		print("     |    ")
		print("   -----")
		print("  | - - |")
		print("  |  -  |")
		print("   ----- \n5 lives remaining")
	if count==4:
		print("\n")
		print("-----------")
		print("     |    ")
		print("     |    ")
		print("   -----")
		print("  | - - |")
		print("  |  -  |")
		print("   ----- ")
		print("     |    ")
		print("     |     ")
		print("     |    ")
		print("     |    \n4 lives remaining")
	if count==5:
		print("\n")
		print("-----------")
		print("     |    ")
		print("     |    ")
		print("   -----")
		print("  | - - |")
		print("  |  -  |")
		print("   ----- ")
		print("     |    ")
		print("     |\\    ")
		print("     |    ")
		print("     |    \n3 lives remaining")
	if count==6:
		print("\n")
		print("-----------")
		print("     |    ")
		print("     |    ")
		print("   -----")
		print("  | - - |")
		print("  |  -  |")
		print("   ----- ")
		print("     |    ")
		print("    /|\\    ")
		print("     |    ")
		print("     |    \n2 lives remaining")
	if count==7:
		print("\n")
		print("-----------")
		print("     |    ")
		print("     |    ")
		print("   -----")
		print("  | - - |")
		print("  |  -  |")
		print("   ----- ")
		print("     |    ")
		print("    /|\\    ")
		print("     |    ")
		print("     |    ")
		print("      \\  \n1 life remaining")
	if count==8:
		print("\n")
		print("-----------")
		print("     |    ")
		print("     |    ")
		print("   -----")
		print("  | - - |")
		print("  |  -  |")
		print("   ----- ")
		print("     |    ")
		print("    /|\\    ")
		print("     |    ")
		print("     |    ")
		print("    / \\  ")
	print("")
def check():
	for i in range(length):
		if space[i]==word[i]:
			continue
		return -1
	return 1

count=0
count=int(count)
clear()
print("\n-------------THIS PROJECT IS MADE BY TARUSH RAJPUT-------------")
print("\n*************************HANGMAN GAME*************************\n")
print("\n#RULES#\n\n")
print("1: Player 1 will enter a word and Player 2 will guess the word\n\n2: Special characters like '*' '@' are NOT allowed\n")
print("3: Both the players can only enter lower case alphabets\n")
print("4: Player 2 can only enter one character at a time\n")
print("5: Player 2 will get 8 lives\n")
print("6: Player 1 can only enter meaningful words\n\n")
word=input("Player 1 enter a word: ")
length=len(word)
flag=0
flag=int(flag)
l=-1
l=int(l)
mistakes=[]
space=["*"]
for i in range(length-1):
	space.append("*")

while(1):
	screen(space, length, mistakes, count)
	guess=input("Enter your guess: ");
	for i in range(length):
		if guess==word[i]:
			space.pop(i)
			space.insert(i, word[i])
			#space[i]==word[i]
			flag=1
	if flag==0:
		
		mistakes.append(guess)
		count=count+1

	print(space)
	flag=0
	l=check()
	if l==1:
		screen(space, length, mistakes, count)
		print("Player 2 wins!!!")
		break
	if count==8:
		l=0
		break

if l==0:
	screen(space, length, mistakes, count)
	print("Player 1 wins!!!")
	print("The word was: ", word)



