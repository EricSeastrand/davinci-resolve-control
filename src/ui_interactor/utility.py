def calc_center_point(coords):
	w = coords['R'] - coords['L']
	h = coords['B'] - coords['T']

	print(f"H is {h}")
	if w < 0:
		raise Exception("Left must be less than Right.")
	
	if h < 0:
		raise Exception("Top must be less than Bottom")

	x = coords['R'] - (w / 2)
	y = coords['B'] - (h / 2)

	return [x, y]

def drag_mouse_relative(element, x, y, button="left"):
	from pywinauto.timings import Timings

	start_coords = element.rectangle().mid_point()
	end_coords   = (start_coords.x + x, start_coords.y + y)
	
	#element.drag_mouse_input(dest_point)
	element.press_mouse_input(button, start_coords)
	#time.sleep(Timings.before_drag_wait)
	# for i in range(5):
	#     self.move_mouse_input((press_coords[0] + i, press_coords[1])) # "left"
	#     #time.sleep(Timings.drag_n_drop_move_mouse_wait)
	element.move_mouse_input(end_coords) # "left"
	#time.sleep(Timings.before_drop_wait)
	element.release_mouse_input(button, end_coords)