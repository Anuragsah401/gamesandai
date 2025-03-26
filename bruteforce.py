import random
import time

# Function for the player's guess mode
def player_guess(target):
    guess = None
    attempts = 0
    while guess != target:
        try:
            guess = int(input("Guess the number (1-100): "))
            attempts += 1
            if guess < target:
                print("Too low! Try again.")
            elif guess > target:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Congratulations! You guessed the number {target} in {attempts} attempts.")

# Function for the brute force mode
def brute_force_guess(target):
    guess = 1
    attempts = 0
    start_time = time.time()
    while guess != target:
        print(f"Brute force trying: {guess}")
        guess += 1
        attempts += 1
    end_time = time.time()
    print(f"Brute force found the number {target} in {attempts} attempts!")
    print(f"Time taken: {end_time - start_time:.2f} seconds.")

# Function to start the game
def start_game():
    while True:
        # Generate a random target number
        target_number = random.randint(1, 100)

        # Ask the player to choose the mode
        mode = input("Choose game mode: (1) Player Guess, (2) Brute Force: ")

        if mode == "1":
            player_guess(target_number)
        elif mode == "2":
            brute_force_guess(target_number)
        else:
            print("Invalid choice! Please enter 1 or 2.")
            continue

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    start_game()
