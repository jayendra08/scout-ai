from typing import List, Dict, Any, Optional
from app.preprocessing import load_and_preprocess_data

_, _, _, interview_df = load_and_preprocess_data()


def recommend_interview_questions(
    category: Optional[str] = None,
    difficulty: Optional[str] = None,
    top_k: int = 5
) -> List[Dict[str, str]]:
    """
    Fetch software interview questions filtered by optional category or difficulty.
    """
    if interview_df.empty:
        return []

    df_filtered = interview_df.copy()

    if category and "Category" in df_filtered.columns:
        df_filtered = df_filtered[
            df_filtered["Category"].astype(str).str.lower() == category.lower()
        ]

    if difficulty and "Difficulty" in df_filtered.columns:
        df_filtered = df_filtered[
            df_filtered["Difficulty"].astype(str).str.lower() == difficulty.lower()
        ]

    # Fallback to full list if filtered output is empty
    if df_filtered.empty:
        df_filtered = interview_df

    # Limit to top_k rows
    selected = df_filtered.head(top_k)

    questions = []
    for _, row in selected.iterrows():
        questions.append({
            "question": str(row.get("Question", "")),
            "answer": str(row.get("Answer", "")),
            "category": str(row.get("Category", "")),
            "difficulty": str(row.get("Difficulty", "")),
        })

    return questions
