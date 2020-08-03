class ElementError(Exception):
    """Base class for all non-trivial errors raised by `element`."""

class MultiMatchError(ElementError):
    """Error when multiple elements meet the desired criteria."""
