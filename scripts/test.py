#!python3

import logging
import jbpy.log_util as log_util

_log = logging.getLogger(__name__)

log_util.configure_logging()


def main():
    print("Hello from jbpy!")
    _log.info("Hello from jbpy!")


if __name__ == "__main__":
    main()
