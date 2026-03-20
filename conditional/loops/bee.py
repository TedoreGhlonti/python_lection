WORDS = {
    "PAIR": 4,
    "HEAR": 4,
    "CHEAR": 5,
    "GRAPHIC": 7,
}

def main():
    print("Welcome to Spelling Bee!")
    print("Your letters are: A I P C R H G")
    
    while len(WORDS) > 0:
        print(f"{len(WORDS)} left")
        guess = input("guess a word: ")
        if guess == "GRAPHIC":
            WORDS.clear()
            print("You won!")
        
        elif guess in WORDS.keys():
             points = WORDS.pop(guess)
             print(f"Good job! you scored {points} points")
    print("That's the game!")
main()