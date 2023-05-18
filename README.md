# Quiz2-DAA
| Name  | NRP  | Class |
| :------------ |:---------------| :-----|
| Andrian Tambunan     | 5025211018 | DAA H |
| Fauzi Rizki Pratama      | 5025211220        |   DAA H |
| Beauty Valen Fajri  | 5025211227        |    DAA E |
## Design

![unnamed](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/62681940-80f0-4842-ac07-abeec1881328)  Picture 1. SudoKuy

SudoKuy is a logic-based number puzzle game. The main objective of the game is to fill all the boxes with numbers from 1 to 9. Sudoku requires players to think logically according to the rules of the game.

![unnamed (1)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/cd9266d3-cc5c-4963-8466-eb3791a03e70) Picture 2. Check

When the user starts playing the SudoKuy game and fills in the empty boxes with numbers from 1 to 9, then clicks "Check" at the bottom right corner, the game will perform a check on the filled-in boxes. If there is an error, the game will display the following

![unnamed (2)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/5a0d2e88-8cec-4a05-a608-5836c3983264) Picture 3. Output

If the player correctly inputs the numbers, the game will continue.

![unnamed (3)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/b193e42d-9e17-4b0f-9391-34cb5262098e) Picture 4. Solve

If the player finishes playing or gives up during the game, they can click on the "Solve" button in the bottom right corner, and the output will be displayed as follows :

![unnamed (4)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/1f2264d3-5cd3-4ce3-bb6e-92063c5f4f01)
Picture 5. Output

Implementation
By utilizing the Backtracking algorithm, the puzzle in the SudoKuy game can be easily solved within seconds. The Backtracking algorithm is a form of problem-solving strategy that falls under the category of searching for solution space, but it doesn't have to examine all possible options. It only processes the paths that lead to solutions. The Backtracking algorithm is actually a recursive algorithm, where the search process is based on the Depth-First Search (DFS) algorithm. DFS systematically searches all possible solution paths in a tree-like structure.

## Analysis

### button.py

![unnamed (5)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/e054e832-0409-4476-ab76-ae863f2b65e6) Picture 6. button.py

The code imports the pygame module. The code defines a class called Button. The Button class has several methods and attributes :
The __init__ method is the class constructor that will be executed when an object of the Button class is created. This method takes arguments such as x (x-coordinate), y (y-coordinate), image (button image), and scale (image scale). The method performs operations such as resizing the image using pygame.transform.scale, initializing the rect attribute representing the rectangular area surrounding the image, and setting the top-left position of the rectangle using self.rect.topleft. The clicked attribute is initialized with the value False.

The check_input method is used to check if the given position, provided as an argument, is inside the rectangle (self.rect) representing the button. If the position is inside the rectangle, the method returns True; otherwise, it returns False.
The update method is used to update the appearance of the button on the surface by placing the button image at the position specified by self.rect.x and self.rect.y using surface.blit.
So, the meaning of the code surface.blit(self.image, (self.rect.x, self.rect.y)) is to place the button image on the surface at the position specified by the self.rect.x and self.rect.y attributes.

![unnamed (6)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/beac87ba-e252-41f0-8892-ec8ed0f2b7e5) Picture 7. button.py

#### Inside the __init__ method :

width and height are obtained from the image using the get_width() and get_height() methods, respectively.
The image is then scaled using pygame.transform.scale with the new dimensions calculated based on the original dimensions (width and height) and the scale factor.
The self.image attribute is set to the scaled image.

The self.rect attribute is set to the rectangle object obtained from the scaled image using self.image.get_rect().

The top-left position of the rectangle (self.rect.topleft) is set to the provided x and y coordinates.

The self.clicked attribute is initialized to False.

![unnamed (7)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/db43eb0e-be7f-4187-aa06-68d593840941) Picture 8. button.py

The check_input method takes two parameters: surface (the surface to check the input on) and position (the position to check). Inside the check_input method, it checks whether the provided position is within the boundaries of the button rectangle (self.rect) using the collidepoint method. If the position is inside the rectangle, it returns True; otherwise, it returns False.

![unnamed (8)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/2c0ca754-1129-451f-8a6d-7123de86cd1e) Picture 9. button.py

The update method takes one parameter: surface (the surface on which to update the button). Inside the update method. It uses the blit function of the surface object to draw the button image (self.image) onto the surface. The image is placed at the position specified by the self.rect.x and self.rect.y attributes, which represent the top-left coordinates of the button rectangle.

### tempCodeRunnerFile.py

![unnamed (9)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/09217978-8587-4264-9afd-689fb7f8d916) Picture 10. tempCodeRunnerFile.py

