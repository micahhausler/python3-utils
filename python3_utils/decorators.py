import inspect
import six


class compare_on_attr(object):
    """
    A decorator for comparing class attributes. By default, the decorator
    searches for an 'id' attribute on your class, but other attributes can be
    specified.

    Usage:

    .. code-block:: python

        @compare_on_attr()
        class MyModel(object):
            id = None
            def __init__(self, id):
                self.id = id

        >>> m1 = MyModel(1)
        >>> m2 = MyModel(2)
        >>> m2 > m1
        True

        # or

        @compare_on_attr(attr='count')
        class MyClass(object):
            count = None

    """
    attr = 'id'

    def __init__(self, attr='id'):
        self.attr = attr

    def __call__(self, func):
        if inspect.isclass(func):
            return self.decorate_class(func)

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def decorate_class(self, cls):
        if not hasattr(cls, self.attr):
            return

        if six.PY3:
            def lt(this, other):
                return getattr(this, self.attr) < getattr(other, self.attr)
            cls.__lt__ = lt

            def gt(this, other):
                return getattr(this, self.attr) > getattr(other, self.attr)
            cls.__gt__ = gt

            def eq(this, other):
                return getattr(this, self.attr) == getattr(other, self.attr)
            cls.__eq__ = eq

            def le(this, other):
                return getattr(this, self.attr) <= getattr(other, self.attr)
            cls.__le__ = le

            def ge(this, other):
                return getattr(this, self.attr) >= getattr(other, self.attr)
            cls.__ge__ = ge

            def ne(this, other):
                return getattr(this, self.attr) != getattr(other, self.attr)
            cls.__ne__ = ne
        return cls
