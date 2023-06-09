import pygame
import button
import requests

WIN_WIDTH = 550 
background_color = (255,255,255)
buffer = 5
solved =0

grid = [
    [1, 9, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 2]]
grid_original = [[grid[x][y] for y in range (len(grid[0]))] for x in range (len(grid))]

def insert(win, position):
    i, j = position[1], position[0]
    numberFont = pygame.font.SysFont('VCR OSD Mono', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                #keep value of grid original
                if grid_original[i-1][j-1] != 0:
                   return
                #remove if value is 0
                if event.key == 48 :
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):  #checking for valid input
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = numberFont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 +15, position[1]*50))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return

def sudoku_board(win):
    for i in range(0, 10):
        if i % 3 == 0 :
            pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 5)
            pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 5)
        pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 2)

def original_number(win):
    numberFont = pygame.font.SysFont('VCR OSD Mono', 35)
    for i in range (0, len(grid[0])):
        for j in range (0, len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = numberFont.render(str(grid[i][j]), True, (0, 0, 0)) # angka original
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 + 7))

def isEmpty(num):
    if num == 0:
        return True
    return False

def isValid(position, num):
    #Checking row
    for i in range(0, len(grid[0])):
        if(grid[position[0]][i] == num):
            return False

    #Checking column
    for i in range(0, len(grid[0])):
        if(grid[i][position[1]] == num):
            return False

    #Check sub-grid
    x = position[0]//3*3
    y = position[1]//3*3
    for i in range(0,3):
        for j in range(0,3):
            if(grid[x+i][y+j]== num):
                return False
    return True

def sudoku_solver(win):
    numberFont = pygame.font.SysFont('VCR OSD Mono', 35)
    for i in range(0,len(grid[0])):
        for j in range(0, len(grid[0])):
            if(isEmpty(grid[i][j])): 
                for k in range(1,10):
                    if isValid((i,j), k):                   
                        grid[i][j] = k
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = numberFont.render(str(k), True, (0,0,0))
                        win.blit(value, ((j+1)*50 +15,(i+1)*50 +7))
                        pygame.display.update()
                        
                        sudoku_solver(win)
                        
                        #Exit condition
                        global solved
                        if(solved == 1):
                            return
                        
                        #if sudoku_solver returns, there's a mismatch
                        grid[i][j] = 0
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()
                return               
    solved = 1

def reset_board(win):
    for i in range (0, len(grid[0])):
        for j in range (0, len(grid[0])):
            if grid[i][j] != grid_original[i][j]:
                grid[i][j] = 0
                pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                pygame.display.update()

def check_answer():
    temp = 0
    for i in range(0,len(grid[0])):
        for j in range(0,len(grid[0])):
            if grid[i][j] != 0:
                temp = grid[i][j]
                grid[i][j] = 0
                if isValid((i, j), temp) == False:
                    grid[i][j] = temp
                    return False
                grid[i][j] = temp
    return True

def submit(win):
    if check_answer() == True:
        textFont = pygame.font.SysFont('VCR OSD Mono', 15)
        desc_text = textFont.render('Not Have Problem', True, (34,139,34))
        win.blit(desc_text, (50, WIN_WIDTH-15))
        pygame.display.update()
        pygame.draw.rect(win, background_color, (50, WIN_WIDTH-15, 200, 200))
    else:
        textFont = pygame.font.SysFont('VCR OSD Mono', 15)
        desc_text = textFont.render('Have Problem', True, (255,0,0))
        win.blit(desc_text, (50, WIN_WIDTH-15))
        pygame.display.update()
        pygame.draw.rect(win, background_color, (50, WIN_WIDTH-15, 200, 200))
    return

def answer(win):
    sudoku_solver(win)
    return

def reset(win):
    reset_board(win)
    return

def main():
    pygame.init()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH+50))
    pygame.display.set_caption("SudoKuy by Valen Ujik Aan")
    win.fill(background_color)
    
    sudoku_board(win)
    pygame.display.update()

    submit_img = pygame.image.load('submit.png').convert_alpha()
    # reset_img = pygame.image.load('reset.png').convert_alpha()
    answer_img = pygame.image.load('enter.png').convert_alpha()

    submit_button = button.Button(WIN_WIDTH-165,WIN_WIDTH-25, submit_img, 0.5)
    answer_button = button.Button(WIN_WIDTH-100,WIN_WIDTH-20, answer_img, 0.1) 
    # reset_button = button.Button(WIN_WIDTH-100,WIN_WIDTH-25, reset_img, 0.5)
    submit_button.update(win)
    answer_button.update(win)
    # reset_button.update(win)
    pygame.display.update()

    original_number(win)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()

                if submit_button.check_input(win, pos):
                    submit(win)
                elif answer_button.check_input(win, pos):
                    answer(win)
                # elif reset_button.check_input(win, pos):
                    # reset(win)
                else:
                    insert(win, (pos[0]//50, pos[1]//50))

            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()