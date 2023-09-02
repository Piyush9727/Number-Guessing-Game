import random
def r_p_s_game():
    choices=["rock","paper","scissors"]

    c_c=random.choice(choices) #c_c for computer choice

    u_c=input("Enter your choice (rock,paper,scissors) => ").lower() #u_c for user choice


    if u_c in choices:
        print(f"Your choice = {u_c}",end="  || ")
        print(f"computer choice = {c_c}")

        print("--------------------------")
        if (u_c==choices[0] and c_c==choices[2]) or (u_c==choices[1] and c_c==choices[0]) or(u_c==choices[2] and c_c==choices[1]):
            print("You win!!!")
        elif u_c==c_c:
            print("It's Tie!!!")
        else:
            print("You Lose")
            
    else:
        print("please enter valid input (rock,paper,scissors)")

if __name__=="__main__":
    while True:
        r_p_s_game()
        Replay=input("you want to play again? (yes/no) = ").lower()
        if Replay != "yes":
            break
