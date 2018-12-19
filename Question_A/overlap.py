'''
Author: Georges Hassana
12/19/2018

Description:
	Your goal for this question is to write a program that accepts 
	two lines (x1,x2) and (x3,x4) on 
	the x-axis and returns whether they overlap.

Example: 
As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).

'''

def overlap(line1, line2):

	'''
	This is a function that takes two inputs line1 and line2
	both are tuples and returns "Yes" for overlapping lines
	or "No" for non-overlapping lines
	'''
	a = line1[0]
	b = line1[1]

	c = line2[0]
	d = line2[1]

	result = [max(a,c), min(b,d)]

	if result[0] > result [1]:
		return "No : Not Overlapping "
	else:

		return "Yes:  Overlapping"

# Test

if __name__ == '__main__':
	print(overlap((1,5),(2,6)))
	print(overlap((1,5),(6,8)))
	print(overlap([6,8],[1,5]))
	print(overlap([1,11],[3,10]))
	print(overlap([1,8],[8,10]))



