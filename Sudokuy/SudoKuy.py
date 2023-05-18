# 1. Andrian Tambunan - 5025211018
# 2. Fauzi Rizki Pratama - 5025211220
# 3. Beauty Valen Fajri - 5025211227

import pygame #A library for creating games and multimedia applications.
import button #A custom module (presumably defined in a separate file) for creating buttons in the game.
import requests #A module for making HTTP requests (though it doesn't seem to be used in the code).

WIN_WIDTH = 550 #The width of the game window.
background_color = (255,255,255) #The background color of the game window.
buffer = 5
#The buffer space around the Sudoku grid.
solved =0 #Flag variable.
#A flag variable to track whether the Sudoku puzzle has been solved.
#You need to define the original number first before run this program.
grid = [ #A 9x9 2D Grid
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
#A copy of the original grid to keep track of the initial values.

def insert(win, position):
    #Handles the user's input for inserting numbers into the Sudoku grid.
    #The function uses the Pygame event system to detect user actions.
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
                    #checking if this is a valid input
                    pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                    value = numberFont.render(str(event.key-48), True, (0,0,0))
                    win.blit(value, (position[0]*50 +15, position[1]*50 + 8))
                    grid[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return

def sudoku_board(win):
    #Draws the grid of the game.
    for i in range(0, 10):
        if i % 3 == 0 :
            pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 5)
            pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 5)
            #The board consists of 9x9 cells with lines separating the 3x3 sub-grids.
        pygame.draw.line(win, (0,0,0), (50+50*i, 50), (50+50*i, 500), 2)
        pygame.draw.line(win, (0,0,0), (50, 50+50*i), (500, 50+50*i), 2)
        #The board consists of 9x9 cells with lines separating the 3x3 sub-grids.
def original_number(win):
    #Render the original number of the Sudoku Grid.
    #The original number is stated at the begining of the game.
    numberFont = pygame.font.SysFont('VCR OSD Mono', 35)
    for i in range (0, len(grid[0])):
        for j in range (0, len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = numberFont.render(str(grid[i][j]), True, (128, 0, 0)) #Color
                win.blit(value, ((j+1)*50 + 15, (i+1)*50 + 8)) #Position

def isEmpty(num):
    #Checks if a number in the grid is empty (0).
    if num == 0:
        #It takes a number (num) as a parameter and returns True.
        return True
    return False

def isValid(position, num):
    #Checks if a number can be placed in a specific position of the grid without violating Sudoku rules.
    for i in range(0, len(grid[0])):
        #The function checks if the number is already present in the same row, column, or 3x3 sub-grid.
        if(grid[position[0]][i] == num):
            return False
    for i in range(0, len(grid[0])):
        #The function checks if the number is already present in the same row, column, or 3x3 sub-grid.
        if(grid[i][position[1]] == num):
            return False
    x = position[0]//3*3 #Check the grid
    y = position[1]//3*3
    for i in range(0,3):
        for j in range(0,3):
            if(grid[x+i][y+j]== num):
                return False
    return True

def sudoku_solver(win):
    #Implements a backtracking algorithm to solve the Sudoku puzzle.
    #The function finds the next empty cell and tries to fill it with numbers from 1 to 9.
    numberFont = pygame.font.SysFont('VCR OSD Mono', 35)
    for i in range(0,len(grid[0])):
        for j in range(0, len(grid[0])):
            if(isEmpty(grid[i][j])): 
                for k in range(1,10):
                    if isValid((i,j), k):   
                        #If a number is valid, it fills the cell and recursively calls itself to solve the remaining puzzle.                
                        grid[i][j] = k
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = numberFont.render(str(k), True, (0,0,0))
                        win.blit(value, ((j+1)*50 +15,(i+1)*50 +8))
                        pygame.display.update()

                        sudoku_solver(win)
                        
                        #Exit condition
                        global solved
                        if(solved == 1):
                        #If the puzzle is solved, it sets the solved flag to 1 and returns.
                            return
                        grid[i][j] = 0
                        #If no valid number can be placed, 
                        #it backtracks by setting the cell value to 0 and tries the next number.
                        pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()
                return               
    solved = 1

def reset_board(win):
    #Resets the user-modified cells in the grid to their original values.
    for i in range (0, len(grid[0])):
        for j in range (0, len(grid[0])):
            if grid[i][j] != grid_original[i][j]:
                grid[i][j] = 0
                pygame.draw.rect(win, background_color, ((j+1)*50 + buffer, (i+1)*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                pygame.display.update()
def check_answer():
    #To chect whether the Sudoku grid is valid.
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
    #if check_answer is correct, it will show 'This Sudoku is solved.' tect.
    #Which means the Sudoku grid is valid.
    if check_answer() == True:
        textFont = pygame.font.SysFont('VCR OSD Mono', 15)
        desc_text = textFont.render('This Sudoku is solved.', True, (34,139,34))
        win.blit(desc_text, (48, WIN_WIDTH+13))
        pygame.display.update()
        pygame.draw.rect(win, background_color, (115, WIN_WIDTH-8, 200, 200))
    else:
        #if check_answer is incorrest, it will show 'There is a problem' tect.
        #Which means the Sudoku grid is invalid.
        textFont = pygame.font.SysFont('VCR OSD Mono', 15)
        desc_text = textFont.render('There is a problem.', True, (255,0,0))
        win.blit(desc_text, (48, WIN_WIDTH+13))
        pygame.display.update()
        pygame.draw.rect(win, background_color, (115, WIN_WIDTH-8, 200, 200))
    return

def answer(win):
    #A button to answer the Riddle.
    sudoku_solver(win)
    return

def main():
    pygame.init() #Show the nam eof the game
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
    check_img = pygame.image.load('./Assets/check.png').convert_alpha() #Load image
    solve_img = pygame.image.load('./Assets/solve.png').convert_alpha() #Load image

    check_button = button.Button(WIN_WIDTH-240,WIN_WIDTH-20, check_img, 0.2)
    #Load image
    solve_button = button.Button(WIN_WIDTH-137,WIN_WIDTH-20, solve_img, 0.2) 
    #Load image
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
                    submit(win) #Check input
                elif solve_button.check_input(win, pos):
                    answer(win)#Check input
                else:
                    insert(win, (pos[0]//50, pos[1]//50))

            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()
