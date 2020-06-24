import sys
import logging
import time
import inspect
from typing import Optional, Any

_DEFAULT_LOG_LEVEL = logging.INFO
_LOG_FORMAT = "%(asctime)s.%(msecs)03dZ %(levelname)-8s %(name)s - %(message)s"
_DATE_FORMAT = "%y-%m-%d %H:%M:%S"
_TIME_CONVERTER = time.gmtime

def get_logger(obj: Any, file_handle: Optional[str] = None) -> logging.Logger:
    if isinstance(obj, str):
        return _get_logger(obj, file_handle)
    if inspect.isclass(obj):
        return _get_logger(obj.__name__, file_handle)

class Handlers:
    _handler = None
    _log_format = logging.Formatter(_LOG_FORMAT, datefmt=_DATE_FORMAT)
    _log_format.converter = _TIME_CONVERTER

    @classmethod
    def get_handler(cls) -> logging.Handler:
        if cls._handler is None:
            handler = logging.StreamHandler(stream=sys.stdout)
            handler.setLevel(_DEFAULT_LOG_LEVEL)
            handler.setFormatter(cls._log_format)
            cls._handler = handler
        
        return cls._handler



def _get_logger(name: str, file_handle: Optional[str]):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = Handlers.get_handler()
        logger.addHandler(handler)
    
    return logger