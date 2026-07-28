# Scout AI

Scout AI is a lightweight full-stack resume analyzer built for portfolio use. It pairs a FastAPI backend with a simple HTML/CSS/JavaScript frontend to match resumes against job postings and surface relevant interview questions.

## Project Overview

The application uses preloaded CSV datasets, SentenceTransformers embeddings, and cosine similarity to recommend jobs for a selected resume index. It also returns skill gaps and interview questions so the user can review both fit and preparation needs in one place.

## Features

- Semantic job matching with SentenceTransformers.
- Skill-gap analysis showing matched and missing skills.
- Interview question suggestions with hidden answers and expand/collapse controls.
- FastAPI endpoints with zero database or authentication setup.
- Responsive dark UI built with vanilla HTML, CSS, and JavaScript.

## Tech Stack

- Backend: FastAPI, Uvicorn, Pandas, NumPy, SentenceTransformers, Scikit-learn, Pydantic.
- Frontend: HTML, CSS, Vanilla JavaScript, Fetch API.

## Folder Structure

```
Scout AI/
├── app/
│   ├── main.py
│   ├── preprocessing.py
│   ├── embeddings.py
│   ├── recommender.py
│   ├── interview.py
│   └── utils.py
├── data/
│   ├── resume_data.csv
│   ├── all_job_post.csv
│   ├── job_title_des.csv
│   └── Software Questions.csv
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── requirements.txt
└── README.md
```

## Installation

1. Create and activate a virtual environment if you want an isolated setup.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

Start the API from the project root:

```bash
uvicorn app.main:app --reload --port 8000
```

Open the application at `http://127.0.0.1:8000/ui`.

### API Endpoints

- `GET /` returns `Scout AI API Running`.
- `POST /analyze` accepts:

```json
{
    "resume_index": 0
}
```

and returns recommendations plus interview questions.

## Screenshots

Placeholder for screenshots.

## Future Improvements

- Resume file upload support.
- Better filtering and sorting controls in the UI.
- Export of analysis results to JSON or PDF.
- Additional datasets for broader role coverage.

## License

Open-source for learning and portfolio use.
