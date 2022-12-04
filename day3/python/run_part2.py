from itertools import islice
def find_duplied(group):
    obj1 = group[0]
    obj2 = group[1]
    obj3 = group[2]
    for obj in obj1:
        if obj in obj2 and obj in obj3:
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
    groups = list(islice(iter(lines), 3))
    groups = [ lines[x:x+3] for x in range(0,len(lines),3)]
    for group in groups:

        duplied = find_duplied(group)
        print(duplied,score(duplied))
        sum += score(duplied)
    print(sum)

    