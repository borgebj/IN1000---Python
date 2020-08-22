

class a:
	def __init__(self, a):
		self.a = a


class b:

	def gjornoe(self, a):
		for x in a.a:
			print(x)



dict = {"en":1, "to":2, "tre":3}
a = a(dict)
b = b()
b.gjornoe(a)