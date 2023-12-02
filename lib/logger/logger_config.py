import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s')

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

logger = _logger
