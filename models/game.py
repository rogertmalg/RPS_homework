class Game():
    def __init__(self):
        self.winner_check = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"           
        }

    def play_game(self, player_1, player_2):
    
        winner = None

        if self.winner_check[player_1.hand.lower()] == player_2.hand.lower():
            winner = player_1

        elif self.winner_check[player_2.hand.lower()] == player_1.hand.lower():
            winner = player_2

        return winner

    # did check homework file for this part, logic behind this is that if 
    # player_1 chose rock, the winner_check will check the value of the 
    # rock key in the dictionary, and if that is equals to player_2 hand
    # it means player_1 wins, and vice-versa. 