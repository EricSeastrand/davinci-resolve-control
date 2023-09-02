import pyautogui


hdr_wheels = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolsContainer.m_pFrameBottomMain.UiPrimaryWidgetContainer.BorderFrame.frameTabWidgetBorder.stackedWidget.colorHDRTab.colorWheelTopFrame.btnWheelsView"

# L120, T1628, R179, B1658
primaries_tab = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnColorWheels"
primaries_coords = {
	'L': 120,
	'T': 1628,
	'R': 179,
	'B': 1658
}

# L180, T1628, R239, B1658
hdr_tab = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnHdr"
hdr_coords = {
	'L': 180,
	'T': 1628,
	'R': 239,
	'B': 1658
}

def calc_center_point(coords):
	w = coords['R'] - coords['L']
	h = coords['B'] - coords['T']
	x = coords['R'] - (w / 2)
	y = coords['B'] - (h / 2)
	return [x, y]

primaries_xy = calc_center_point(primaries_coords)
hdr_xy = calc_center_point(hdr_coords)
#print(primaries_coords)
#print(primaries_xy)

pyautogui.click(*primaries_xy)

pyautogui.click(*hdr_xy)