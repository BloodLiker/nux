import math

def arithmatic ( args ):
	args [ 0 ] = args [ 0 ].replace ( '\r\n', '' )
	for letter in 'abcdefghijklmnopqrstuvwxyz':
		args [ 0 ] = args [ 0 ].replace ( letter, '' )
	solution = str ( eval ( args [ 0 ], { '__builtins__' : {} } ) )
	return solution

def sine ( args ):
	solution = str ( math.sin ( float ( args [ 0 ] ) * ( 2 * math.pi ) / 360 ) )
	return solution

def cosine ( args ):
	solution = str ( math.cos ( float ( args [ 0 ] ) * ( 2 * math.pi ) / 360 ) )
	return solution

def tangent ( args ):
	solution = str ( math.tan ( float ( args [ 0 ] ) * ( 2 * math.pi ) / 360 ) )
	return solution
