import numpy as np

def get_odd_magic_square(n):
	magicSquare = np.zeros((n,n),dtype=int)
	
	maxNum = n**2
 
	num = 1
	i = n//2
	j = n-1
		
	while num < maxNum+1:
	
		if not magicSquare[i%n,j%n]:
			
			magicSquare[i%n,j%n] = num
			num += 1
			
			j += 1
			i -= 1
		
		else:
			j -= 2
			i += 1
			
	return magicSquare		

def get_random_square(n):
	return np.random.permutation(np.arange(1,n**2+1)).reshape((n,n))
	
def isMagicSquare(m):
	
	n = m.shape[0] 
	
	sumLine = n*(n**2+1)//2 
	
	
	if m.trace() != sumLine:
		return False
	
	sumNum = 0
	for i in range(n):
		sumNum += m[i,n-i-1]
	if sumNum != sumLine:
		return False
	
	for i in range(n):
		if sum(m[i,:]) != sumLine:
			return False
	
	for j in range(n):
		if sum(m[:,j]) != sumLine:
			return False

	return True
 
n = int(input())

print("Generating random square (size = {}): \n".format(n))
magicSquare = get_random_square(n)
print(magicSquare)
print("\nIt is{} a magic square!\n".format("" if isMagicSquare(magicSquare) else " not"))


if n%2:
	print("This is a magic square (size = {}): \n".format(n))
	magicSquare = get_odd_magic_square(n)
	if not isMagicSquare(magicSquare):
		print("ERROR!")
	else:
		print(magicSquare)
		print("\nIts each line and diags sum = {}.".format(n*(n**2+1)//2))
	
else:
	print("Magic square of this size can't be generated. The developer requires more coffee and ideas...")




