import logging
from datetime import datetime
import os

class CustomLogger:

    def __init__(self):
        
        # Create a logs directory if it doesn't exist
        logs_dir = os.path.join(os.getcwd(), "logs") # detecting the current working directory and creating a logs directory within it
        os.makedirs("logs", exist_ok=True) # Create the logs directory if it doesn't exist
        
        # log file path with date and time as its name
        LOG_FILE = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log" # create a log file with date and time as its name
        LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE) # Join the logs directory path with the log file 
        
        # Configure the logging settings
        logging.basicConfig(
            filename=LOG_FILE_PATH,
            format='%(asctime)s - %(levelname)s - %(name)s (line:%(lineno)d) - %(message)s',
            level=logging.INFO, # Set the logging level to INFO, which means it will capture INFO, WARNING, ERROR, and CRITICAL messages
        )

    def get_logger(self, name: __file__):
        return logging.getLogger(os.path.basename(name)) # Get a logger instance with the specified name, which is the base name of the file)
    

    if __name__ == "__main__":
        logger = CustomLogger() # Create an instance of the CustomLogger class
        logger.get_logger(__file__)
        logger.info("custom logger initialized") # Log an INFO level message