
def find_duplied(obj1,obj2):
    for obj in obj1:
        if obj in obj2:
            return obj

def score(obj):
    if ord('a') <= ord(obj) <= ord('z'):
        return ord(obj) - ord('a') + 1
    if ord('A') <= ord(obj) <= ord('Z'):
        return ord(obj) - ord('A') + 27

if __name__ == '__main__':
    with open('../input.txt', 'r') as f:
        lines = f.readlines()

#     lines = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()
    sum = 0
    for line in lines:
        compartment_1 = line[:len(line)//2]
        compartment_2 = line[len(line)//2:]
        duplied = find_duplied(compartment_1,compartment_2)
        print(duplied,score(duplied))
        sum += score(duplied)
    print(sum)

    