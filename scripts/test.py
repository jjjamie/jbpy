import logging
import jbpython.log_util as log_util

_log = logging.getLogger(__name__)

log_util.configure_logging()


def main():
    print("Hello from jbpython!")
    _log.info("Hello from jbpython!")


if __name__ == "__main__":
    main()
