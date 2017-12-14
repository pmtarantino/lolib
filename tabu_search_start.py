import numpy
import pdb
from random import randint
from utils import *
import time

def improve_start(m):

	rows = m.shape[0]-1

	for row in range(0,rows):
		
		# Recorro las filas
		mcandidato = 0
		mcol = 0

		for col in range(0,rows):
		
			# Por cada fila, me muevo por las columnas
			candidato = sum_col(m,col,row)
			if candidato > mcandidato:
				mcandidato = candidato
				mcol = col

		# Genero este vecino
		m = swap(m,mcol,row+1)

	return m

def tabu_search(group, instance):
	m = numpy.loadtxt("instances/" + group + "/N-" + instance, dtype=int)

	m = improve_start(m)

	original = m

	# Start
	total = 0
	accum = []
	optimal = get_optimal(group, instance)
	iterations = 20

	for t in range(0,iterations):

		s1 = time.time()
		
		tabu_list = LimitedFifo(10)

		m = original
		value = lop(m) # Valor a maximizar
		old_value = value-1 # To start

		rows = m.shape[0]-1

		iterations = 0

		while value > old_value:
			iterations = iterations + 1
			old_value = value

			mayorM = m
			for row in range(0,rows):
				
				c1 = row#randint(0,rows)
				c2 = randint(0,rows)

				# Genero este vecino
				tempm = swap(m,c1,c2)
				tempvalue = lop(tempm)

				if tempvalue >= value and not tabu_list.is_in(tempm):
					value = tempvalue
					tabu_list.add(tempm)
					mayorM = tempm

			m = mayorM


		s2 = time.time()

		accum.append(value)
		total = total+value

	mean = numpy.mean(accum)
	std = numpy.std(accum)
	print group, "&", instance, "&", optimal, "&", mean, "&", int(std), "&", round((optimal-mean)*100/optimal,2), "&", iterations, "&", round(s2-s1,2)

instances = {}
instances['IO'] = ['be75eec','be75np','stabu75','t59i11xx','t65w11xx','t59n11xx','t70w11xx','t75u11xx']
instances['SBG'] = ['sgb75.07','sgb75.09','sgb75.11','sgb75.13']#['sgb75.01','sgb75.03','sgb75.05','sgb75.07','sgb75.09','sgb75.11','sgb75.13']
instances['MB'] = ['r100a2','r150b1','r200b0','r250c0','r250e0']
#instances['XLOLIB'] = ['be75eec_150','t75d11xx_150','t75k11xx_250','tiw56n67_150','tiw56n67_250','tiw56r66_250']

for group in instances:
	for inst in instances[group]:
		tabu_search(group, inst)