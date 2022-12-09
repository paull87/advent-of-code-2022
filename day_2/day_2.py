
FILE_NAME = 'input.txt'

opp_key = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
}

player_key = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
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
    p2_pick = player_key[player_2]
    if beats_key[p1_pick] == p2_pick:
        return 'L'
    if beats_key[p2_pick] == p1_pick:
        return 'W'
    return 'D'


def calculate_score(result, pick):
    p1_pick = player_key[pick]
    return win_key[result] + score_key[p1_pick]


def play():
    score = 0
    with open(FILE_NAME) as file:
        for rec in file.readlines():
            rec = rec.strip()
            opp, player = rec.split()
            print(opp, player)
            result = calculate_winner(opp, player)
            score += calculate_score(result, player)
            print(f"{opp} vs {player} = {result} {calculate_score(result, player)}")

    print(f"FINAL SCORE: {score}")

if __name__ == '__main__':
    play()
