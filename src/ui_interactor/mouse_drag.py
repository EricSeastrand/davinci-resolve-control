import pyautogui
pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

class MouseDrag:
	
	def __init__(self):
		self.timeout_ms = 1000
		self.state = {
			'action': None,
			'x': None,
			'y': None,
			'drag_start': [0,0],
			'subject': None,
			'timestamp_last_change': 0
		}

	def is_drag_timed_out(self):
		current_time = current_milli_time()
		time_since_previous = current_time - self.state['timestamp_last_change']
		return time_since_previous > self.timeout_ms

	def update_mouse_state(self):
		x,y = pyautogui.position()
		self.state['x'] = x
		self.state['y'] = y

	def drag_start(self, element, x,y):
		pyautogui.moveTo(x,y)
		self.update_mouse_state()
		self.state['action'] = 'drag'
		self.state['drag_start'] = [x,y]
		self.state['subject'] = element
		pyautogui.mouseDown()

	def xy_is_where_we_started(self, x,y):
		if self.state['drag_start'][0] != x:
			return False

		if self.state['drag_start'][1] != y:
			return False

		return True

	def element_is_subject(self, element):
		if not self.state['subject']:
			return False

		subject = self.state['subject']
		if subject.automation_id == element.automation_id:
			return True
		
		return False

	def is_dragging(self):
		return self.state['action'] == 'drag'

	def drag_on_element(self, element, x, y):
		if self.is_drag_timed_out():
			print("Time out")
			self.drag_stop()

		if not self.is_dragging() or not self.element_is_subject(element):
			element_midpoint = element.get_pointer().rectangle().mid_point()
			self.drag_stop()
			self.drag_start(element, element_midpoint[0], element_midpoint[1])

		self.do_drag(x, y)


	def do_drag(self, x, y):
		self.state['x'] = self.state['x'] + x
		self.state['y'] = self.state['y'] + y
		pyautogui.moveTo(self.state['x'], self.state['y'])
		self.state['timestamp_last_change'] = current_milli_time()

	def drag_stop(self):
		pyautogui.mouseUp()
		self.state['action'] = None
		self.state['drag_start'] = [0,0]

import time
def current_milli_time():
    return round(time.time() * 1000)