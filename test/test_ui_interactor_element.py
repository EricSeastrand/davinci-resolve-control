import pytest
from ui_interactor.element import Element

id_to_test_with = 'a.totally.real.id'

def retriever_function(element_instance):
	return { "pointer": "I'm a reference to something IRL", "properties": {'foo': 'bar'}}

@pytest.fixture
def element_instance():
	return Element(
		automation_id = id_to_test_with,
		retriever_function = retriever_function
	)

def test_element_instantiates(element_instance):
	assert element_instance, "Failed to instanciate"

def test_element_adopts_automation_id(element_instance):
	assert element_instance.automation_id==id_to_test_with, "Element didn't get the automation_id"

def test_element_accepts_reference_retriever(element_instance):
	assert element_instance.retriever_function == retriever_function, "Element didn't get the retriever_function"

def test_element_gets_pointer_from_retriever(element_instance):
	expected_reference = retriever_function(element_instance)

	element_instance.get_pointer() == expected_reference

def test_element_caches_pointer(element_instance):
	fake_pointer = {"pointer": "A pointer, if this was real", "properties": {'foo': 'bar'}}
	attempted_retrievals = 0
	def retriever_function(_unused):
		nonlocal attempted_retrievals, fake_pointer
		attempted_retrievals = attempted_retrievals +1
		return fake_pointer

	element_instance.retriever_function = retriever_function

	retrieved_pointer = element_instance.get_pointer()
	assert retrieved_pointer == fake_pointer['pointer'], "Element didn't get our fake pointer"

	retrieved_pointer = element_instance.get_pointer()
	assert retrieved_pointer == fake_pointer['pointer'], "Element didn't return our fake pointer the second time around"

	assert attempted_retrievals == 1, "Element should have called retriever function exactly 1 time."