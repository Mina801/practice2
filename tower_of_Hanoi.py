class Stack:
    def __init__(self,name , limit,size = 0 ):
        self.list=[]
        self.name = name
        self.size = size
        self.limit = limit

    def peek(self):
        if self.size == 0:
            return 0
        else:
            return self.list[-1]

    def push_list(self,disk):
        self.push_list.append(disk)

    def pull_list(self):
        disk_to_remove = self.list.pop()



print("Let's Play Towers of Hanooi")
while True:
    num_of_disk =int( input(print("How many disks do you like to play with?")))

    if num_of_disk >= 3:
        break
    else:
        print("""
        please enter a number greater than or equall to 3
        """)
stacks=[]
left_stick = Stack("Left" , num_of_disk , num_of_disk)
stacks.append(left_stick)
middle_stick = Stack("Middle" , num_of_disk)
stacks.append(middle_stick)
right_stick = Stack("Right", num_of_disk )
stacks.append(right_stick)

letters=[]
for i in stacks:
    letters.append(i.name[0])

for i in range(num_of_disk ,0 , -1):
    left_stick.list.append(i)

def get_input():
    while True:
        for i in range(len(stacks)):
            print("please enter {0} for {1}.".format(letters[i] , stacks[i].name))
        letter = input().upper()
        if letter in letters:
            for i in range(len(letters)):
              if letters[i] == letter:
                return stacks[i]
            break
        else:
            print("please enter a valid letter.")
#game:
num_moves = 0
while True:
    while True:
        print("---------current stacks-------")
        for i in stacks:
            print(i.list)
        print("which stack do you want to move from?")
        stack_to_remove = get_input()
        print("which stack do you want to move to?")
        stack_to_go = get_input()
        if (stack_to_remove.size > 0) and (stack_to_go.size <=stack_to_go.limit):
            if stack_to_go.size == 0 :
                number_to_remove = stack_to_remove.list.pop()
                stack_to_go.list.append(number_to_remove)
                stack_to_go.size +=1
                stack_to_remove.size -=1
                num_moves +=1
                break
            elif stack_to_go.list[-1] > stack_to_remove.list[-1]:
                number_to_remove = stack_to_remove.list.pop()
                stack_to_go.list.append(number_to_remove)
                stack_to_go.size +=1
                stack_to_remove.size -=1
                num_moves +=1
                break
            else:
                print("""

            The value you wanna add should be less than the value on the stick.


            """)
        else:
            print("""
              Be careful to select the sticks that have values on them.
              """)
    if right_stick.size == right_stick.limit:
        print("Congradulation! you won in {0} moves".format(num_moves))
        break
