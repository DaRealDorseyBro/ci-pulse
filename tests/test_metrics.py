from ci_pulse import metrics


def test_queue_seconds():
    from datetime import datetime
    create_time = datetime(2024, 1, 1, 12, 0, 0)
    start_time = datetime(2024, 1, 1, 12, 0, 30)
    assert metrics.queue_seconds(create_time, start_time) == 30.0

def test_queue_seconds_negative():
    from datetime import datetime
    create_time = datetime(2024, 1, 1, 12, 0, 30)
    start_time = datetime(2024, 1, 1, 12, 0, 0)
    assert metrics.queue_seconds(create_time, start_time) == -30.0

def test_duration_seconds():
    from datetime import datetime
    start_time = datetime(2024, 1, 1, 12, 0, 0)
    end_time = datetime(2024, 1, 1, 12, 0, 30)
    assert metrics.duration_seconds(start_time, end_time) == 30.0

def test_duration_seconds_negative():
    from datetime import datetime
    start_time = datetime(2024, 1, 1, 12, 0, 30)
    end_time = datetime(2024, 1, 1, 12, 0, 0)
    assert metrics.duration_seconds(start_time, end_time) == -30.0