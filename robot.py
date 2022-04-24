'''A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
'''
import math
pos=[0,0]
while True:
	s=raw_input()
	if not s:
		break
	mov=s.split()
	steps=int(mov[1])
	if mov[0]=='UP':
		pos[1]+=steps
	if mov[0]=='DOWN':
		pos[1]-=steps
	if mov[0]=='LEFT':
		pos[0]-=steps
	if mov[0]=='RIGHT':
		pos[0]+=steps

dist=math.sqrt(pos[0]**2+pos[1]**2)
print pos		
print dist