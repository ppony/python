
import abc

"""class Context:
	def __init__(self, strategy):
		self._strategy = strategy

	def call_func(self):
		self._strategy.erase_func()
		self._strategy.prog_func()	
"""

class Strategy(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def erase_func(self):
		pass

	@abc.abstractmethod
	def prog_func(self):
		pass


#class ICP(Strategy):
#	def erase_func(self):
#		print('icp erase')
#	def prog_func(self):
#		print('icp prog')

#class ISP(Strategy):
#	def erase_func(self):
#		print('isp erase')
#	def prog_func(self):
#		print('isp prog')

#if __name__=="__main__":
#	_isp = ISP()
#	_icp = ICP()
#	con=Context(_icp)
#	con.call_func()
#	con=Context(_isp)
#	con.call_func()
#	con=Context(_icp)
#	con.call_func()
