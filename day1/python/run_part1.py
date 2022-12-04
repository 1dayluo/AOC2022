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
    max_elf_calo = 0
    for elf in groups:
        elf_total = sum(elf)
        if elf_total >= max_elf_calo:
            max_elf_calo = elf_total
    print(max_elf_calo)

    
