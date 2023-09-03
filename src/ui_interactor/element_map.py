class ElementMap(object):
	"""
		Provides the Element abstraction with pointers to actual pywinauto/Win32/uia elements
	"""
	def __init__(self, element_list):
		super(ElementMap, self).__init__()
		self.element_list = element_list

	def lookup(self, automation_id):
		for item in self.element_list:
			properties = item['properties']
			if properties['automation_id'] != automation_id:
				continue

			return item

		raise ElementNotFoundException(f"Could not find element matching automation_id='{automation_id}'")
	
	
	def make_retriever_function(self):
		def retriever_function(dependent_element):
			nonlocal self
			lookup_result = self.lookup(dependent_element.automation_id)
			return lookup_result['pointer']

		return retriever_function



class ElementNotFoundException(Exception):
    "raised if search for an element yields no matches"
    pass