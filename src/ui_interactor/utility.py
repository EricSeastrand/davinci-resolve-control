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
