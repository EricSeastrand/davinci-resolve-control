from midi.controller import Controller
from midi.message import Message

controller = Controller(input_id=2)

def on_message(raw_message, timing):
	print(raw_message)
	message = Message(raw_message)

	print(message.summary())

controller.start_loop(on_message)