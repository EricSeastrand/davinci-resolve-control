import pytest
from application_connector import ApplicationConnector
from ui_interactor.element_map import ElementMap, ElementNotFoundException

# Primaries tab in DaVinci Resolve
automation_id_of_a_real_element = "UiMainWindow.bigBossWidget.widgetStack_Panel.WStackPage_Color.m_pColorPanel.frameVerticalContainer.frameColorBottom.frameColorBottomToolbar.frameColorBottomToolbarButtons.btnColorWheels"

@pytest.fixture(scope="session")
def connector_connected():
	process_descriptor = {
		'title_re': "DaVinci Resolve.*?",
		#'process': pid
	}

	connector = ApplicationConnector(
		process_descriptor = process_descriptor,
	)
	connector.start()

	return connector


@pytest.fixture
def map_instance():
	return ElementMap(
		element_list = mock_element_list,
	)

@pytest.mark.integration
def test_map_instance_can_find_an_element(connector_connected):
	element_map = ElementMap(
		element_list = connector_connected.elements
	)

	element = element_map.lookup(automation_id=automation_id_of_a_real_element)

	assert element