Additionally, the code defines several variables and initializes a number grid for a Sudoku game.

import pygame, imports the pygame module used for creating games or graphical applications.

import button, imports the button module, which might be a custom module defined in a separate file and used in this program.

import requests, imports the requests module used for making HTTP requests to a specific URL.

#### Next, there are several variables initialized:

WIN_WIDTH represents the width of the game window with a value of 550.

background_color represents the background color in RGB format with a value of (255, 255, 255), which corresponds to white.

buffer with a value of 5, possibly used as the spacing between elements in the game.

solved is initialized with a value of 0, potentially used to track the number of successfully solved puzzles.

Then, there is the initialization of the number grid for the Sudoku game. The grid represents a 9x9 matrix consisting of numbers from 0 to 9. The number 0 indicates an empty square to be filled. There are two forms of the grid, namely grid and grid_original. grid holds the current status of the Sudoku game, while grid_original stores the initial grid before the player starts the game. Both grids are initialized with the provided numbers in the code.

![unnamed (10)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/b54bdb5c-a146-4bf3-b945-33bb054fec0e) Picture 11. tempCodeRunnerFile.py

The given code defines a function named insert with two parameters: win (representing the game window) and position (representing the position of the cell in the grid where the number will be inserted). Let's break down the code and provide a detailed explanation
The insert function is responsible for inserting a number into the Sudoku grid at the specified position. The function begins by extracting the row and column indices (i and j) from the position parameter. It creates a font object named numberFont using the system font "VCR OSD Mono" with a size of 35. The function enters a while loop, which ensures that it keeps running until a return statement is reached.

Within the while loop it iterates over the events captured by pygame.event.get() to handle them. If the event type is pygame.QUIT, indicating the user closed the game window, the function returns, terminating the program. If the event type is pygame.KEYDOWN, indicating a key press event, the following actions are performed :

The function checks if the original grid value at the specified position (grid_original[i-1][j-1]) is not zero. If it's not zero, it means the cell already contains an initial value, and the function returns without making any changes.
If the pressed key is "0" (event.key == 48), it means the user wants to remove the number from the cell. In this case, the grid value is set to 0, the cell is cleared by drawing a rectangle with the background color over it, and the display is updated using pygame.display.update(). Then, the function returns.

If the pressed key is a number between 1 and 9 (inclusive), it means the user wants to insert that number into the cell. In this case, the grid value is updated with the pressed key value, the cell is cleared, and the number is rendered using the numberFont font object. The updated display is then updated, and the function returns.

![unnamed (11)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/cba21f2a-3f4d-4912-95bd-747cb903072e) Picture 12. tempCodeRunnerFile.py

#### def sudoku_board(win) :

This function is used to draw the lines that form the Sudoku board on the game window (win). The function uses a for loop to iterate from 0 to 9. If i modulo 3 is equal to 0, it means we have reached the boundaries of the larger blocks within the Sudoku board. In this case, the function draws thick lines using pygame.draw.line to separate these blocks. Otherwise, the function draws thin lines as separators for all the cells within the Sudoku board. This function aims to create the visual representation of the Sudoku board with the separating lines between the cells.

#### def original_number(win):

This function is used to display the original numbers that exist in the grid on the game window (win). The function uses nested for loops to iterate through each row and column in the grid. If the number at the grid position is not 0 (indicating it is an original number, not a number entered by the player), the function creates a text object using the numberFont font with the corresponding number. The text object is then displayed on the game window using win.blit(). This function aims to display the original numbers that cannot be changed by the player within the Sudoku board.

![unnamed (12)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/3fe56c93-582b-4468-b649-d617bcd62eb0) Picture 13. tempCodeRunnerFile.py

#### def isEmpty(num) :

This function checks if a number (num) is empty (0) or not. It compares the given number with 0 using the equality operator (==). If the number is 0, it means it is empty, and the function returns True. Otherwise, it returns False.

#### def isValid(position, num) :

This function checks if a number (num) is valid to be placed at a given position in the Sudoku grid (position). The function checks for the validity of the number in three aspects : 

Row Check
It iterates through each element in the row of the given position (position[0]) and compares it with the given number (num). If any element is found to be equal to the number, it means the number is not valid, and the function returns False.
Column Check 
It iterates through each element in the column of the given position (position[1]) and compares it with the given number (num). If any element is found to be equal to the number, it means the number is not valid, and the function returns False.
Sub-grid Check
It determines the starting position (x and y) of the sub-grid based on the given position. It then iterates through the elements of the corresponding 3x3 sub-grid and compares each element with the given number (num). If any element is found to be equal to the number, it means the number is not valid, and the function returns False.

