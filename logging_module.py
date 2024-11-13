import logging

logger = logging.getLogger()

print(logger.name, logger.hasHandlers())
logger.debug("Debugging this line")
logger.info("This is informational")
logger.warning("This is warning") # This is warning
logger.error("This is error") # This is error
logger.critical("This is critical") # This is critical