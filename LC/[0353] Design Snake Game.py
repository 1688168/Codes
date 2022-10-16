from collections import deque
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.height=height
        self.width=width
        self.food=food
        self.fd_idx=0
        self.snake_body=deque([(0,0)]) #body size is score
        self.snake_set=set()
        self.snake_set.add((0,0))
        self.x=0
        self.y=0




    def move(self, direction: str) -> int:
        #remove tail
        if direction=='R':
            dx, dy=0, 1
        elif direction=='U':
             dx, dy=-1, 0
        elif direction=='L':
             dx, dy=0, -1
        elif direction=='D':
             dx, dy=1, 0
        else:
            print("thow exception")
            pass
        nx, ny=self.x+dx, self.y+dy
        #print("snake body: ", self.snake_body)
        tail=self.snake_body.pop()
        self.snake_set.remove(tail)
        #print(" nx: ", nx, " ny: ", ny, " set: ", self.snake_set)
        if nx >= self.height or nx < 0 or ny >=self.width or ny<0 or (nx, ny) in self.snake_set:
            #print("dead!!!")
            return -1
        
        #add head
        self.x=nx
        self.y=ny
        self.snake_body.appendleft((nx, ny))
        self.snake_set.add((nx, ny))
        #hasFood?
        #print("nx: ", nx, "ny: ", ny)
        if self.fd_idx < len(self.food) and nx==self.food[self.fd_idx][0] and ny==self.food[self.fd_idx][1]:
            self.fd_idx +=1
            self.snake_body.append(tail)
            self.snake_set.add(tail)
        return len(self.snake_body)-1


        #put back the tail



# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