If the number passes all the checks and is valid to be placed at the given position, the function returns True. This function is used to validate whether a number can be placed at a specific position in the Sudoku grid based on the rules of Sudoku.

![unnamed (14)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/6b62b010-8484-49c9-9614-2f5495241bab) Picture 14. tempCodeRunnerFile.py

This function is used to solve Sudoku puzzles using recursion and the backtracking algorithm. It uses the numberFont font with a size of 35 from the Pygame module to display numbers on the game window (win). The function iterates through each row and column in the grid. If an empty cell is found (calling the isEmpty() function), the function attempts to insert numbers from 1 to 9 into that cell to find a valid solution. 

The isValid() function is used to check the validity of the number at the current position. If the number is valid, it is inserted into the cell, and the visual display on the game window is updated. After inserting the number, the sudoku_solver() function is called recursively to continue the search for a solution. 

If a solution is found (solved = 1), the function stops and returns. If no valid number can be inserted into the current cell, the function tries the next number in the next iteration. 

If all numbers from 1 to 9 have been tried and no valid number can be inserted into the current cell, the function returns and goes back to the previous iteration. 

This function uses recursion and backtracking to try various solution possibilities until a valid solution is found. It marks that a solution has been found by changing the value of the solved variable to 1.

Note : The code assumes the use of a global variable solved to track whether a solution has been found.

![unnamed (15)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/f07ea1b9-38c5-47ff-a040-fedc9120984d) Picture 15. tempCodeRunnerFile.py

#### def reset_board(win) :
This function is used to reset the game board by reverting all modified cells back to their original values. 

The function iterates through each row and column in the grid. If the value of a cell in the grid is not equal to the corresponding cell in the original grid, it is reset to 0. 

The visual display on the game window (win) is updated to remove the numbers from those cells. A

fter resetting the game board, the function returns.

#### def check_answer() :
This function is used to check if the current answer on the game board is a valid solution. 

The function uses a temporary variable temp to store the temporary value of a cell during the testing process. 

The function iterates through each row and column in the grid. If the value of a cell in the grid is not 0, it is stored in the temp variable, and the cell is set to 0. 

The isValid() function is used to check the validity of the removed cell value. If the removed cell value is not valid, the original value is restored to the cell, and the function returns False. 

If all non-zero cell values on the game board are valid, the function returns True.

Note : The code assumes the use of a global variable grid_original to store the original values of the game board.

![unnamed (16)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/1588d669-2287-42d8-b55d-05c2845df5c3) Picture 16. tempCodeRunnerFile.py

#### def submit(win) :

This function is used to submit the current solution on the game board for evaluation. It calls the check_answer() function to check if the current solution is correct.

If the return value of check_answer() is True, it means the solution is correct. 
The function displays a message "Not Have Problem" on the game window at the specified coordinates using a specific font and color. 

The display is updated to show the message. A rectangular area is drawn on the game window to clear any previous messages.

If the return value of check_answer() is False, it means there is a problem with the solution. The function displays a message "Have Problem" on the game window at the specified coordinates using a specific font and color. 

The display is updated to show the message. A rectangular area is drawn on the game window to clear any previous messages. The function returns.
#### def answer(win) :

This function is used to automatically solve the Sudoku puzzle on the game board using the sudoku_solver() function. It calls the sudoku_solver() function to solve the Sudoku puzzle. The function returns.

#### def reset(win) :

This function is used to reset the game board by calling the reset_board() function. It calls the reset_board() function to reset the game board. The function returns.
Note : The win parameter represents the game window where the graphical elements are displayed.

![unnamed (17)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/aed8d8d1-6d4c-4c20-ba73-c6085154de7d) Picture 17. tempCodeRunnerFile.py

Essentially, the main() function is responsible for setting up the game display, handling user interactions, and updating the game window based on the events and inputs received.
pygame.init() : Initializes the pygame module to start the game.

win = pygame.display.set_mode((WIN_WIDTH, WIN_WIDTH+50)) : Creates the game window with the specified width and height.

pygame.display.set_caption("SudoKuy by Valen Ujik Aan") : Sets the title of the game window.

win.fill(background_color) : Fills the game window with the specified background color.

sudoku_board(win) : Calls the sudoku_board() function to draw the Sudoku game board

pygame.display.update() : Updates the display of the game window. Reads and loads the submit button, answer button, and reset button images. These images are then converted into objects that can be used in the game.

submit_button = button.Button(WIN_WIDTH-165,WIN_WIDTH-25, submit_img, 0.5) : Creates a submit button object with the specified position, image, and scale.

