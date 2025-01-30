import subprocess
import logger
import config

log = logger.get_logger()


def call_api(timestamp):
    """
    Calls the API and logs the response.
    """
    try:
        log.info(f"Calling API at {config.API_URL} for timestamp {timestamp}")

        # Execute the API call using subprocess (mimics curl)
        result = subprocess.run(["curl", "-s", config.API_URL], capture_output=True, text=True)

        if result.returncode == 0:
            log.info(f"{timestamp}: API Response - {result.stdout.strip()}")
        else:
            log.error(f"{timestamp}: API Call Failed - {result.stderr.strip()}")

    except Exception as e:
        log.error(f"{timestamp}: API Call Error - {str(e)}")
