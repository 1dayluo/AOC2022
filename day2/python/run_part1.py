def score(choice):
    score_shap = {
        'X':1,
        'Y':2,
        'Z':3
    }
    return score_shap.get(choice)

def compare(elf,player):
    win_shape = {
        'XY':'Y',
        'XZ':'X',
        'YZ':'Z'
    }
    all_possible = [ [key[0],key[1]] for key in win_shape.keys()]
    for i in all_possible:
        if elf in i and player in i:
            choiced_key = "".join(i)
            return win_shape[choiced_key]
def calc_winscore(elf,player_shape):
    related_shape = {
        'A':'X',
        'B':'Y',
        'C':'Z'
    }
    if related_shape[elf] == player_shape:
        added_score = 3
    else:
        result = compare(related_shape[elf],player_shape)
        if result == related_shape[elf]:
            added_score = 0
        else:
            added_score = 6
    return added_score

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        lines = f.readlines()
    sum_score = 0
    for line in lines:
        inputs = [i.rstrip('\n') for i in line.split(' ')]
        sum_score += calc_winscore(inputs[0],inputs[1]) + score(inputs[1])
    print(sum_score)