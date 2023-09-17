class Message:
	def __init__(self, raw_message):
		self.status_byte = raw_message[0]
		self.data_byte1 = raw_message[1]
		self.data_byte2 = raw_message[2]

		self.type_mapping = {
			176: self.decode_dial,
			177: self.decode_button
		}

		self.decode_message()

	def summary(self):
		summary = {
			'control_id': self.control_id,
			'type'      : self.type
		}

		if self.type == 'button':
			summary['button_state'] = self.button_state
		elif self.type == 'dial':
			summary['direction'] = self.direction
		else:
			raise Exception(f"Not sure how to summarize control type: {self.type}")
		return summary

	def decode_message(self):
		if self.status_byte not in self.type_mapping:
			raise Exception(f"Unknown message type: type_mapping doesn't know about status_byte={self.status_byte}.")
		
		handler = self.type_mapping[self.status_byte]
		
		self.control_id = self.data_byte1 + 1

		
		handler()


	def decode_button(self):
		self.type = 'button'

		button_states = {
			0  : 'up',
			127: 'down'
		}

		if self.data_byte2 not in button_states:
			raise Exception(f"Unknown button state {self.data_byte2}")

		self.button_state = button_states[self.data_byte2]

	def decode_dial(self):
		self.type = 'dial'

		dial_directions = {
			65 : 'up',
			63 : 'down'
		}

		if self.data_byte2 not in dial_directions:
			raise Exception(f"Unknown dial direction {self.data_byte2}")

		self.direction = dial_directions[self.data_byte2]