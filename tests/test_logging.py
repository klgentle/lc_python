import logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

logging.info("Start print log")
logging.debug("Do something")
logging.warning("Something maybe fail.")
logging.info("Finish")