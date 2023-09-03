from pywinauto.application import Application
from pywinauto import timings
from pywinauto import actionlogger

pid = 10964

process_descriptor = {
	'title_re': "DaVinci Resolve.*?",
	#'process': pid
}

actionlogger.enable()

timings.Timings.fast() # divide all timings by two (~2x faster)


app = Application(
	backend="uia",
	allow_magic_lookup=False
).connect(**process_descriptor)


import pprint

window = app.window(class_name="UiMainWindowImp")
#pprint.pprint(window)
#window.dump_tree(filename='dump-nodes.txt')

elements = window.descendants()

primaries_tab = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnColorWheels"
hdr_tab = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnHdr"


elements_data = []
for element in elements:
	properties = element.get_properties()
	elements_data.append(properties)

	if properties['automation_id'] == primaries_tab:
		print("FOUND PRIMARIES!")
		primaries_btn = element
		
	if properties['automation_id'] == hdr_tab:
		print("FOUND HDR_BTN!")
		hdr_btn = element

print(primaries_btn)
print(hdr_btn)

from time import sleep

print("primaries_btn clicking")
primaries_btn.click()
print("primaries_btn clicked")

sleep(.1)
print("hdr_btn clicking")
hdr_btn.click()
print("hdr_btn clicked")

sleep(.1)
print("primaries_btn clicking")
primaries_btn.click()
print("primaries_btn clicked")

sleep(.1)
print("hdr_btn clicking")
hdr_btn.click()
print("hdr_btn clicked")

sleep(.1)
print("primaries_btn clicking")
primaries_btn.click()
print("primaries_btn clicked")

sleep(.1)
print("hdr_btn clicking")
hdr_btn.click()
print("hdr_btn clicked")

sleep(.1)

# app_root_id = "UiMainWindow.bigBossWidget"

# app_root = window.child_window(
# 	auto_id=app_root_id
# )

# elements = app_root.find_elements()

# print(elements)

