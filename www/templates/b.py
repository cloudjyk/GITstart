class hello(object):
	"""docstring for hello"""
	def __init__(self, name):
		# super(hello, self).__init__()
		self.name = name
	def print_hello(self):
		print('hello %s' % self.name)
if __name__ == '__main__':
	Nancy = hello('nancy')
	Nancy.print_hello()
		