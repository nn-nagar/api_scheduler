import threading
import time
import datetime
import api_client
import logger

log = logger.get_logger()


def schedule_api_calls(timestamps):
    """
    Schedule API calls based on provided timestamps.
    """
    grouped_timestamps = {}

    # Group timestamps by second
    for ts in timestamps:
        grouped_timestamps.setdefault(ts, []).append(ts)

    current_time = datetime.datetime.now().replace(microsecond=0)
    for ts, calls in grouped_timestamps.items():
        # Convert timestamp to datetime
        call_time = datetime.datetime.combine(current_time.date(), datetime.datetime.strptime(ts, "%H:%M:%S").time())

        # If the timestamp is in the past, schedule it for tomorrow
        if call_time < current_time:
            call_time += datetime.timedelta(days=1)

        delay = (call_time - current_time).total_seconds()
        log.info(f"Scheduling {len(calls)} API calls at {call_time} (in {delay} seconds)")

        # Schedule API calls with threading for concurrent execution
        threading.Timer(delay, execute_api_calls, args=[calls]).start()


def execute_api_calls(timestamps):
    """
    Execute API calls concurrently for all timestamps that match the same second.
    """
    threads = []
    for ts in timestamps:
        thread = threading.Thread(target=api_client.call_api, args=(ts,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
