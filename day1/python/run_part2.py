def get_groups(lines):
    groups = []
    start = 0  
    for index in range(len(lines)):
        if lines[index] == '\n': 
            groups.append([ int(l.strip('\n')) for l in lines[start:index]])
            start = index + 1
    return groups



if __name__ == '__main__':
    with open('../input.txt','r') as f:
        lines = f.readlines()
    groups = get_groups(lines) 
    every_elf = [ sum(elf) for elf in groups]
    top_three = sum(sorted(every_elf,reverse=True)[:3])
    print(top_three)

    
