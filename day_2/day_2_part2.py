
FILE_NAME = 'input.txt'

opp_key = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

player_key = {
    'X': 'L',
    'Y': 'D',
    'Z': 'W',
}

score_key = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

beats_key = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}

win_key = {
    'W': 6,
    'D': 3,
    'L': 0,
}


def calculate_winner(player_1, player_2):
    p1_pick = opp_key[player_1]
    p2_pick = player_2
    if beats_key[p1_pick] == p2_pick:
        return 'L'
    if beats_key[p2_pick] == p1_pick:
        return 'W'
    return 'D'


def calculate_score(result, pick):
    p1_pick = pick
    return win_key[result] + score_key[p1_pick]


def calculate_pick(pick, needed_result):
    opp_pick = opp_key[pick]
    needed_result = player_key[needed_result]
    if needed_result == 'D':
        return opp_pick
    if needed_result == 'L':
        return beats_key[opp_pick]
    if needed_result == 'W':
        return [k for k, v in beats_key.items() if v == opp_pick][0]


def play():
    score = 0
    with open(FILE_NAME) as file:
        for rec in file.readlines():
            rec = rec.strip()
            opp, needed_result = rec.split()
            print(opp, needed_result)
            player = calculate_pick(opp, needed_result)
            result = calculate_winner(opp, player)
            score += calculate_score(result, player)
            print(f"{opp} vs {player} = {result} {calculate_score(result, player)}")

    print(f"FINAL SCORE: {score}")

if __name__ == '__main__':
    play()
