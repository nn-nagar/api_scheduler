import logger


def test_logger():
    log = logger.get_logger()
    assert log is not None
