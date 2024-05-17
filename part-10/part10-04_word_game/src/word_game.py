import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if (len(player1_word) > len(player2_word)):
            return(1)
        elif (len(player1_word) < len(player2_word)):
            return(2)
        return(0)
    
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels1 = 0
        vowels2 = 0
        for char in player1_word:
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowels1 += 1
        for char in player2_word:
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowels2 += 1
    
        if (vowels1 > vowels2):
            return(1)
        elif (vowels1 < vowels2):
            return(2)
        return(0)
    
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        winner_dict = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
        if (player1_word not in ['rock', 'paper', 'scissors']) and (player2_word not in ['rock', 'paper', 'scissors']):
            return(0)
        elif (player1_word not in ['rock', 'paper', 'scissors']):
            return(2)
        elif (player2_word not in ['rock', 'paper', 'scissors']):
            return(1)
        else:
            for choice in winner_dict:
                if player1_word == choice and player2_word == winner_dict[choice]:
                    return(1)
                elif player2_word == choice and player1_word == winner_dict[choice]:
                    return(2)
            return(0)

if __name__ == "__main__":
    p = RockPaperScissors(6)
    p.play()