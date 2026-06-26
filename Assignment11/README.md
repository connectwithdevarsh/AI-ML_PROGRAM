# Assignment 11: AI Text Summarizer

An interactive AI-powered command-line summarization tool built using the Cohere API.

## Python Version
- Python 3.x (tested on Python 3.9+)

## Libraries Used
- cohere
- python-dotenv

## How to Get Cohere API Key
1. Go to the [Cohere Dashboard](https://dashboard.cohere.com/).
2. Sign up or log in.
3. Go to the "API Keys" section.
4. Create a new Trial or Production API Key.
5. Copy the generated key.

## How to Create .env
1. Duplicate the `.env.example` file and rename it to `.env` in the root folder of Assignment11.
2. Open `.env` and paste your Cohere API key:
   ```env
   COHERE_API_KEY=your_actual_api_key_here
   ```

## How to Install
Run the following command to install the required libraries:
```bash
pip install -r requirements.txt
```

## How to Run
Run the tool using:
```bash
python main.py
```
Paste your text, hit enter twice, select the summary size and format options, and see the results!

## Project Files
- **main.py**: The main interactive summarizer application script.
- **requirements.txt**: Project dependency configuration.
- **.env.example**: Example template for environment variables configuration.
