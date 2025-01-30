import api_client


def test_call_api():
    assert api_client.call_api("12:00:00") is None  # Function should execute without error
