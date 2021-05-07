import random

rps = random.randint(1, 3)

ask = input("Write your call (1. Rock, 2. Paper, 3. Scissors):- ")

if rps == '1' or ask == '1' :
    print("TIE !!!!")

elif rps == '1' or ask == '2':
    print(f"You won. Computer chose {rps}")

elif rps == '1' or ask == '3':
    print(f"You lose. Computer chose {rps}")

elif rps == '2' or ask == 1:
    print(f"You lose. Computer chose {rps}")

elif rps == '2' or ask == '2':
    print("TIE !!!!")

elif rps == '2' or ask == '3':
    print(f"You won. Computer chose {rps}")

elif rps == '3' or ask == '1':
    print(f"You lose. Computer chose {rps}")

elif rps == '3' or ask == '2':
    print(f"You lose. Computer chose {rps}")

elif rps == '3' or ask == '3':
    print("TIE !!!!")

else :
    print("Error !!!!")