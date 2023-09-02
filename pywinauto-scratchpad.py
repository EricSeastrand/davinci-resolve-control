from pywinauto.application import Application
from pywinauto import timings
from pywinauto import actionlogger

pid = 10964

actionlogger.enable()

timings.Timings.fast() # divide all timings by two (~2x faster)

automation_id = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorHDRTab.colorWheelTopFrame.btnWheelsView"

# 2A.22178E.4.800017F7
primaries = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnColorWheels"

# 2A.22178E.4.8000363D
hdr = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnHdr"

app = Application(
	backend="uia",
	allow_magic_lookup=False
).connect(process=pid)
#.connect(title_re="DaVinci Resolve.*?")

import pprint

window = app.window(class_name="UiMainWindowImp")
pprint.pprint(window)
#window.print_control_identifiers()

#window.dump_tree()


app_root = "UiMainWindow.bigBossWidget"

# hdr_button = get_element_by_id_path(hdr, window)

hdr_button = window.child_window(
	auto_id=hdr,
	control_type="CheckBox",
)
print(hdr_button)
print(hdr_button.handle)

#primaries_button = get_element_by_id_path(primaries, window)
primaries_button = window.child_window(
	auto_id=primaries,
	control_type="CheckBox",
)
print(primaries_button)
print(primaries_button.handle)

hdr_button.print_control_identifiers()

print("Click HDR")
hdr_button.click_input()

print("Click Primaries")
primaries_button.click_input()

print("Click HDR")
hdr_button.click_input()

print("Click Primaries")
primaries_button.click_input()



def get_element_by_id_path(path, window):
	parts = path.split('.')
	path_so_far = ''
	for part in parts:
		if part == 'UiMainWindow':
			continue
		
		path_so_far += part
		
		print("Looking for:"+part)
		look_for = 'UiMainWindow.' +path_so_far
		print(look_for)
		from pywinauto.findwindows import find_elements
		elements = find_elements(
			parent=window,
			process=pid,
			auto_id=look_for
		)
		path_so_far += "."

		if len(elements) < 1:
			raise Exception("No Elements Found for path: "+look_for)

		window = elements[0]

	return window
