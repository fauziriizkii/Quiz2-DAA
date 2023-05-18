import pygame 
import button 
import requests 

WIN_WIDTH = 550 
background_color = (255,255,255)
buffer = 5


solved =0 
grid = [ 
    [0, 6, 0, 0, 1, 2, 0, 5, 0],
    [0, 5, 3, 7, 8, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 9],
    [2, 0, 4, 6, 7, 0, 5, 9, 1],
    [6, 0, 5, 3, 4, 1, 7, 8, 0],
    [8, 0, 1, 0, 0, 0, 0, 0, 3],
    [0, 1, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 7, 9, 0, 6],
    [0, 0, 6, 0, 0, 0, 2, 7, 0]]
grid_original = [[grid[x][y] for y in range (len(grid[0]))] for x in range (len(grid))]


def insert(win, position):


    i, j = position[1], position[0]
    numberFont = pygame.font.SysFont('VCR OSD Mono', 35)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if grid_original[i-1][j-1] != 0:
                   return
                if event.key == 48 :
                    grid[i-1][j-1] = event.key - 48
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):  
                    
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = numberFont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 +15, position[1]*50 + 8))
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
                value = numberFont.render(str(grid[i][j]), True, (128, 0, 0)) 
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 + 8)) 

def isEmpty(num):
    
    if num == 0:
        
        return True
    return False

def isValid(position, num):
    
    for i in range(0, len(grid[0])):
        
        if(grid[position[0]][i] == num):
            return False
    for i in range(0, len(grid[0])):
        
        if(grid[i][position[1]] == num):
            return False
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
                        win.blit(value, ((j+1)*50 +15,(i+1)*50 +8))
                        pygame.display.update()

                        sudoku_solver(win)
                        
                        
                        global solved
                        if(solved == 1):
                        
                            return
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
        desc_text = textFont.render('This Sudoku is solved.', True, (34,139,34))
        win.blit(desc_text, (48, WIN_WIDTH+13))
        pygame.display.update()
        pygame.draw.rect(win, background_color, (115, WIN_WIDTH-8, 200, 200))
    else:
        

        textFont = pygame.font.SysFont('VCR OSD Mono', 15)
        desc_text = textFont.render('There is a problem.', True, (255,0,0))
        win.blit(desc_text, (48, WIN_WIDTH+13))
        pygame.display.update()
        pygame.draw.rect(win, background_color, (115, WIN_WIDTH-8, 200, 200))
    return

def answer(win):
    
    sudoku_solver(win)
    return

def main():
    pygame.init() 
    win = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH+50))
    pygame.display.set_caption("SudoKuy by Aan Ujik Valen")
    win.fill(background_color)

    #show the Contributors
    # 1. Andrian Tambunan - 5025211018
    # 2. Fauzi Rizki Pratama - 5025211220
    # 3. Beauty Valen Fajri - 5025211227
    textFont = pygame.font.SysFont('VCR OSD Mono', 15)
    text = textFont.render('SudoKuy by :', True, (0,0,0))
    win.blit(text, (48, WIN_WIDTH-47))
    pygame.display.update()
    pygame.draw.rect(win, background_color, (500, WIN_WIDTH-8, 200, 200))

    textFont = pygame.font.SysFont('VCR OSD Mono', 15)
    text = textFont.render('Andrian T.- 5025211018', True, (0,0,0))
    win.blit(text, (48, WIN_WIDTH-32))
    pygame.display.update()
    pygame.draw.rect(win, background_color, (500, WIN_WIDTH-8, 200, 200))

    textFont = pygame.font.SysFont('VCR OSD Mono', 15)
    text = textFont.render('Fauzi Rizki P.- 5025211220', True, (0,0,0))
    win.blit(text, (48, WIN_WIDTH-17))
    pygame.display.update()
    pygame.draw.rect(win, background_color, (500, WIN_WIDTH-8, 200, 200))
    
    textFont = pygame.font.SysFont('VCR OSD Mono', 15)
    text = textFont.render('Beauty Valen F.- 5025211227', True, (0,0,0))
    win.blit(text, (48, WIN_WIDTH-2))
    pygame.display.update()
    pygame.draw.rect(win, background_color, (500, WIN_WIDTH-8, 200, 200))

    sudoku_board(win)
    pygame.display.update()
    check_img = pygame.image.load('Asset/check.png').convert_alpha() 
    solve_img = pygame.image.load('Asset/solve.png').convert_alpha() 

    check_button = button.Button(WIN_WIDTH-240,WIN_WIDTH-20, check_img, 0.2)
    
    solve_button = button.Button(WIN_WIDTH-137,WIN_WIDTH-20, solve_img, 0.2) 
    
    check_button.update(win)
    solve_button.update(win)
    pygame.display.update()

    original_number(win)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()

                if check_button.check_input(win, pos):
                    submit(win) 
                elif solve_button.check_input(win, pos):
                    answer(win)
                else:
                    insert(win, (pos[0]//50, pos[1]//50))

            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()