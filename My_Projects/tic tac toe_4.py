import random

combinations = [[1,2,3],[4,5,6],[7,8,9],
                [1,4,7],[2,5,8],[3,6,9],
                [1,5,9],[3,5,7]]

occupied = []
positions = [1,2,3,4,5,6,7,8,9]

def gameBoard():
    print("""
             {} | {} | {} 
          ------------------
             {} | {} | {} 
          ------------------
             {} | {} | {}

    """.format(positions[0],positions[1],positions[2],
                positions[3],positions[4],positions[5],
                positions[6],positions[7],positions[8]))

def checkWinner(pos,user_ch):
    for i in range(len(combinations)):
        if pos in combinations[i]:
            index = combinations[i].index(pos)
            combinations[i][index] = user_ch

    
    for i in range(len(combinations)):
        if combinations[i][0] == user_ch and combinations[i][1] == user_ch and combinations[i][2] == user_ch:
        elif combinations[i][0] == cpu_ch and combinations[i][1] == cpu_ch and combinations[i][2] == cpu_ch: 
            return "winner"

def user_moves(user_ch):
    pos = int(input("Enter the position : "))
    positions[pos - 1] = user_ch
    occupied.append(pos - 1)
    gameBoard()
    winner = checkWinner(pos,user_ch)
    return winner

def cpu_moves(cpu_ch):
    while True:
        if len(occupied) < 8:
            cpu_pos = random.randint(0, 8)
            if cpu_pos in occupied:
                print("Position Already Occupied...")
            else:
                print("CPU Moved at",cpu_pos+1)
                positions[cpu_pos] = cpu_ch
                occupied.append(cpu_pos)
                break
        else:
            print("Out of values")
            break
    gameBoard()
    winner = checkWinner(cpu_pos+1,cpu_ch)
    return winner

def main():
    print("******************************Welcome to TIC--TAC--TOE**************************")
    gameBoard()
    user_ch = input("Please Enter a choice : X or O : ")
    print("You have picked :",user_ch)
    if user_ch == "X" or user_ch == "x":
        cpu_ch = O
    else: cpu_ch = "X"
    while True:
        result = user_moves(user_ch)
        if result == "winner":
            print("User win")
            break

        result = cpu_moves(cpu_ch)
        if result == "winner":
            print("CPU Win")
            break

main()
