import logging


def get_logger():
    """
    Configures and returns a logger.
    """
    logging.basicConfig(
        filename="api_scheduler.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("APIScheduler")
