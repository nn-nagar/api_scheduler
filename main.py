import scheduler
import logger
import test_utils


def main():
    log = logger.get_logger()

    # Load timestamps from a file (timestamps.txt) or generate test timestamps
    timestamps = test_utils.load_timestamps("timestamps.txt")

    if not timestamps:
        log.error("No timestamps found. Please provide a valid timestamps file.")
        return

    log.info(f"Loaded {len(timestamps)} timestamps. Scheduling API calls...")

    # Start scheduling
    scheduler.schedule_api_calls(timestamps)


if __name__ == "__main__":
    main()
