# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , A, B, C):
	if n==1:
		print ("Move disk 1 from source",A,"to destination",C)
		return
	TowerOfHanoi(n-1, A, C, B)
	print ("Move disk",n,"from source",A,"to destination",C)
	TowerOfHanoi(n-1, B, A, C)
		
# Driver code
n = 3
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods
