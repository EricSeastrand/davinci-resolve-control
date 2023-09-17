from rtmidi import MidiIn
import time
poll_ms = 100

midi_input = MidiIn()

ports = midi_input.get_ports()

print(ports)

port = midi_input.open_port(port=2)

print(port)

def on_midi_message(message):
	print(message)

while True:
	message = port.get_message()

	if message:
		on_midi_message(message)
	else:
		print("Sleeping")
		time.sleep(poll_ms / 1000)
