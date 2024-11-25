import io
from xml.etree.ElementTree import Element, tostring

import pytest

from docx.image.svg import BASE_PX, Svg


@pytest.fixture
def svg_with_dimensions():
    """Fixture for SVG stream with width and height."""
    root = Element("svg", width="200", height="100")
    return io.BytesIO(tostring(root))


@pytest.fixture
def svg_with_viewbox():
    """Fixture for SVG stream with viewBox but no width and height."""
    root = Element("svg", viewBox="0 0 400 200")
    return io.BytesIO(tostring(root))


@pytest.fixture(
    params=[
        ("0 0 400 200", BASE_PX, BASE_PX // 2),  # Landscape
        ("0 0 200 400", BASE_PX // 2, BASE_PX),  # Portrait
        ("0 0 100 100", BASE_PX, BASE_PX),  # Square
    ]
)
def viewbox_data(request):
    """Fixture for different viewBox test cases as tuples."""
    return request.param


@pytest.fixture(
    params=[
        (b'<svg width="200" height="100"/>', 200, 100),
        (b'<svg viewBox="0 0 400 200"/>', BASE_PX, BASE_PX // 2),
    ]
)
def svg_stream_data(request):
    return request.param


def test_dimensions_from_stream(svg_stream_data):
    stream_data, expected_width, expected_height = svg_stream_data
    stream = io.BytesIO(stream_data)
    width, height = Svg._dimensions_from_stream(stream)
    assert width == expected_width
    assert height == expected_height


def test_calculate_scaled_dimensions(viewbox_data):
    viewbox, expected_width, expected_height = viewbox_data
    width, height = Svg._calculate_scaled_dimensions(viewbox)
    assert width == expected_width
    assert height == expected_height
