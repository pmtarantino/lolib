import numpy
from md5 import md5

# Funciones para hacer el Swap
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

# Funcion a maximizar
def lop(m):
	x = [sum(m[i][i+1:]) for i in range(len(m))]
	return sum(x)

# Ver suma de columna a partir de la fila row
def sum_col(m,col,row):
	#print m[:row+1,col]
	return sum(m[:row+1,col])
# Ver suma de la fila a partir de la columna col
def sum_row(m,row,col):
	#print m[row,col:]
	return sum(m[row,col:])

def hash_matrix(m):
	m.flags.writeable = False
	return hash(m.data)

def get_optimal(group, instance):

	optimo = {}

	optimo['IO'] = {}
	optimo['IO']['be75eec']		= 236464
	optimo['IO']['be75np']		= 716994
	optimo['IO']['stabu75'] 	= 553303
	optimo['IO']['t59i11xx'] 	= 8261545
	optimo['IO']['t65w11xx'] 	= 138181029
	optimo['IO']['t59n11xx'] 	= 20928
	optimo['IO']['t70w11xx'] 	= 224319954
	optimo['IO']['t75u11xx'] 	= 52708323

	optimo['SBG'] = {}
	optimo['SBG']['sgb75.01'] = 2724126
	optimo['SBG']['sgb75.03'] = 2747384
	optimo['SBG']['sgb75.05'] = 2707863
	optimo['SBG']['sgb75.07'] = 2727928
	optimo['SBG']['sgb75.09'] = 2687364
	optimo['SBG']['sgb75.11'] = 2732686
	optimo['SBG']['sgb75.13'] = 2714591

	optimo['MB'] = {}
	optimo['MB']['r100a2'] = 145270
	optimo['MB']['r150b1'] = 347627
	optimo['MB']['r200b0'] = 651237
	optimo['MB']['r250c0'] = 1010961
	optimo['MB']['r250e0'] = 1008267

	optimo['XLOLIB'] = {}
	optimo['XLOLIB']['be75eec_150'] = 3482828
	optimo['XLOLIB']['t75d11xx_150'] = 9642140
	optimo['XLOLIB']['t75k11xx_250'] = 4093849
	optimo['XLOLIB']['tiw56n67_150'] = 2372926
	optimo['XLOLIB']['tiw56n67_250'] = 6324858
	optimo['XLOLIB']['tiw56r66_250'] = 4948414


	return optimo[group][instance]

class LimitedFifo():

	def __init__(self, num=10):
		self.list = [None] * num

	def add(self, elem):
		self.list.pop()
		elem = hash_matrix(elem)
		self.list.insert(0,elem)

	def list(self):
		return self.list

	def is_in(self,elem):
		return hash_matrix(elem) in self.list