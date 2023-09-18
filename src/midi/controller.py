from rtmidi import MidiIn
import time

class Controller:
	def __init__(self, input_id):
		self.input_id = input_id
		self.poll_ms = 100
		self.midi_input = MidiIn()
		self.keep_listening = False

		try:
			self.init_connection()
		except:
			print(f"Can't open midi controller connection id:{input_id}. Check list..")
			self.get_ports()
			raise Exception("Can't find midi controller.")


	def init_connection(self):
		self.port = self.midi_input.open_port(port=self.input_id)
		print(f"opened port {self.port}")

	def get_ports(self):
		ports = self.midi_input.get_ports()
		print(ports)
		return ports

	def start_loop(self, callback):
		self.keep_listening = True
		while self.keep_listening:
			message = self.port.get_message()

			if message:
				data = message[0]
				timing = message[1]
				callback(data, timing)
			else:
				print("Sleeping")
				time.sleep(self.poll_ms / 1000)




def on_midi_message(message):
	print(message)

