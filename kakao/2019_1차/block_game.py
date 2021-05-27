

def search_block_index(board):

    horizon = []
    vertical = []


    # search horizontaly
    for y in range(len(board) - 1):

        for x in range(len(board)-2):
            temp = []

            temp.append(board[y][x])
            temp.append(board[y][x+1])
            temp.append(board[y][x+2])
            temp.append(board[y+1][x])
            temp.append(board[y+1][x+1])
            temp.append(board[y+1][x+2])

            cnt = 0

            for i in temp :
                if i == 0:
                    cnt +=1
            
            if cnt == 2:
                
                if (temp[1]==0 and temp[2]==0) and (temp[0]==temp[3]==temp[4]==temp[5]):
                    horizon.append((x,y))

                elif (temp[0]==0 and temp[1]==0) and (temp[2]==temp[3]==temp[4]==temp[5]):
                    horizon.append((x,y))


                elif (temp[0]==0 and temp[2]==0) and (temp[1]==temp[3]==temp[4]==temp[5]):
                    horizon.append((x,y))


    # search vertically
    for y in range(len(board) - 2):

        for x in range(len(board)-1):
            temp = []

            temp.append(board[y][x])
            temp.append(board[y][x+1])
            temp.append(board[y+1][x])
            temp.append(board[y+1][x+1])
            temp.append(board[y+2][x])
            temp.append(board[y+2][x+1])

            cnt = 0

            for i in temp :
                if i == 0:
                    cnt +=1
            
            if cnt == 2:
                
                if (temp[0]==0 and temp[2]==0) and (temp[1]==temp[3]==temp[4]==temp[5]):
                    vertical.append((x,y))

                elif (temp[1]==0 and temp[3]==0) and (temp[0]==temp[2]==temp[4]==temp[5]):
                    vertical.append((x,y))

    return vertical, horizon



def remove_block(vertical,horizon,board):

    cnt = 0

    for i in vertical:

        x = i[0]
        y = i[1]

        check = False
        
        for j in range(0,y):
            if board[j][x] != 0:
                check = True
                break
            if board[j][x+1] != 0:
                check = True
                break            

        if check:
            continue
        else :
            board[y][x] = board[y+1][x] = board[y+2][x] = board[y][x+1] = board[y+1][x+1] = board[y+2][x+1] = 0
            cnt +=1


    for i in horizon:
        x = i[0]
        y = i[1]
        
        check = False

        for j in range(0,y):
            if board[j][x] != 0:
                check = True
                break
                
            elif board[j][x+1] != 0:
                check = True
                break    

            elif board[j][x+2] != 0:
                check = True
                break    

        if check:
            continue
        else :
            board[y][x] = board[y][x+1] = board[y][x+2] = board[y+1][x] = board[y+1][x+1] = board[y+1][x+2] = 0
            cnt +=1

    return cnt

           




def solution(board):

    answer = 0


    for x in board:
        print(x) 
    print("222222222222222222222222222222222222222222222")
    while True:


        vertical, horizon = search_block_index(board)

        cnt = remove_block(vertical,horizon,board)

        for x in board:
            print(x) 
        
        print(cnt)
        answer += cnt

        if cnt ==0:
            break




    return answer










board = [
    [0,0,0,0,3,0,0,0,0,0],
    [0,2,0,0,3,3,1,0,0,0],
    [0,2,2,2,3,0,1,0,0,0],
    [0,0,0,1,0,1,1,0,0,0],
    [0,1,1,1,0,0,4,0,0,0],
    [0,0,0,0,0,4,4,0,0,0],
    [0,0,0,0,3,0,4,0,0,0],
    [0,0,0,2,3,0,0,0,5,5],
    [1,2,2,2,3,3,2,0,0,5],
    [1,1,1,0,0,0,2,2,2,5]
    ]


answer = solution(board)

print(answer)




