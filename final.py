#  Python coursework 2011
#  UP622197
#  "Patchwork"

from graphics import *


#  Main function to get grid size and colours
def main():
    #  Choose size of grid
    while True:
        columns = eval(input("Please choose a grid size min. 2 x 2, max. 8 x 8\n\
How many columns?: "))
        if columns > 1 and columns < 9:
            break
    while True:
        rows = eval(input("Please choose a grid size min. 2 x 2, max. 8 x 8\n\
How many rows?: "))
        if rows > 1 and rows < 9:
            break
    #  Choose colours
    colourChoice = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    print("Enter four space seperated colours e.g.: 'red green blue cyan'\n\
Valid colours are: ", colourChoice)
    colours = input("colours: ").split(' ')
    for i in range(4):
        while colours[i] not in colourChoice:
            print(colours[i], "is not valid, please \
choose another from the following:  ", colourChoice)
            colours[i] = (input("Replace invalid colour with: "))
        else:
            colourChoice.remove (colours[i])
    #  Define size and draw window
    width = columns * 101
    height = rows * 101
    win = GraphWin("Patchwork", width, height)
    win.setCoords(0, 0, width, height)
    drawPatchwork(win, rows, columns, height, colours)
    replacePatchwork(win, rows, columns, height, colours)
    win.getMouse()
    win.close()
    

#  Draw the patchwork
def drawPatchwork(win, rows, columns, height, colours):
    colourCycle = 0
    for i in range(rows):
        for j in range(columns):
            colour = colours[colourCycle % 4]
            if (i + j)%2 == 0:
                bottomY = (height - 100) - (i * 101)
                topY = height - (i * 101)
                bottomX = 0 + (j * 101)
                topX = 100 + (j * 101)
                drawSquares(win, bottomX, bottomY, topX, topY, colour)
            else:
                boatX = 13 + (j * 101)
                boatY = (height - 91) - (i * 101)
                drawBoats(win, boatX, boatY, colour)
            colourCycle = colourCycle + 1
            

#  Swap tiles
def replacePatchwork(win, rows, columns, height, colours):
    while True:
        swap = input("Would you like to swap two tiles? \
To end, enter or type 'no'. ")
        if swap == "" or swap == "no":
            break
        print("Select the two tiles to swap by clicking on each one.")
        #  Get coordinates of tiles to swap
        firstTile = win.getMouse()
        secondTile = win.getMouse()
        xList = [firstTile.getX(), secondTile.getX()]
        yList = [firstTile.getY(), secondTile.getY()]
        for i in range(2):
            #  Calculate location, colour and pattern of selected tiles
            x1 = xList[i] // 100
            y1 = rows - ((yList[i] // 100) + 1)
            x2 = xList[i - 1] // 100
            y2 = rows - ((yList[i - 1] // 100) + 1)
            tileColour = int(((y2 * columns + x2) % 4))
            colour = colours[tileColour]
            if (y2 + x2)%2 == 0:
                bottomY = (height - 100) - (y1 * 101)
                topY = height - (y1 * 101)
                bottomX = 0 + (x1 * 101)
                topX = 100 + (x1 * 101)
                drawSquares(win, bottomX, bottomY, topX, topY, colour)
            else:
                boatX = 13 + (x1 * 101)
                boatY = (height - 91) - (y1 * 101)
                #  Background for covering swapped tiles
                boatBackground = Rectangle (Point (boatX - 12, boatY - 8), \
                                    Point (boatX + 89, boatY + 90))
                boatBackground.setFill("white")
                boatBackground.setOutline("white")
                boatBackground.draw(win)
                drawBoats(win, boatX, boatY, colour)
    print("Click anywhere in the graphics window to close")
    

#  Draw squares [pattern no. 9]
def drawSquares(win, bottomX, bottomY, topX, topY, colourInput):
    for i in range (10):
            xMove = topX - (i * 10)
            yMove = topY - (i * 10)
            #  Check odd/even
            if i%2 == 0:
                colour = "white"
            else:
                colour = colourInput
            square = Rectangle(Point (bottomX, bottomY), \
                               Point (xMove, yMove))
            square.setFill(colour)
            square.draw(win)
            #  Reset colour
            colour = colourInput


#  Draw boats [pattern no. 7]
def drawBoats(win, boatX, boatY, colour):
    for i in range (4):
        for j in range (3):
            x = boatX + (i * 25)
            y = boatY + (j * 34)
            #  Set boat coordinates
            boatSail = Polygon (Point (x - 12, y), Point (x, y + 21), \
                                Point (x + 12,  y))
            boatMast = Line (Point (x, y), Point (x, y - 4))
            boatHull = Polygon (Point (x - 8, y - 9), Point (x + 7, y - 9), \
                                Point (x +12, y - 4), Point (x - 12, y - 4))
            #  Draw boat
            boatSail.setFill(colour)
            boatSail.draw(win)
            boatMast.draw(win)
            boatHull.draw(win)

#  Python coursework 2011
#  UP622197
#  "Patchwork"
