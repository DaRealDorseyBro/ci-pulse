from datetime import datetime


def queue_seconds(create_time: datetime, start_time: datetime) -> float:
    return (start_time - create_time).total_seconds()

def duration_seconds(start_time: datetime, end_time: datetime) -> float:
    return (end_time - start_time).total_seconds()