from pink_morsel_app import app


def test_header(dash_duo):
    expected_header = "Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?"
    dash_duo.start_server(app)
    assert dash_duo.find_element('h1').text == expected_header


def test_figure(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#pink-morsel-sale', timeout=10)


def test_region_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region-button', timeout=10)
