from game import game_player,tie_breaker
from utils import roll_two_d6
def play_game():
    result_game=game_player()
    if result_game is not  None:
        return result_game
    else:
        game_result=tie_breaker(roll_two_d6())
        if game_result==1:
            print("the winner is player_1")
            return "game over and player_1 win because is score are bigger"
        elif game_result==2:
            print("the winner is player_2")
            return "game over and player_2 win because is score are bigger"
    return None
if __name__=="__main__":
    print(play_game())








