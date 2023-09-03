from pywinauto.application import Application

class ApplicationConnector(object):
	"""docstring for ApplicationConnector"""
	def __init__(self, process_descriptor):
		super(ApplicationConnector, self).__init__()
		self.process_descriptor = process_descriptor
		self.app = None
		self.window = None
		self.elements = []
	
	def start(self):
		self.connect()
		self.get_window()
		self.load_elements()

	def connect(self):
		self.app = Application(
			backend="uia",
			allow_magic_lookup=False
		).connect(**self.process_descriptor)

	def get_window(self):
		self.window = self.app.window(class_name="UiMainWindowImp") # ToDo: Is it OK for this to be hardcoded?
		return self.window

	def load_elements(self):
		descendants = self.window.descendants()
		
		self.elements = []
		for element in descendants:
			element_data = {
				"pointer": element,
				"properties": element.get_properties()
			}
			self.elements.append(element_data)

		return self.elements