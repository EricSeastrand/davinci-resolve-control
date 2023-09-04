class Element(object):
	"""
		Abstracts the minutiae of interacting with onscreen UI elements
	"""
	def __init__(self, automation_id, retriever_function):
		self.automation_id = automation_id
		self.retriever_function = retriever_function
		self._pointer = None
		self._properties = None

	def get_pointer(self):
		if not self._pointer:
			retrieved = self.retriever_function(self)
			self._pointer = retrieved['pointer']
			self._properties = retrieved['properties']

		return self._pointer
	
