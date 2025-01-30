import scheduler


def test_schedule_api_calls():
    timestamps = ["12:00:00", "12:00:01", "12:00:02"]
    assert scheduler.schedule_api_calls(timestamps) is None  # Function should execute without error
