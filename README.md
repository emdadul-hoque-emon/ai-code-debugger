# AI Code Debugger

A Streamlit app that analyzes coding-related screenshots and generates either:

- **Hints** to guide debugging
- **Solutions with code** for likely fixes

The app uses the **Google Gemini API** (`gemini-3-flash-preview`) to understand uploaded images and return markdown-formatted output.

## Features

- Upload a coding screenshot (`.jpg`, `.jpeg`, `.png`)
- Choose response type:
  - Hints
  - Solutions with code
- AI-generated, formatted output shown directly in the app
- Basic guardrail for non-coding images (handled by model prompt)

## Tech Stack

- Python
- Streamlit
- Pillow
- Google GenAI SDK
- python-dotenv

## Project Structure

```text
project-2-ai-code-debugger/
|-- main.py             # Streamlit UI
|-- api_call.py         # Gemini API integration
|-- requirements.txt    # Python dependencies
|-- .env                # Local environment variables (not committed)
|-- project-venv/       # Local virtual environment
```

## Prerequisites

- Python 3.10+ (recommended)
- A Google Gemini API key

## Setup

1. Clone the repository

```bash
git clone <your-repo-url>
cd project-2-ai-code-debugger
```

2. Create and activate a virtual environment

### Windows (PowerShell)

```powershell
python -m venv project-venv
.\project-venv\Scripts\Activate.ps1
```

### Windows (Git Bash)

```bash
python -m venv project-venv
source project-venv/Scripts/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

## Run the App

```bash
streamlit run main.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## How to Use

1. Upload an image containing coding-related content (error message, code screenshot, stack trace, etc.)
2. Select either:
   - **Hints**
   - **Solutions with code**
3. Click **Solution with code** button
4. Review the AI-generated markdown output

## Environment Variables

- `GEMINI_API_KEY`: Required. API key used by `google-genai` client.

## Troubleshooting

### App starts but generation fails

- Verify `.env` exists in the project root.
- Confirm `GEMINI_API_KEY` is valid.
- Ensure internet access is available.

### "Please select a type and upload an image"

- Make sure both an image is uploaded and an option is selected before clicking the button.

### Virtual environment activation fails in Git Bash

Use:

```bash
source project-venv/Scripts/activate
```

(or recreate the venv if it was created with a different Python installation).

## Notes

- The app behavior and output quality depend on model response.
- Current model set in code: `gemini-3-flash-preview`.
- Keep `.env` out of version control.

## License

No license file is currently included. Add one (for example, MIT) if you plan to distribute this project.
