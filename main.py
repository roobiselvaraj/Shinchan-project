from shinchan import Shinchan

def welcome_message():
    choices = ["Play with Nani", "Watch Action Kamen", "Play with Shiro", "Dance", \
               "Eat Ramen", "Check Status", "Energy Drink", "Random Event"\
                , "Play video games", "Quit"]
    print("Welcome to Shinchan's World")
    print("These are the activities that you can do here!!")
    for i in range(len(choices)):
        print(f'{i+1}  - {choices[i]}')

    choice = input("Choose one options (Specify the number):")
    return choice
    
shinchan = Shinchan("shinchan")

def main():
    while True:
        choice = welcome_message()
        if choice == "1":
            shinchan.play_with_nani()
        elif choice == "2":
            shinchan.watch_action_kamen()
        elif choice == "3":
            shinchan.play_with_shiro()
        elif choice == "4":
            shinchan.dance()
        elif choice == "5":
            shinchan.eat_ramen()
        elif choice == "6":
            shinchan.check_status()
        elif choice == "7":
            shinchan.drink_energy_drink()
        elif choice == "8":
            shinchan.random_event()
        elif choice == "9":
            shinchan.play_video_games()  #Calling function
        elif choice == "10":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")
        loop = input("Do you want to try out any other activities? (yes/no)")
        if loop.strip().lower() != 'yes':
            break
        

if __name__ == "__main__":
    main()