answer_button = button.Button(WIN_WIDTH-100,WIN_WIDTH-20, answer_img, 0.1) : Creates an answer button object with the specified position, image, and scale.

submit_button.update(win) : Updates the appearance of the submit button on the game window.

answer_button.update(win) : Updates the appearance of the answer button on the game window.

original_number(win) : Calls the original_number() function to draw the initial numbers on the game board.

pygame.display.update() : Updates the display of the game window.

Starts the game loop using while True: .

for event in pygame.event.get(): : Loop to handle all the events that occur in pygame.
I
f the left mouse button is pressed (MOUSEBUTTONUP) and the mouse position is clicked (event.button == 1):
Gets the clicked mouse position.

If the submit button is clicked, calls the submit(win) function to check the filled answer.

If the answer button is clicked, calls the answer(win) function to find the automatic solution for Sudoku.

If the reset button is clicked, calls the reset(win) function to clear all the filled numbers and reset the game board to the initial state.

If no specific button is clicked, calls the insert(win, (pos[0]//50, pos[1]//50)) function to insert a number into a box on the game board.

If the event is a quit event (QUIT), pygame.quit() is called to stop the game.

Returns from the main() function, ending the program execution.

### SudoKuy by Valen Ujik Aan.py
![unnamed (18)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/bcccd48b-b6c8-4177-86f6-a494adfbc384) Picture 18. SudoKuy by Valen Ujik Aan.py

The main() function is the core component of the Sudoku game. It plays a crucial role in initializing the game, setting up the game window, displaying the names of the contributors, drawing the Sudoku board, loading and presenting buttons for checking and solving, displaying the original numbers on the board, and handling various user interactions.

When the main() function is executed, it first initializes the Pygame library using pygame.init() to prepare the game environment. It then creates a game window using the pygame.display.set_mode() function, specifying the window dimensions based on the WIN_WIDTH variable. The window caption is set as "SudoKuy by Aan Ujik Valen" using pygame.display.set_caption().

Next, the window background color is filled using win.fill(background_color) to provide a consistent background for the game. The names of the contributors are displayed using the pygame.font.SysFont() function to set the font style and size, and the win.blit() function to render the text on the window. Each name is rendered separately and positioned accordingly. Rectangles are drawn using pygame.draw.rect() to provide a background for each name.

![unnamed (20)](https://github.com/fauziriizkii/Quiz2-DAA/assets/100081922/7eb2f6b2-b3cd-4942-8a89-66354da9da4b) Picture 19. SudoKuy by Valen Ujik Aan.py

The Sudoku board is drawn on the window using the sudoku_board(win) function, which uses nested loops and the pygame.draw.line() function to create the gridlines and borders of the Sudoku board. The pygame.display.update() function is called after each update to ensure that the changes are visible on the screen.

Buttons for checking and solving are loaded using pygame.image.load() to load the corresponding images, and the button.Button class is used to create the buttons with their positions and scaling factors. The buttons are then displayed on the window using the update() method of each button object. The pygame.display.update() function is called again to update the display. The original numbers of the Sudoku puzzle are displayed on the board using the original_number(win) function. It iterates through the grid list, checks for non-zero values, and renders the numbers on the corresponding positions using the win.blit() function.

Inside the game loop, the program continuously listens for events using pygame.event.get(). When a mouse button is released (pygame.MOUSEBUTTONUP) and the left button is clicked (event.button == 1), the position of the mouse cursor is obtained using pygame.mouse.get_pos(). Depending on the position of the click, different actions are taken. If the check button is clicked, the submit(win) function is called to check the filled answer. If the solve button is clicked, the answer(win) function is invoked to find the automatic solution for the Sudoku puzzle. Otherwise, the insert(win, (pos[0]//50, pos[1]//50)) function is called to insert a number into a specific box on the game board based on the click position.

The game loop continues until a quit event is triggered, either by closing the game window or by a pygame.QUIT event. In either case, the game is terminated by calling pygame.quit(). In summary, the main() function serves as the central controller of the Sudoku game. It handles game initialization, window setup, rendering of UI elements, user interactions, and overall game flow. It combines various functions and events to provide an immersive and interactive Sudoku gaming experience to the player.

### Conclusion

Based on the quiz we have worked on, we have drawn the following conclusions:

The number of empty cells in SudoKuy does not significantly affect the number of backtracking processes.

The more backtracking processes, the more time it takes to complete the SudoKuy game.

In some tested SudoKuy puzzles, the difficulty level affects the number of backtracking processes and the overall completion time.

The accuracy level of the SudoKuy solving program using the backtracking algorithm reaches 100% with 45 empty cells.
