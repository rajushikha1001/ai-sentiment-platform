import logging
import sys

# Create logger
logger = logging.getLogger("ai-platform")
logger.setLevel(logging.INFO)

# Output → console
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(message)s",
    "%Y-%m-%d %H:%M:%S"
)
handler.setFormatter(formatter)

logger.addHandler(handler)
