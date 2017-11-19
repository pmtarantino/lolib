import numpy
import pdb

def swap_column(m,i,j):
	a = m.copy()
	a[:, i], a[:, j] = a[:, j], a[:, i].copy()
	return a

def swap_row(m,i,j):
	a = m.copy()
	a[i,:], a[j,:] = a[j,:], a[i,:].copy()
	return a

def swap(m,i,j):
	return swap_column(swap_row(m,i,j),i,j)

def sum_up(m):
	x = [sum(m[i][i+1:]) for i in range(len(m))]
	return sum(x)

m = numpy.loadtxt("instances/IO/N-be75eec", dtype=int)


print m
print sum_up(m)
new = swap(m,0,1)
print new
print sum_up(new)