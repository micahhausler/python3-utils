import uuid
from unittest import TestCase

from mock import patch

from python3_utils.decorators import compare_on_attr


with patch('python3_utils.decorators.six') as mock_six:
    mock_six.PY3 = False

    @compare_on_attr()
    class MockModel(object):
        id = None

        def __init__(self, id=None):
            self.id = id or uuid.uuid4()

    class CompareTests(TestCase):

        def test_compare_has_attr_py2(self):

            model1 = MockModel(1)
            model2 = MockModel(1)

            self.assertFalse(
                model1 == model2
            )
