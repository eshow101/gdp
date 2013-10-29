'''
            GDP - The Generic Device Programmer.

    By Dean Camera (dean [at] fourwalledcubicle [dot] com)
'''

class Transport(object):
	def open(self):
		raise NotImplementedError


	def close(self):
		raise NotImplementedError


	def read(self):
		raise NotImplementedError


	def write(self, data):
		raise NotImplementedError
