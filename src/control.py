import IPython
from time import sleep

from application_connector import ApplicationConnector

from ui_interactor.element_map import ElementMap, ElementNotFoundException
from ui_interactor.element import Element

process_descriptor = {
	'title_re': "DaVinci Resolve.*?",
	#'process': pid
}

print("Initializing application")
connector = ApplicationConnector(
	process_descriptor = process_descriptor,
)
connector.start()

def refresh_element_map():
	connector.load_elements()
	element_map.element_list = connector.elements

print("Loading element map")
element_map = ElementMap(
	element_list = connector.elements
)
retriever_function = element_map.make_retriever_function()

print("Initializing button controllers")
activate_tab_primaries = Element(
	automation_id = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnColorWheels",
	retriever_function = retriever_function
)

activate_tab_hdr = Element(
	automation_id = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnHdr",
	retriever_function = retriever_function
)

exposure_slider = Element(
	automation_id = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorHDRTab.frameWidgetContainer.stackedWidget.stackedColorWheelsWidgetContainer.colorWheelsWidget.primaryTopHoldFrame.groupBoxZone4.frameZone4FooterContainer.frameZone4DualSliderContainer.zone4LumaLabelSlider",
	retriever_function = retriever_function
)

gain_wheel = Element(
	automation_id = 'UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorWheelsTab.colorWheelsMainContainer.colorWheelsSplitter.colorWheelsStackedWidget.threeWayColorWidget.primaryTopHoldFrame.groupBoxGain.frameGainFooterContainer.frameGainThumbHolder.gainThumbWheel',
	retriever_function = retriever_function
)

def make_element(automation_id):
	return Element(
		automation_id = automation_id,
		retriever_function = retriever_function
	)

hdr_tab_activate_wheels = make_element('UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorHDRTab.colorWheelTopFrame.btnWheelsView')
hdr_tab_wheel_page_selector = make_element('UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorHDRTab.frameWidgetContainer.stackedWidget.stackedColorWheelsWidgetContainer.colorWheelsWidget.frameTopToolbar.hdrColorZonesScroller')
hdr_tab_wheel_page_right = make_element('UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorHDRTab.frameWidgetContainer.stackedWidget.stackedColorWheelsWidgetContainer.colorWheelsWidget.frameTopToolbar.btnHDRColorZoneRightScroller')

gain_color_ball = make_element('UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorWheelsTab.colorWheelsMainContainer.colorWheelsSplitter.colorWheelsStackedWidget.threeWayColorWidget.primaryTopHoldFrame.groupBoxGain.gainWheel')

def go_to_hdr_exposure():
	activate_tab_hdr.get_pointer().click()
	hdr_tab_activate_wheels.get_pointer().click()
	
	page_selector_rect = hdr_tab_wheel_page_selector.get_pointer().rectangle()
	if page_selector_rect.width() == 0:
		import time
		time.sleep(0.100)
		page_selector_rect = hdr_tab_wheel_page_selector.get_pointer().rectangle()
	
	import math
	click_x = math.floor(page_selector_rect.width() / 14 * 12)
	click_y = math.floor(page_selector_rect.height() / 2)
	
	print(f"Sending to {click_x}, {click_y}")
	hdr_tab_wheel_page_selector.get_pointer().click_input(coords=(click_x,click_y))	

	exposure_slider.get_pointer().move_mouse_input(absolute=False)

def go_to_gain_global():
	activate_tab_primaries.get_pointer().click()
	gain_wheel.get_pointer().move_mouse_input(absolute=False)

def go_to_gain_color():
	activate_tab_primaries.get_pointer().click()
	xy = gain_color_ball.get_pointer().rectangle().mid_point()
	gain_color_ball.get_pointer().move_mouse_input(coords=xy)

def gain_color_adjust(x, y):
	mouse_drag.drag_on_element(gain_color_ball, x, y)

def hdr_exposure_adjust(x):
	mouse_drag.drag_on_element(exposure_slider, x, 0)

#descendants = exposure_slider.get_pointer().descendants()
# In [11]: descendants[4].get_properties()
# Out[11]:
# {'class_name': 'BmdDavUI::UiDoubleSlider',
#  'friendly_class_name': 'Slider',
#  'texts': [''],
#  'control_id': None,
#  'rectangle': <RECT L1078, T1991, R1236, B2001>,
#  'is_visible': True,
#  'is_enabled': True,
#  'control_count': 0,
#  'is_keyboard_focusable': True,
#  'has_keyboard_focus': False,
#  'automation_id': ''}

# descendants[4].set_value(1000) # https://github.com/pywinauto/pywinauto/blob/bf7f789d01b7c66ccd0c213db0a029da7e588c9e/pywinauto/controls/uia_controls.py#L687
# print(exposure_slider)
#
#colorwheel = element_map.lookup("UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorWheelsTab.colorWheelsMainContainer.colorWheelsSplitter.colorWheelsStackedWidget.threeWayColorWidget.primaryTopHoldFrame.groupBoxGain.gainWheel")

from midi.controller import Controller
from midi.message import Message

controller = Controller(input_id=2)

from ui_interactor.mouse_drag import MouseDrag

mouse_drag = MouseDrag()



def on_message(raw_message, timing):
	print(raw_message)
	message = Message(raw_message)

	print(message.summary())

	if message.type == 'button' and message.control_id==1 and message.button_state == 'down':
		go_to_hdr_exposure()

	if message.type == 'button' and message.control_id==2 and message.button_state == 'down':
		go_to_gain_color()

	if message.type == 'dial' and message.control_id==1:
		sensitivity = 1
		direction = -1 if message.direction == 'down' else 1
		hdr_exposure_adjust(sensitivity * direction)

	if message.type == 'dial' and (message.control_id==2 or message.control_id==3):
		sensitivity = 1
		if message.direction == 'up':
			amount = sensitivity
		if message.direction == 'down':
			amount = -sensitivity

		#pointer = gain_color_ball.get_pointer()
		
		

		if message.control_id == 2:
			gain_color_adjust(amount, 0)
		if message.control_id == 3:
			gain_color_adjust(0, amount)
		
		
		#pointer.click_input(button='move', coords=coords, absolute=False, pressed="")
		

def on_message_with_reload(raw_message, timing):
	try:
		on_message(raw_message, timing)
	except ElementNotFoundException:
		print("Could not find element. Will try a refresh.")
		refresh_element_map()
		#on_message(raw_message, timing)

controller.start_loop(on_message_with_reload)


IPython.embed()
