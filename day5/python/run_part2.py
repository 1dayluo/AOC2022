from pprint import pprint
stack_1= ['B','Z','T']
stack_2 = ['V','H','T','D','N']
stack_3 = ['B','F','M','D']
stack_4 = ['T','J','G','W','V','Q','L']
stack_5 = ['W','D','G','P','V','F','Q','M']
stack_6 = ['V','Z','Q','G','H','F','S']
stack_7 = ['Z','S','N','R','L','T','C','W']
stack_8 = ['Z','H','W','D','J','N','R','M']
stack_9 = ['M','Q','L','F','D','S']
stack = [stack_1,stack_2,stack_3,stack_4,stack_5,stack_6,stack_7,stack_8,stack_9]



with open('../input.txt') as f:
    lines = f.readlines()


for line in lines:
    print(line)
    move_num = int(line.split(' ')[1])
    from_c = int(line.split(' ')[3])-1
    to_c = int(line.split(' ')[-1])-1
    temp = []
    for i in range(move_num):
        temp.append(stack[from_c].pop())
    # print()
    stack[to_c].extend(list(reversed(temp)))

# print(stack)
res = ''
for i in stack:
    res += i[-1]
print(res)

# 