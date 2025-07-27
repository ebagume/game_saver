import csv
import os.path


class GameState:
    def __init__(self, score, level, lives):
        self.score = score
        self.level = level
        self.lives = lives

    def add_to_score(self, amount):
        self.score += amount

    def next_level(self):
        self.level += 1
        self.add_to_score(100)  # Bonus points for completing a level

    def add_or_subtract_lives(self, amount):
        self.lives += amount
        if self.lives < 0:
            self.lives = 0
        return self.lives

def save_game(game_state, saved_data):
    with open(saved_data, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["score", "level", "lives"])
        writer.writerow([game_state.score,
                         game_state.level,
                         game_state.lives
                        ])

def load_game(Super_Broes):
    DEFAULT_SCORE = 0
    DEFAULT_LEVEL = 1
    DEFAULT_LIVES = 3

    try:
        if os.path.isfile(Super_Broes):
            with open(Super_Broes, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                row = next(reader)
                return GameState(score= int(row[0]),
                                 level= int(row[1]),
                                 lives= int(row[2])
                                 )
        else:
            return GameState(DEFAULT_SCORE, DEFAULT_LEVEL, DEFAULT_LIVES)

    except Exception as e:
        print(f"Error loading game: {e}")
        return GameState(DEFAULT_SCORE, DEFAULT_LEVEL, DEFAULT_LIVES)

# Main program
if __name__ == "__main__":
    game = GameState(0, 1, 3)

    # Simulate some gameplay
    game.add_to_score(150)  # Add some points
    game.next_level() # Go to next level
    game.add_to_score(-75)
    game.next_level() # Go to next level
    game.add_or_subtract_lives(-1)

    # Save the game
    save_game(game, "Super_Broes.txt")

    # Delete the game instance to simulate quitting
    del game

    # Now load the saved game
    game = load_game("Super_Broes.txt")
    print(f"score:{game.score} level:{game.level} lives:{game.lives}")


    
