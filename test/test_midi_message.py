import pytest

from midi.message import Message


def test_parses_midi_bytes_correctly():
	raw_message = [176, 34, 65]

	message = Message(raw_message)

	assert message.status_byte == 176, "Status byte was wrong"
	assert message.data_byte1 == 34, "Data byte 1 was wrong"
	assert message.data_byte2 == 65, "Data byte 2 was wrong"

# They come in zero-indexed, but we want 1-indexed for this "16 button controller"
def test_detects_correct_button_or_knob():
	raw_message = [176, 3, 65]

	message = Message(raw_message)

	assert message.control_id == 4, "Button/Knob number was wrong"

def test_detects_dial_turns():
	raw_message = [176, 3, 65]

	message = Message(raw_message)

	assert message.type == 'dial', "Supposed to be a dial message"

def test_detects_dial_turn_down():
	raw_message = [176, 3, 63]

	message = Message(raw_message)

	assert message.direction == 'down', "Direction should be down"

def test_detects_dial_turn_up():
	raw_message = [176, 3, 65]

	message = Message(raw_message)

	assert message.direction == 'up', "Direction should be up"

def test_detects_button_press():
	raw_message = [177, 3, 0]

	message = Message(raw_message)

	assert message.type == 'button', "Supposed to be a button message"

def test_detects_button_press():
	raw_message = [177, 3, 127]

	message = Message(raw_message)

	assert message.button_state == 'down', "Direction should be down"

def test_detects_button_release():
	raw_message = [177, 3, 0]

	message = Message(raw_message)

	assert message.button_state == 'up', "Direction should be up"
