import logging
import pandas as pd
import numpy as np

logger = logging.getLogger("DataCleaner")

class DataCleaner:
    """
    DataCleaner processes raw student data, addressing missing values,
    clipping out-of-range columns, mapping categories, and handling outliers via IQR.
    """
    def __init__(self):
        self.stats = {}

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Cleans the input DataFrame and returns a clean, copy of the DataFrame.
        """
        logger.info("Initializing data cleaning process.")
        cleaned_df = df.copy()
        
        # Reset stats report
        self.stats = {
            "initial_rows": len(df),
            "imputed_study_hours": 0,
            "imputed_final_score": 0,
            "clipped_attendance": 0,
            "age_outliers_handled": 0,
            "categorical_mapped": 0
        }

        # 1. Numerical Median Imputation
        cleaned_df = self._impute_missing_values(cleaned_df)

        # 2. Categorical Mapping
        cleaned_df = self._map_categorical_variables(cleaned_df)

        # 3. Attendance Rate Clipping
        cleaned_df = self._clip_attendance_rate(cleaned_df)

        # 4. Age Outliers via IQR
        cleaned_df = self._handle_age_outliers(cleaned_df)

        self.stats["final_rows"] = len(cleaned_df)
        logger.info(f"Cleaning complete. Summary of changes: {self.stats}")
        return cleaned_df

    def _impute_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Imputes missing values in Study_Hours and Final_Score using their median values.
        """
        # Study_Hours
        missing_study = df["Study_Hours"].isna().sum()
        if missing_study > 0:
            median_hours = df["Study_Hours"].median()
            df["Study_Hours"] = df["Study_Hours"].fillna(median_hours)
            self.stats["imputed_study_hours"] = int(missing_study)
            logger.info(f"Imputed {missing_study} missing values in Study_Hours with median: {median_hours}")

        # Final_Score
        missing_score = df["Final_Score"].isna().sum()
        if missing_score > 0:
            median_score = df["Final_Score"].median()
            df["Final_Score"] = df["Final_Score"].fillna(median_score)
            self.stats["imputed_final_score"] = int(missing_score)
            logger.info(f"Imputed {missing_score} missing values in Final_Score with median: {median_score}")

        return df

    def _map_categorical_variables(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Maps Internet_Access ('Yes' -> 1, 'No' -> 0).
        """
        if "Internet_Access" in df.columns:
            # Check unique values before mapping
            initial_cats = df["Internet_Access"].unique()
            logger.info(f"Categorical values in Internet_Access: {initial_cats}")
            
            # Binary mapping
            mapping = {"Yes": 1, "No": 0}
            df["Internet_Access"] = df["Internet_Access"].map(mapping)
            
            self.stats["categorical_mapped"] = int(df["Internet_Access"].notna().sum())
            logger.info("Mapped 'Internet_Access' column: 'Yes' -> 1, 'No' -> 0")
        else:
            logger.warning("Internet_Access column not found in dataset.")
            
        return df

    def _clip_attendance_rate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Clips Attendance_Rate to the valid range [0.0, 100.0].
        """
        if "Attendance_Rate" in df.columns:
            out_of_bounds_mask = (df["Attendance_Rate"] < 0.0) | (df["Attendance_Rate"] > 100.0)
            num_out_of_bounds = out_of_bounds_mask.sum()
            
            if num_out_of_bounds > 0:
                logger.info(f"Found {num_out_of_bounds} attendance rates outside logical limits [0, 100]")
                # Clip values
                df["Attendance_Rate"] = df["Attendance_Rate"].clip(lower=0.0, upper=100.0)
                self.stats["clipped_attendance"] = int(num_out_of_bounds)
                logger.info("Clipped Attendance_Rate column to [0.0, 100.0]")
        else:
            logger.warning("Attendance_Rate column not found in dataset.")
            
        return df

    def _handle_age_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Detects Age outliers using the IQR (Interquartile Range) method
        and replaces them with the median Age of the dataset.
        """
        if "Age" in df.columns:
            q1 = df["Age"].quantile(0.25)
            q3 = df["Age"].quantile(0.75)
            iqr = q3 - q1
            
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            
            logger.info(f"IQR Age boundaries: Lower={lower_bound}, Upper={upper_bound} (IQR={iqr})")
            
            outliers_mask = (df["Age"] < lower_bound) | (df["Age"] > upper_bound)
            num_outliers = outliers_mask.sum()
            
            if num_outliers > 0:
                median_age = df["Age"].median()
                logger.info(f"Found {num_outliers} Age outliers. Replacing with median: {median_age}")
                # Replace with median
                df.loc[outliers_mask, "Age"] = median_age
                self.stats["age_outliers_handled"] = int(num_outliers)
        else:
            logger.warning("Age column not found in dataset.")
            
        return df

    def get_cleaning_summary(self) -> dict:
        """
        Returns the stats dictionary summarizing modifications.
        """
        return self.stats
