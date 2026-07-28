import ast
from pathlib import Path
from typing import List

# Base Paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

RESUME_DATA_PATH = DATA_DIR / "resume_data.csv"
JOB_DATA_PATH = DATA_DIR / "all_job_post.csv"
JOB_DES_PATH = DATA_DIR / "job_title_des.csv"
QUESTIONS_PATH = DATA_DIR / "Software Questions.csv"


def parse_skill_string(skill_text: str) -> List[str]:
    """
    Convert skill data into a clean Python list.
    Handles:
    - Python list strings
    - Comma-separated strings
    """

    if not skill_text or str(skill_text).strip() == "" or str(skill_text) == "nan":
        return []

    if isinstance(skill_text, list):
        return [
            str(skill).strip().lower()
            for skill in skill_text
            if str(skill).strip()
        ]

    try:
        parsed = ast.literal_eval(str(skill_text))

        if isinstance(parsed, list):
            return [
                str(skill).strip().lower()
                for skill in parsed
                if str(skill).strip()
            ]

    except Exception:
        pass

    # Fallback for comma-separated skills
    return [
        skill.strip().lower()
        for skill in str(skill_text).split(",")
        if skill.strip()
    ]


def clean_column_names(df):
    """
    Clean dataframe column names:
    - Remove hidden BOM characters
    - Remove extra spaces
    """

    df.columns = (
        df.columns.astype(str)
        .str.replace("\ufeff", "", regex=False)
        .str.strip()
    )

    return df


def combine_text_columns(df, columns):
    """
    Combine multiple dataframe columns into one text column.

    Example:
    job_title + job_description + skills
    becomes:
    "Python Developer Backend API FastAPI MongoDB"
    """

    return (
        df[columns]
        .astype(str)
        .apply(
            lambda row: " ".join(row.values),
            axis=1
        )
    )