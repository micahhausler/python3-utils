import uuid
from unittest import TestCase, skipIf

import six

from python3_utils.decorators import compare_on_attr


class MockObject(object):
    id = None

    def __init__(self, id=None):
        self.id = id or uuid.uuid4()


@compare_on_attr()
class MockModel(object):
    id = None

    def __init__(self, id=None):
        self.id = id or uuid.uuid4()


@compare_on_attr(attr='count')
class MockModelCount(object):
    count = None

    def __init__(self, count=None):
        self.count = count


@skipIf(six.PY2, 'Only run on PY3')
class CompareTests(TestCase):

    def setUp(self):
        self.model1 = MockModel(1)
        self.model2 = MockModel(2)

        super(CompareTests, self).setUp()

    def test_lt(self):
        self.assertTrue(
            self.model1 < self.model2
        )

    def test_gt(self):
        self.assertTrue(
            self.model2 > self.model1
        )

    def test_eq(self):
        self.assertTrue(
            self.model1 == MockModel(1)
        )

    def test_le(self):
        self.assertTrue(
            self.model1 <= MockModel(1)
        )

        self.assertTrue(
            self.model1 <= self.model2
        )

    def test_ge(self):
        self.assertTrue(
            self.model2 >= self.model1
        )
        self.assertTrue(
            self.model2 >= MockModel(2)
        )

    def test_ne(self):
        self.assertTrue(
            self.model2 != self.model1
        )

    def test_different_attr(self):
        self.assertTrue(
            MockModelCount(2) >= MockModelCount(1)
        )

    def test_not_decorating_class(self):
        @compare_on_attr(attr='count')
        def myFunc(one):
            return one

        self.assertFalse(
            hasattr(myFunc, 'count')
        )
