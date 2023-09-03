import pytest
from application_connector import ApplicationConnector
from pywinauto.application import Application, WindowSpecification
from pywinauto.controls.uiawrapper import UIAWrapper

@pytest.fixture(scope="session")
def connector():
	process_descriptor = {
		'title_re': "DaVinci Resolve.*?",
		#'process': pid
	}

	return ApplicationConnector(
		process_descriptor = process_descriptor,
	)

@pytest.fixture(scope="session")
def connector_connected(connector):
	connector.connect()

	return connector

def test_application_connector_instantiates(connector):
	assert isinstance(connector, ApplicationConnector), "Must be an instance of ApplicationConnector"

@pytest.mark.integration
def test_connector_finds_process(connector_connected):
	assert isinstance(connector_connected.app, Application), "Connector must connect to pywinauto app."


@pytest.mark.integration
def test_connector_finds_process(connector_connected):
	connector_connected.get_window()

	assert isinstance(connector_connected.window, WindowSpecification), "Connector must locate DaVinci Resolve window."

@pytest.mark.integration
def test_connector_gets_element_list(connector_connected):
	connector_connected.load_elements()

	assert len(connector_connected.elements) > 0, "Connector must find at least one element"

@pytest.mark.integration
def test_connector_gets_element_details(connector_connected):
	first_element = connector_connected.elements[3]

	assert isinstance(first_element['pointer'], UIAWrapper), "Element pointer must be a UIAWrapper type"

	assert 'properties' in first_element, "Element must include identifyable properties"

	assert isinstance(first_element['properties'], dict), "element['properties'] must be a dict."

