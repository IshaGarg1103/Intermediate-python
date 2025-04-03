import logging
logging.basicConfig(level=logging.INFO)
logging.info("hello ! the program has started.")

logging.basicConfig(level=logging.DEBUG, force=True)
logging.debug("this is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("this is a critical message")
#logging.basicConfig() only works once, the first call sets up the logging system with info as the minimum level
#hence force call is done to call the basicConfig
