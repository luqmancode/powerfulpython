import logging

logging.basicConfig(level=logging.INFO, filename="log.txt", filemode="a", format="%(pathname)s %(funcName)s %(lineno)d %(asctime)s Log level: %(levelname)s, msg: %(message)s") # Always to be at top before any new log message used and only one instance
logging.basicConfig(filename="log.txt", filemode="w") # not working as second instance

logging.warning("Look Out!") # WARNING:root:Look Out!
logging.error("Here is the error!") # ERROR:root:Here is the error!

logging.debug("Small details. Useful for debugging") # No results in log
logging.info("This is informative") # No results in log
logging.warning("This is a warning message") # WARNING:root:This is a warning message
logging.error("Oh no, something went wrong") # ERROR:root:Oh no, something went wrong
logging.critical("We have a big problem") # CRITICAL:root:We have a big problem

# Change the default settings
# logging.basicConfig(level=logging.INFO) Not working when we add here
logging.info("This is informative.")
logging.error("Uh oh. Something went wrong.")


logging.log(logging.DEBUG, "This is small detail, useful for troubleshooting")
logging.log(logging.INFO, "This is informative")
logging.log(logging.WARNING, "This is a warning message")
logging.log(logging.ERROR, "Oh, something went wrong")
logging.log(logging.CRITICAL, "We have a big problem")

# To have it in dynamic
def log_results(message, level=logging.INFO):
    logging.log(level, "Results: " + message)

log_results("This is info")
log_results("We have problem in lines of code", logging.CRITICAL)

# log levels by number 10 DEBUG, 20 INFO, 30 WARNING, 40 ERROR, 50 CRITICAL

logging.error("oops")

# default format : %(levelname)s:%(name)s:%(message)s

no_fruits = 14
fruit_name = "oranges"

logging.info("I ate %d of %s during workout", no_fruits, fruit_name)

# format is logging.info("message_format_in_%", *args)
fruit_info = {"counts": 6, "name": "Apple"}
logging.warning("I ate total of %(counts)d %(name)s. Thanks", fruit_info)

logger = logging.getLogger()
print(logger.name) # root
for item in dir(logger):
    print(item() if callable(item) else item)

logger = logging.getLogger()

logger.debug("Debugging this line")
logger.info("This is informational")
logger.warning("This is warning") # This is warning
logger.error("This is error") # This is error
logger.critical("This is critical") # This is critical