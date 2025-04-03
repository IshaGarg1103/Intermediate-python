import logging
logging.basicConfig(
    filename="my_program.log",
    level=logging.INFO
)
logging.info("The program is running.")
logging.error("Oops, something broke!")