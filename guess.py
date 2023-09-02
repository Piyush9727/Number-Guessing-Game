import random

def Number_guess_game():
    up=100
    low=0
    chances=7

    ac_num=random.randint(low,up)
    print("-------------------------------------")
    print("Welcome To The Number Guessing Game")
    print("-------------------------------------")
    print(f"Guess the number you have 7 chances")
    print("-------------------------------------")
    
    for attempt in range(1,8):
        try:
            gus_num=int(input(f"{attempt}'s chance out of 7 ="))
        except ValueError:
            print("please enter valid input")
            continue

        if gus_num==ac_num:
            print(f"your guess is correct!!! number is {ac_num}")
            print("-------------------------------------")
            break
        elif gus_num<ac_num:
            print("enter larger number")
        else:
            print("enter smaller number")

    if attempt==7:
        print(f"Sorry your all chances are over the acutal number is {ac_num}")

if __name__ == "__main__":
       while True:
           Number_guess_game()
           Replay=input("you want to play again?(Yes/No) =>").lower()
           print("-------------------------------------")
           if Replay !="yes":
               break
