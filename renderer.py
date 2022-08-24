import pygame
import math
import time

#gameflow:
game_is_running = True

#initialize
pygame.init()
pygame.font.init()

#gamesettings:
fps = 60
prev_time = time.time()
dt = 0
scrw = 800
ox = scrw/2
scrh = 600
oy = scrh/2
wins=((scrw,scrh))
screen = pygame.display.set_mode(wins)
pygame.display.set_caption('3D Cube Renderer')
clock = pygame.time.Clock()

#colours:
mcolor = (255,255,255)
bgcolor = (0,0,0)

#gamevar:
cverts = [[[1],[1],[1]],[[-1],[1],[1]],[[1],[-1],[1]],[[1],[1],[-1]],[[-1],[-1],[1]],[[1],[-1],[-1]],[[-1],[1],[-1]],[[-1],[-1],[-1]]]
cvertrad = 10
rotang = 0
projmat = [[1,0,0],[0,1,0]]
scalemat = [[100,0,0],[0,100,0],[0,0,100]]
linewidth = 2

def quit_game():
    pygame.quit()
    quit()

def matmul2d(a,b):
    c = []
    for row in range(len(a)):
       curr_row = []
       for col in range(len(b[0])):
           curr_row.append(0)
       c.append(curr_row)
    for i in range(len(a)):
       for j in range(len(b[0])):
           curr_val = 0
           for k in range(len(a[0])):
                curr_val += a[i][k]*b[k][j]
           c[i][j] = curr_val
    return c 

def connect_vert(i,j,arr):
    pygame.draw.line(screen,mcolor,(ox+arr[i][0][0],oy+arr[i][1][0]),(ox+arr[j][0][0],oy+arr[j][1][0]),linewidth)

def draw_model():
    global cverts,projection_matrix,rotang
    a = math.cos(rotang)
    b = math.sin(rotang)
    rotmatx = [[1,0,0],[0,a,-b],[0,b,a]]
    rotmaty = [[a,0,b],[0,1,0],[-b,0,a]]
    rotmatz = [[a,-b,0],[b,a,0],[0,0,1]]
    transmat = []
    for c in cverts:
        stv = matmul2d(scalemat,c)
        rtv = matmul2d(rotmatx,stv)
        rtv = matmul2d(rotmaty,rtv)
        ptv = matmul2d(projmat,rtv)
        pygame.draw.circle(screen,mcolor,(ox+(ptv[0][0]),oy+(ptv[1][0])),cvertrad)
        transmat.append(ptv)
    rotang += 1*dt
    connect_vert(0,1,transmat)
    connect_vert(0,2,transmat)
    connect_vert(2,4,transmat)
    connect_vert(4,1,transmat)
    connect_vert(3,5,transmat)
    connect_vert(5,7,transmat)
    connect_vert(7,6,transmat)
    connect_vert(6,3,transmat)
    connect_vert(6,1,transmat)
    connect_vert(5,2,transmat)
    connect_vert(7,4,transmat)
    connect_vert(3,0,transmat)

def main():
    draw_model()

while game_is_running:
    now = time.time()
    dt = now - prev_time
    prev_time = now
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            game_is_running = False
    screen.fill(bgcolor)
    if __name__ == "__main__":
        main()
    #updatedisplayandsetfps
    pygame.display.update()
    clock.tick(fps)
quit_game()
