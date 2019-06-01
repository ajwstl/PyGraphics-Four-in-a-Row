# -*- coding: utf-8 -*-

"""
A naive version of the popular game for two players to 
get four of the same color in a row horizontally, 
diagonally, or vertically.

See file LICENSE for this code's open source license

"""

__author__ = 'Andrew White <andrew@vivalibre.com>'
__copyright__ = 'Copyright {year}, {project_name}'
__license__ = 'MIT'
__version__ = '0.1'


import sys
try:
	from graphics import *
except ImportError:
	print("This program requires the Python graphics library")
	print("See https://pypi.org/project/graphics.py/")

ROWS = 6
COLS = 7
boardStatus = {}
win = GraphWin("Game", 1000, 800)
win.setBackground('#222223')

def drawHoles():
	for x in range(1, COLS + 1):
		for y in range(1, ROWS + 1):
			center = Point(100 + 100 * x, 100 + 100 * y)
			c = Circle(center, 40)
			c.setFill('#222223')
			c.draw(win)


def drawTitle(title):
	message = Text(Point(win.getWidth()/2, 50), title)
	message.setTextColor('#ddb502')
	message.setStyle('bold')
	message.setSize(36)
	message.draw(win)

def drawBoard():
    # Blue board
	rect = Rectangle(Point(150,150),Point(850,750))
	rect.setFill('#252a5d')
	rect.draw(win)

	# Player 1 area
	p1 = Text(Point(75,160), "Player 1")
	p1.setTextColor("white")
	p1.setSize(20)
	p1.draw(win)
	c1 = Circle(Point(75,225), 40)
	c1.setFill('#7c0901')
	c1.draw(win)
	# Player 2 area
	p2 = Text(Point(925,160), "Player 2")
	p2.setTextColor("white")
	p2.setSize(20)
	p2.draw(win)
	c2 = Circle(Point(925,225), 40)
	c2.setFill("#d6bd00")
	c2.draw(win)
    

def drawPlayerArrow(nextPlayer):
	x = 75 if nextPlayer == 1 else 925
	t = Polygon(Point(x-15,40), Point(x+15,40), Point(x+15, 80), Point(x+30, 80), 
		        Point(x,113), Point(x-30,80), Point(x-15, 80))
	t.setFill("#ddbf02")
	t.draw(win)    


def showWhichPlayerTurn():
	nextPlayer = 1 if boardStatus['lastPlayer'] == 2 else 2
	r1 = Rectangle(Point(0,0), Point(150,140))
	r1.setFill("#222223")
	r1.draw(win)
	r2 = Rectangle(Point(850,0), Point(1000,140))
	r2.setFill("#222223")
	r2.draw(win)
	drawPlayerArrow(nextPlayer)


def getFreeRow(column):
	for row in range(ROWS, 0, -1):
		if not boardStatus[column][row]:
			return row


def showMove(player, column, row):
	color = '#7c0901' if player == 1 else '#d6bd00'
	center = Point(100 + 100 * column, 100 + 100 * row)
	c = Circle(center, 40)
	c.setFill(color)
	c.draw(win)



def makeMove(col):
	row = getFreeRow(col)
	if not row:  # no free slots
		return
	player = 1 if boardStatus['lastPlayer'] == 2 else 2
	showMove(player, col, row)
	boardStatus['lastPlayer'] = player
	boardStatus[col][row] = player
	return (col, row)


def checkForWinOrTie(col, row, plays):
	winner = checkRowWin(row) or checkColWin(col) or checkDiagWin(col, row)
	if plays == ROWS * COLS:
		endGame("tie")
	else:
		if winner:
			return boardStatus['lastPlayer']


def checkRowWin(row):
	lastPlayer = boardStatus['lastPlayer']
	for x in range(1, COLS - 3):
		consecutive = 0
		for offset in range(0, 5):
			if boardStatus[x + offset][row] == lastPlayer:
				consecutive += 1
				if consecutive == 4:
					return True
			else:
				consecutive = 0
	return False


def checkColWin(col):
	lastPlayer = boardStatus['lastPlayer']
	for y in range(1, ROWS - 3):
		consecutive = 0
		for offset in range(0, 5):
			if boardStatus[col][y + offset] == lastPlayer:
				consecutive += 1
				if consecutive == 4:
					return True
			else:
				consecutive = 0
	return False


def checkDiagWin(col, row):
	return checkDiagWinSlash(col, row) or checkDiagWinBackslash(col, row)


def checkDiagWinSlash(col, row):
	for (x, y) in [(1,3), (1,2), (1,1), (2,1), (3,1), (4,1)]:
		xp = x
		yp = y
		d = ''
		while xp <= 7 and yp <= 6:
			if not boardStatus[xp][yp]:
				d += '0'
			else:
				d += str(boardStatus[xp][yp])
			xp += 1
			yp += 1
		if "1111" in d or "2222" in d:
			return True
	return False


def checkDiagWinBackslash(col, row):
	for (x, y) in [(4,1), (5,1), (6,1), (7,1), (7,2), (7,3)]:
		xp = x
		yp = y
		d = ''
		while xp >= 1 and yp <= 6:
			if not boardStatus[xp][yp]:
				d += '0'
			else:
				d += str(boardStatus[xp][yp])
			xp -= 1
			yp += 1
		if "1111" in d or "2222" in d:
			return True
	return False


def endGame(winner):
	if winner != "tie":
		message = Text(Point(win.getWidth()/2, 400), "Player {} Wins!".format(winner))
		message.setTextColor('white')
		message.setStyle('bold')
		message.setSize(36)
		message.draw(win)
	else:
		message = Text(Point(win.getWidth()/2, 400), "It's a tie!")
		message.setTextColor('white')
		message.setStyle('bold')
		message.setSize(36)
		message.draw(win)
	message = Text(Point(win.getWidth()/2, 770), "Click anywhere to start over".format(winner))
	message.setTextColor('white')
	message.setStyle('bold')
	message.setSize(20)
	message.draw(win)
	win.getMouse()
	rect = Rectangle(Point(200,750), Point(800,800))
	rect.setFill('#222223')
	rect.draw(win)


def getColumnClick(click):
	x = click.getX()
	for column in range(1, COLS + 1):
			left = 60 + 100 * column
			right = 60 + 100 * (column + 1)
			if x > left and x < right:
				return column 


def getPlayerMove():
	while True:
		click = win.getMouse()
		column = getColumnClick(click)
		if column:
			break
	return makeMove(column)


def main():
	try:
		while True:
			for column in range(1, COLS + 1):
				boardStatus[column] = {}
				for row in range(1, ROWS + 1):
					boardStatus[column][row] = False
			drawTitle("Four In A Row")
			drawBoard()
			drawHoles()
			boardStatus['lastPlayer'] = 2
			plays = 0
			while True:
				showWhichPlayerTurn()
				try:
					(col, row) = getPlayerMove()
				except TypeError:
					continue
				plays += 1
				winner = checkForWinOrTie(col, row, plays)
				if winner:
					endGame(winner)
					break
	except (KeyboardInterrupt, GraphicsError):
		sys.exit()


if __name__ == '__main__':
	sys.exit(main())
