# Day 11 Internship - Multi-LLM API Integration

## Project Name
Day 11 Multi-LLM API Integration

## Python Version
Python 3.x

## Libraries Used
- `groq`
- `google-genai`
- `openai`
- `python-dotenv`

## Files Included
- `main.py` - Main Python script connecting to the APIs.
- `platforms.txt` - List of five AI platforms and their models.
- `.env.example` - Example file for environment variables.
- `requirements.txt` - Required packages.

## How to Run

### Step 1: Install requirements
```bash
pip install -r requirements.txt
```

### Step 2: Create .env
Copy the `.env.example` file and rename it to `.env`:
```bash
cp .env.example .env
```

### Step 3: Add API Keys
Open the `.env` file and replace the placeholders with your actual API keys:
```env
GROQ_API_KEY=your_actual_groq_key
GEMINI_API_KEY=your_actual_gemini_key
OPENAI_API_KEY=your_actual_openai_key
```

### Step 4: Run
Execute the script:
```bash
python main.py
```
