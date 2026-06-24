import os
import sys
import platform
import logging
from pathlib import Path
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("DataLoader")

class DataLoader:
    """
    DataLoader is responsible for validating file paths, verifying OS-specific details,
    and reading raw CSV files into Pandas DataFrames.
    """
    def __init__(self, data_path: str | Path):
        self.raw_path = Path(data_path)
        self.os_name = platform.system()
        self.platform_name = sys.platform
        logger.info(f"Initialized DataLoader. Detected OS: {self.os_name} (sys.platform: {self.platform_name})")

    def validate_file(self) -> bool:
        """
        Validates that the source path exists, is a file, and is readable.
        """
        logger.info(f"Validating file path: {self.raw_path}")
        
        # Verify if path exists
        if not self.raw_path.exists():
            logger.error(f"Path does not exist: {self.raw_path}")
            return False
            
        # Verify it is a file
        if not self.raw_path.is_file():
            logger.error(f"Path exists but is not a file: {self.raw_path}")
            return False
            
        # OS-specific access check
        if not os.access(self.raw_path, os.R_OK):
            logger.error(f"Read permission denied for file: {self.raw_path}")
            return False

        logger.info(f"File validation succeeded for: {self.raw_path}")
        return True

    def load_data(self) -> pd.DataFrame:
        """
        Loads the data from the CSV file. Performs paths verification before loading.
        """
        # Ensure path format matches local OS conventions
        resolved_path = self.raw_path.resolve()
        logger.info(f"Resolved file path: {resolved_path}")

        if not self.validate_file():
            raise FileNotFoundError(f"Source file {resolved_path} could not be validated or found.")

        try:
            df = pd.read_csv(resolved_path)
            logger.info(f"Successfully loaded dataset of shape {df.shape}")
            return df
        except pd.errors.EmptyDataError:
            logger.error("The CSV file is empty.")
            raise
        except pd.errors.ParserError as e:
            logger.error(f"Failed to parse CSV file: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during data loading: {e}")
            raise
