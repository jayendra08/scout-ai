from typing import List, Dict, Any

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from app.preprocessing import load_and_preprocess_data
from app.embeddings import generate_embeddings, compute_job_embeddings

# Load datasets
resume_df, skills_df, job_des_df, interview_df = load_and_preprocess_data()

# Precompute all job embeddings once
job_embeddings = (
    compute_job_embeddings(skills_df["job_text"].tolist())
    if not skills_df.empty
    else np.array([])
)


def recommend_jobs_with_skill_gap(
    resume_text: str,
    top_k: int = 5
) -> List[Dict[str, Any]]:

    if skills_df.empty or job_embeddings.size == 0:
        return []

    # Generate embedding for uploaded resume
    resume_embedding = generate_embeddings([resume_text])

    if resume_embedding.size == 0:
        return []

    # Compare with all jobs
    similarities = cosine_similarity(
        resume_embedding,
        job_embeddings
    )[0]

    # Top matching jobs
    top_indices = similarities.argsort()[-top_k:][::-1]

    recommendations = []

    for idx in top_indices:

        job_row = skills_df.iloc[idx]

        job_skills = job_row.get("parsed_skills", [])

        # Until PDF skill extraction is added
        matched_skills = []
        missing_skills = job_skills

        score = float(similarities[idx])
        score = round(max(0.0, min(1.0, score)), 4)

        recommendations.append({
            "job_title": str(job_row.get("job_title", "")),
            "category": str(job_row.get("category", "")),
            "match_score": score,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        })

    return recommendations


def get_resume_count():
    return len(resume_df)