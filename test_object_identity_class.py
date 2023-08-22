import pytest
from object_identity import ObjectIdentity

class TestObjectIdentity:

    @pytest.fixture
    def object_a(self):
        return ObjectIdentity('Hello')

    @pytest.fixture
    def object_b(self):
        return ObjectIdentity('Hello')

    def test_initial_text(self, object_a):
        assert object_a.text == 'Hello'

    def test_change_text(self, object_a):
        object_a.text = 'New Text'
        assert object_a.text == 'New Text'

    def test_equal_objects(self, object_a, object_b):
        assert object_a == object_b

    def test_equal_objects_with_strings(self, object_a):
        assert object_a == 'Hello'

    def test_not_equal_objects(self, object_a):
        assert object_a != 'Not Hello'

    def test_not_equal_objects_different_instances(self, object_a):
        other_object = ObjectIdentity('Not Hello')
        assert object_a != other_object