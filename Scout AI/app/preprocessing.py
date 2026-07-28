from typing import Tuple

import pandas as pd
from app.utils import (
    RESUME_DATA_PATH,
    JOB_DATA_PATH,
    JOB_DES_PATH,
    QUESTIONS_PATH,
    combine_text_columns,
    parse_skill_string,
    clean_column_names,
)


def load_and_preprocess_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load data from CSV files and apply preprocessing routines:
    1. Clean column names (strip spaces, remove BOM).
    2. Fill NaN values.
    3. Construct combined text representations (`resume_text` and `job_text`).
    4. Parse skill columns into Python lists.
    """
    # Load Resumes
    if RESUME_DATA_PATH.exists():
        resume_df = pd.read_csv(RESUME_DATA_PATH)
    else:
        resume_df = pd.DataFrame(columns=["career_objective", "skills", "responsibilities", "job_position_name"])
    
    resume_df = clean_column_names(resume_df).fillna("")
    resume_df["resume_text"] = combine_text_columns(
        resume_df,
        ["career_objective", "skills", "responsibilities", "job_position_name"],
    )
    resume_df["parsed_skills"] = resume_df["skills"].apply(parse_skill_string)

    # Load Job Posts
    if JOB_DATA_PATH.exists():
        skills_df = pd.read_csv(JOB_DATA_PATH)
    else:
        skills_df = pd.DataFrame(columns=["job_title", "job_description", "job_skill_set", "category"])
    
    skills_df = clean_column_names(skills_df).fillna("")
    skills_df["parsed_skills"] = skills_df["job_skill_set"].apply(parse_skill_string)
    skills_df["job_text"] = combine_text_columns(
        skills_df,
        ["job_title", "job_description", "job_skill_set"],
    )

    # Load Job Descriptions (supplementary)
    if JOB_DES_PATH.exists():
        job_des_df = pd.read_csv(JOB_DES_PATH)
        job_des_df = clean_column_names(job_des_df).fillna("")
    else:
        job_des_df = pd.DataFrame()

    # Load Software Interview Questions
    if QUESTIONS_PATH.exists():
        interview_df = pd.read_csv(QUESTIONS_PATH)
        interview_df = clean_column_names(interview_df).fillna("")
    else:
        interview_df = pd.DataFrame(columns=["Question", "Answer", "Category", "Difficulty"])

    return resume_df, skills_df, job_des_df, interview_df
