from utils import turn_decision,roll_two_d6,is_bust,is_exact_100,closer_to_target
score_player_1= 82
score_player_2 = 79
def game_player():
    global score_player_1
    global score_player_2
    print("the turn is for the player_1")
    print(f"your score is:{score_player_1} ,the score of player_2 is:{score_player_2}")
    choice_1 = input("for roll press: `r`,for pass press:`p`")
    game_choice_1 = turn_decision(choice_1)
    if game_choice_1 == "r":
        result_1=roll_two_d6()
        score_player_1+=result_1[0]+result_1[1]
        print(f"the result is:{result_1[0],result_1[1]},and the score of player_1 is:{score_player_1}")
        if is_bust(score_player_1) :
            print("player_1 are disqualified and player_2 win the game")
            return " game is over and player_2 win the game because player_1 is bust"
        elif is_exact_100(score_player_1):
            print("player_1 win the game")
            return "game is over and player_1 win the game because player_1 is exact 100"
    print("the turn is for the player_2")
    print(f"your score is:{score_player_2},the score of player_1 is:{score_player_1}")
    choice_2=input("for roll press: `r`,for pass press:`p`")
    game_choice_2=turn_decision(choice_2)
    if game_choice_2=="r":
        result_2=roll_two_d6()
        score_player_2+=result_2[0]+result_2[1]
        print(f"the result is:{result_2[0],result_2[1]},and the score of player_2 is:{score_player_2}")
        if is_bust(score_player_2):
            print("player_2 are disqualified and player_1 win the game")
            return " game is over and player_1 win the game because player_2 is bust"
        elif is_exact_100(score_player_2):
            print("player_2 win the game")
            return " game is over and player_2 win the game because player_2 is exact 100"
        return game_player()
    if game_choice_2=="p" and game_choice_1=="r":
        return game_player()
    if game_choice_2=="p" and game_choice_1=="p":
        print("the game is over")
        winner=closer_to_target(score_player_1,score_player_2)
        if winner ==1:
            print("the winner is player_1")
            return "game is over and player_1 win the game because the score of player_1 is closer to target"
        elif winner==2:
            print("the winner is player_2")
            return "game is over and player_2 win the game because the score of player_2 closer to target"
    return None
def tie_breaker(roller) -> int:
    global score_player_1
    global  score_player_2
    final_result=0
    print("the turn is for player_1")
    score_player_1+=roller[0]+roller[1]
    print(f"the result for player_1 is:{roller[0],roller[1]},and the score of player_1 is:{score_player_1}")
    print("the turn is for player_2")
    roll=roll_two_d6()
    score_player_2+=roll[0]+roll[1]
    print(f"the result of player_2 is:{roll[0],roll[1]},and the score of player_2 is:{score_player_2}")
    if score_player_1>score_player_2:
        print("the winner is player_1")
        return 1
    elif score_player_2>score_player_1:
        print("the winner is player_2")
        return 2
    while score_player_1==score_player_2:
        final_result=tie_breaker(roll_two_d6())
    return final_result

























