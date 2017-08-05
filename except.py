import time


while True:
	try:
		time.sleep(1)
		raise IndexError('12')
	except IndexError as e:
		print(type(e),str(e))
		print('except')

