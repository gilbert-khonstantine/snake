snake = [[0,0]]
new_coor = [999999,999999]
num_step = 0
data = "EEEELLLL"
movements = list(data)
head = 0
directions = [0,1,2,3] #NWSE resp.

for i in range(len(movements)):
    if head ==0:
        if movements[i]=="L":
            head = directions[(head+1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]-1
            new_coor[1] = temp[1]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]-1
            new_coor = [99999,999999]

        elif movements[i]=="R":
            head = directions[(head-1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]+1
            new_coor[1]=temp[1]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]+1
            new_coor = [99999,999999]

        elif movements[i] == "F":
            num_step+=1
            temp = snake[-1]
            new_coor[1] = temp[1]+1
            new_coor[0]=temp[0]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][1]= snake[j][1]+1
                new_coor = [99999,999999]

        elif movements[i] == "E":
            num_step+=1
            temp = snake[-1]
            new_coor[1] = temp[1]+1
            new_coor[0] = temp[0]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)

            new_coor = [99999,999999]

    if head ==1:
        if movements[i]=="L":
            head = directions[(head+1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]
            new_coor[1] = temp[1]-1
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]-1
            new_coor = [99999,999999]

        elif movements[i]=="R":
            head = directions[(head-1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[1] = temp[1]+1
            new_coor[0]=temp[0]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]+1
            new_coor = [99999,999999]

        elif movements[i] == "F":
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]-1
            new_coor[1]=temp[1]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][1]= snake[j][1]+1
                new_coor = [99999,999999]

        elif movements[i] == "E":
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]-1
            new_coor[1]=temp[1]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)

            new_coor = [99999,999999]

    if head ==2:
        if movements[i]=="L":
            head = directions[(head+1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]+1
            new_coor[1] = temp[1]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]-1
            new_coor = [99999,999999]

        elif movements[i]=="R":
            head = directions[(head-1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[1] = temp[1]
            new_coor[0]=temp[0]-1
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]+1
            new_coor = [99999,999999]

        elif movements[i] == "F":
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]
            new_coor[1]=temp[1]-1
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][1]= snake[j][1]+1
                new_coor = [99999,999999]

        elif movements[i] == "E":
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]
            new_coor[1]=temp[1]-1
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)

            new_coor = [99999,999999]
    
    if head ==3:
        if movements[i]=="L":
            head = directions[(head+1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]
            new_coor[1] = temp[1]+1
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]-1
            new_coor = [99999,999999]

        elif movements[i]=="R":
            head = directions[(head-1)%4]
            num_step+=1
            temp = snake[-1]
            new_coor[1] = temp[1]-1
            new_coor[0]=temp[0]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][0]= snake[j][0]+1
            new_coor = [99999,999999]

        elif movements[i] == "F":
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]+1
            new_coor[1]=temp[1]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)
                snake.pop(0)
                # for j in range(len(snake)):
                #     snake[j][1]= snake[j][1]+1
                new_coor = [99999,999999]

        elif movements[i] == "E":
            num_step+=1
            temp = snake[-1]
            new_coor[0] = temp[0]+1
            new_coor[1]=temp[1]
            if new_coor in snake:
                print(num_step)
                break
            else:
                snake.append(new_coor)

            new_coor = [99999,999999]


    if len(movements)==num_step:
        print(snake)
        print("YES")
