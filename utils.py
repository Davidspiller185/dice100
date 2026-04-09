import random
def turn_decision(input_fn)->str:
    decision=input_fn
    while decision!="r" and decision!="p":
        decision=input("for roll press: `r`,for pass press:`p`")
    return  decision
def roll_two_d6() -> tuple[int, int]:
    roll_dic_1=random.randint(1,6)
    roll_dic_2=random.randint(1,6)
    return roll_dic_1,roll_dic_2
def is_bust(score: int) -> bool:
    if score>100:
        return True
    else:
        return False
def is_exact_100(score: int) -> bool:
    if score==100:
        return True
    else:
        return False
def closer_to_target(a: int, b: int, target: int = 100) -> int | None:
    if b<a<target:
        return 1
    if a<b<target:
        return 2
    else:
        return None






