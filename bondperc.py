import numpy as np
import matplotlib.pyplot as plt

N = 40
p = 0.3

def createVertices(p, N):
	mat = np.zeros((N, N))
	for x in np.nditer(mat, op_flags=['readwrite']):
		if np.random.uniform() < p:
			x[...] = -1
	return mat

# analyse a cell
def analyse(val, r, c, mat, cluster):
	val = mat[r, c]
	
	if (mat[r, c] == (-1)): # if vertex is open
		val = mat[r, c]
		mat[r, c] = cluster

		if c < (N-1) and mat[r,c + 1] == (-1):
			#print '[{}, {}]: up exists'.format(r, c)
			analyse(val, r, c+1, mat, cluster)
		if c > (0) and mat[r,c - 1] == (-1):
			#print '[{}, {}]: down exists'.format(r, c)
			analyse(val, r, c-1, mat, cluster)
		if r < (N-1) and mat[r + 1,c] == (-1):
			#print '[{}, {}]: right exists'.format(r, c)
			analyse(val, r+1, c, mat, cluster)
		if r > (0) and mat[r - 1,c] == (-1):
			#print '[{}, {}]: left exists'.format(r, c)
			analyse(val, r-1, c, mat, cluster)
		else:
			return mat
	else:
		return mat

# init
M = createVertices(p, N)
cl = 1
# compute
for row in xrange(M.shape[0]):
	for col in  xrange(M.shape[1]):
		if M[row,col] == (-1): # if vertex is open
			M = analyse(M[row,col], row, col, M, cl)
			cl += 1
plt.imshow(np.transpose(M), cmap='Accent', interpolation='nearest')
plt.show()

# make sure there are no consecutive cells with different cluster
test = []
for row in xrange(M.shape[0]-1):
	for col in  xrange(M.shape[1]-1):
		if M[row, col] != 0:
			if M[row+1, col] != 0:
				test.append(M[row, col] != M[row+1, col])
			if M[row, col+1] != 0:
				test.append(M[row, col] != M[row, col+1])
print '{}/{}={}'.format(sum(test), len(test), float(sum(test))/len(test))