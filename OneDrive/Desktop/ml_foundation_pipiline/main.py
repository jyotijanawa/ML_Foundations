import sys
import logging
from pathlib import Path
from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.statistics_engine import StatisticsEngine

# Set up logging for main execution
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("PipelineRunner")

def main():
    logger.info("Starting ML Foundations Data Processing and Analysis Pipeline.")
    
    # 1. Paths Setup
    workspace_dir = Path(__file__).resolve().parent
    raw_data_path = workspace_dir / "data" / "raw_student_data.csv"
    cleaned_data_path = workspace_dir / "data" / "cleaned_student_data.csv"
    report_output_path = workspace_dir / "data" / "data_analysis_report.txt"

    # Ensure output data folder exists
    raw_data_path.parent.mkdir(parents=True, exist_ok=True)

    # 2. Data Loading Phase
    loader = DataLoader(raw_data_path)
    try:
        raw_df = loader.load_data()
    except Exception as e:
        logger.critical(f"Pipeline failed at loading phase: {e}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("                    RAW DATA PREVIEW                     ")
    print("=" * 60)
    print(raw_df.head(10))
    print(f"\nTotal Records: {len(raw_df)}")
    print("-" * 60)

    # 3. Data Cleaning Phase
    cleaner = DataCleaner()
    logger.info("Running DataCleaner on raw dataset...")
    cleaned_df = cleaner.clean(raw_df)

    print("\n" + "=" * 60)
    print("                   CLEANED DATA PREVIEW                  ")
    print("=" * 60)
    print(cleaned_df.head(10))
    print(f"\nTotal Records: {len(cleaned_df)}")
    print("-" * 60)

    # Print summary of cleaned anomalies
    cleaning_summary = cleaner.get_cleaning_summary()
    print("\nCleaning Operations Report:")
    print(f"  - Missing Study_Hours imputed: {cleaning_summary['imputed_study_hours']}")
    print(f"  - Missing Final_Score imputed: {cleaning_summary['imputed_final_score']}")
    print(f"  - Out-of-bounds Attendance Rates clipped: {cleaning_summary['clipped_attendance']}")
    print(f"  - Extreme Age outliers handled (IQR): {cleaning_summary['age_outliers_handled']}")
    print(f"  - Categorical variables mapped (Internet_Access): {cleaning_summary['categorical_mapped']}")
    print("=" * 60)

    # Save Cleaned Dataset
    try:
        cleaned_df.to_csv(cleaned_data_path, index=False)
        logger.info(f"Saved cleaned dataset to: {cleaned_data_path}")
    except Exception as e:
        logger.error(f"Failed to save cleaned dataset: {e}")

    # 4. Statistical Analysis Phase
    stats_engine = StatisticsEngine()
    logger.info("Generating statistical report from cleaned dataset...")
    report_content = stats_engine.generate_report(cleaned_df)

    # Display Report in Terminal
    print("\n" + report_content)

    # Save Statistical Report
    try:
        with open(report_output_path, "w") as f:
            f.write(report_content)
        logger.info(f"Saved analysis report to: {report_output_path}")
    except Exception as e:
        logger.error(f"Failed to save statistical report: {e}")

    logger.info("ML Foundations pipeline execution successfully completed.")

if __name__ == "__main__":
    main()
