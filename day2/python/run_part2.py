def winscore(choice):
    score_shap = {
        'X':0,
        'Y':3,
        'Z':6
    }
    return score_shap.get(choice)

def shape_score(player):
    score = {
        'A':1,
        'B':2,
        'C':3
    }
    return score.get(player)

def get_player_shape(elf,reverse_dict):
    others = [ i for i in ['A','B','C'] if i!=elf]
    print('other',others)
    for i in others:
        for key,value in reverse_dict.items():
            if i in key and elf in key:
                if value != elf:
                    return i

def calc_score(elf,player_choice):
    win_dict = {
        'B': 'AB',
        'A': 'AC',
        'C': 'BC'
    }
    reverse_dict = {v:k for k,v in win_dict.items()}

    if player_choice == 'X':
        round_content = win_dict[elf].strip(elf)
    if player_choice == 'Y':
        round_content = elf
    if player_choice == 'Z':
        round_content = get_player_shape(elf,reverse_dict)

    return shape_score(round_content)
    

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        lines = f.readlines()
    sum_score = 0
    # lines = ['A Y','B X','C Z']

    for line in lines:
        inputs = [i.rstrip('\n') for i in line.split(' ')]
        sum_score += calc_score(inputs[0],inputs[1]) + winscore(inputs[1])  
    print(sum_score)