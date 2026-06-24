import logging
import pandas as pd

logger = logging.getLogger("StatisticsEngine")

class StatisticsEngine:
    """
    StatisticsEngine provides methods to extract descriptive statistics and
    calculate correlations for ML phase datasets.
    """
    def __init__(self):
        pass

    def extract_descriptive_stats(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Extracts mean, median, and standard deviation (std) for numerical features.
        """
        logger.info("Extracting descriptive statistics.")
        numeric_df = df.select_dtypes(include=["number"])
        
        if numeric_df.empty:
            logger.warning("No numeric columns found in the DataFrame to analyze.")
            return pd.DataFrame()

        # Compute metrics
        means = numeric_df.mean()
        medians = numeric_df.median()
        stds = numeric_df.std()

        # Build summary dataframe
        summary_df = pd.DataFrame({
            "Mean": means,
            "Median": medians,
            "Standard_Deviation": stds
        })
        
        logger.info("Successfully extracted descriptive statistics.")
        return summary_df

    def calculate_correlation(self, df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
        """
        Calculates linear correlation matrix for numeric columns in the DataFrame.
        Supported methods: 'pearson', 'spearman', 'kendall'.
        """
        logger.info(f"Calculating correlation matrix using method: {method}")
        numeric_df = df.select_dtypes(include=["number"])
        
        if numeric_df.empty:
            logger.warning("No numeric columns found to calculate correlation.")
            return pd.DataFrame()

        corr_matrix = numeric_df.corr(method=method)
        logger.info("Successfully calculated correlation matrix.")
        return corr_matrix

    def generate_report(self, df: pd.DataFrame) -> str:
        """
        Generates a human-readable text report of statistics and correlations.
        """
        desc_stats = self.extract_descriptive_stats(df)
        corr_matrix = self.calculate_correlation(df)

        report = []
        report.append("=" * 60)
        report.append("             ML FOUNDATIONS PIPELINE - STATISTICAL REPORT      ")
        report.append("=" * 60)
        report.append("\n1. DESCRIPTIVE STATISTICS")
        report.append("-" * 30)
        report.append(desc_stats.to_string())
        
        report.append("\n2. LINEAR CORRELATION MATRIX (PEARSON)")
        report.append("-" * 38)
        report.append(corr_matrix.to_string())
        report.append("\n" + "=" * 60)
        
        return "\n".join(report)
