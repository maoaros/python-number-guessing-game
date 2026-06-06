import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Capture user guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check proximity 
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
                
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
