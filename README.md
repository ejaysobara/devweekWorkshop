# Parallel and Distributed Computing Assignment

This repository contains a deployable Python web application that visualizes the same matrix multiplication logic as the original assignment.

## Run locally

1. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the app:

   ```bash
   python app.py
   ```

4. Open the browser at `http://localhost:5000`

## Files

- `app.py` — Flask application
- `templates/index.html` — HTML template for the visualization
- `static/style.css` — page styles
- `requirements.txt` — Python dependencies

## Notes

- The matrix multiplication logic is preserved in Python.
- The page displays Matrix A, Matrix B, and the computed result matrix.
