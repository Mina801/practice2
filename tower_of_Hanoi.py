class Stack:
    def __init__(self,name , limit, size = 0):
        self.list=[]
        self.name = name
        self.size = size
        self.limit = limit
        self.last_item = list[-1]

    def peek(self):
        return self.last_item
    def push_list(self,disk):
        self.push_list.append(desk.value)

    def pull_list(self):
        disk_to_remove = self.list.pop()


class Node:
    def __init__(self,value,next_node=None):
        self.value = value

print("Let's Play Towers of Hanooi")
while True:
    num_of_disk = inpute(print("How many disks do you like to play with?"))
    if num_of_disk >= 3:
        break
    else:
        print("please enter a number greater than or equall to 3")
stacks=[]
left_stick = Stack("Left" , num_of_disk , num_of_disk)
stacks.append(left_stick.name)
right_stick = Stack("Right", num_of_disk )
stacks.append(right_stick.name)
middle_stick = Stack("Middle" , num_of_disk)
stacks.append(middle_stick.name)

letters=[]
for i in stacks:
    letters.append(i[0])

for i in range(num_of_disk:0 , -1):
    disk=Node(i)
    left_stick.list.append(disk.value)
def get_input():
    while True:
        for i in range(len(stacks)):
            print("please enter {0} for {1}.".format(letters[i] , stacks[i]))
        stack_to_change = input()
        return stack_to_change
        if stack_to_change in letters:
            break
        else:
            print("please enter a valid letter.")
#game:
num_moves = 0
while True:
    while True:
        print("which stack do you want to move from?")
        stack_to_remove = get_input()
        print("which stack do you want to move to?")
        stack_to_go = get_input()
        if stack_to_go.peek().value > stack_to_remove.peek().value:
            break
        else:
            pint("The value you wnat to add should be less than the value on the stick.")
        disk_to_change = stack_to_remove.list.pop()
        stack_to_go.list.append(disk_to_change)
        num_moves +=1
    if rihgt_stick.size ==right_stick.limit:
        print("Congradulation! you won in {0} moves".format(num_moves))
        break
