import time 
import os

while True:
	l = {}
	print('tutorial:\n\
type "end" for end your exam\
\ntype "st" for stop your exam(take break or any thing)\
\ntype "eNum" to edit than question Num answer\
\ntype "bl" to see your blank answers\
\ntype "0" to esc question\
')
	s = int(input('Starting number : '))
	qNum = s
	qS = qNum
	qNow = qNum
	input('Press ENTER to start...')
	t = time.time()
	n = input(str(qNow)+' : ').lower()
	flag = False
	st = 0
	while n != 'end':
		if n != 'st' and n != '':		
			if n[0] == 'e': 
				if n[1:].isdigit():
					qNow = int(n[1:])
					flag = True
				else:
					print('invalid answer')
			elif flag:
				flag = False
				l[qNow] = n
				qNow = qNum
			else:
				l[qNow] = n
				qNum += 1
				qNow = qNum
			if n == 'bl':
				print(f'{list(l.values()).count("0")} tests are blank')
				for i,j in l.items():
					if j == '0':
						print(f'{i} || ',end='')
				print()
		elif n == 'st':
			v = time.time()
			input('press ENTER to continue...')
			st += time.time()-v
		t2 = time.time()
		n = input(str(qNow)+' : ').lower()
	print('---------------------')
	r = 0
	w = 0
	b = 0
	l2 = []
	for i in range(len(l)):
		n = input(f'Right for "{qS+i}" : ')
		if l[qS+i] == '0':
			b += 1
		elif l[qS+i] != n :
			w += 1
			l2 += [[i+qS,n,l[qS+i]]]
		else:
			r += 1
	x = t2 -t - st
	print(f'Timing : {int(x//60)}:{int(x%60)}    ,    T/Q : {round((x/60)/len(l),2)}')
	print(f'Right : {r} , Wrong : {w} , Blank : {b}')
	print(f'with-: {round((r-w/3)/len(l)*100,2)},  without- : {round((r)/len(l)*100,2)}')
	print('Type "wr" to see wrong answers')
	print('Type "bl" to see blank tests') 
	print('Tppe "fl" to write results in txt file (not available)')
	com = input('Press ENTER to clear Terminal and start new or type "new" to start from begining | ')
	while com!= '' and com != 'new':  
		if com == 'fl':
			com = input('Write some information for your txt file : ')
			file = open(time.strftime('%Y-%m-%d %H_%M_%S')+'.txt','w')
			file.write(com)
			file.write('\n')
			file.write(f'Timing : {int(x//60)}:{int(x%60)}    ,    T/Q : {round((x/60)/len(l),2)}')
			file.write('\n')
			file.write(f'Right : {r} , Wrong : {w} , Blank : {b}')
			file.write('\n')
			file.write(f'with-: {round((r-w/3)/len(l)*100,2)},  without- : {round((r)/len(l)*100,2)}')
			file.write('\n')
			file.write('Blanks : \n')
			for i,j in l.items():
					if j == '0':
							file.write(str(i)+'\n')
			file.write('Wrongs : \n')
			for i in l2:
					file.write(f'q : {i[0]} , right : {i[1]} , yours : {i[2]}')
					file.write('\n')
			file.close()
		elif com == 'bl':
			for i,j in l.items():
				if j == '0':
					print(i)
		elif com == 'wr':
			for i in l2 :
				print(f'q : {i[0]} , right : {i[1]} , yours : {i[2]}')
		com = input('Press ENTER to clear Terminal and start new or type "new" to start from begining | ')
	if com == '':
		os.system('cls' if os.name == 'nt' else 'clear')




