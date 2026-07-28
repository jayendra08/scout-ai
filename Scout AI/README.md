
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
