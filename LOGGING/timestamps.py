import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt= "%H:%M:%S %y/%m/%d "
)
logging.info("The program is running")
logging.error("Oops, something broke!")

#PLACEHOLDERS 👇
#asctime- timestamp when the log was created 
#levelname - logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
#message - the actual log message text

#format parameter lets you customize log messages with structured details like timestamps.

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
    force=True
)
logging.debug("This won't appear (DEBUG < WARNING).")
logging.info("This won't appear either (INFO < WARNING).")
logging.warning("This will appear (WARNING >= default level).")
logging.error("This will appear (ERROR > WARNING).")
#when the level is not specified in the log, the root logger defaults to WARNING.
