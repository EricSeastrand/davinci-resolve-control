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

print("Clicking buttons")

from time import sleep

for i in range(1, 11):
	print("HDR")
	activate_tab_hdr.get_pointer().click()
	sleep(.5)
	print("Primaries")
	activate_tab_primaries.get_pointer().click()
