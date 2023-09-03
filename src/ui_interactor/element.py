class Element(object):
	"""
		Abstracts the minutiae of interacting with onscreen UI elements
	"""
	def __init__(self, automation_id, retriever_function):
		self.automation_id = automation_id
		self.retriever_function = retriever_function
		self._pointer = None

	def get_pointer(self):
		if not self._pointer:
			self._pointer = self.retriever_function(self)

		return self._pointer
	
