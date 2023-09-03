import pytest
from ui_interactor.element_map import ElementMap, ElementNotFoundException
from ui_interactor.element import Element

mock_element_list = [
	{
		"properties" : {"automation_id": 'element_id_1'},
		"pointer"    : 'element_pointer_1'
	},
	{
		"properties" : {"automation_id": 'element_id_2'},
		"pointer"    : 'element_pointer_2'
	}
]


@pytest.fixture
def map_instance():
	return ElementMap(
		element_list = mock_element_list,
	)


def test_element_map_can_instanciate(map_instance):
	assert isinstance(map_instance, ElementMap), "Test instance should be an instance of ElementMap"

def test_finds_correct_pointer_for_automation_id(map_instance):
	automation_id = 'element_id_1'
	expected_pointer = 'element_pointer_1'

	element_details = map_instance.lookup(automation_id=automation_id)

	assert element_details['pointer'] == expected_pointer, "Lookup by automation ID should find the right info."

def test_exception_if_pointer_not_found_for_automation_id(map_instance):
	with pytest.raises(ElementNotFoundException) as excinfo:
		map_instance.lookup(automation_id="something that won't exist in the map")
		
	assert "Could not find" in str(excinfo.value)

def test_element_map_provides_element_retriever_function(map_instance):
	element_abstraction = Element(
		automation_id = 'element_id_1',
		retriever_function = map_instance.make_retriever_function()
	)

	pointer = element_abstraction.get_pointer()

	assert pointer == 'element_pointer_1', 'ElementMap Retriever function should work with Element abstraction.'