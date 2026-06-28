# Enterprise Analytics & AI Assistant Portal

## Python Version
Python 3.10+

## Libraries
- streamlit
- streamlit-option-menu
- pandas
- plotly
- groq
- python-dotenv

## How To Run

### Step 1: Install requirements
Run the following command to install all required libraries:
```bash
pip install -r requirements.txt
```

### Step 2: Create .env file
Create a `.env` file in the project directory (use `.env.example` as a reference).

### Step 3: Add GROQ_API_KEY
Open the `.env` file and add your Groq API key:
```env
GROQ_API_KEY=your_api_key_here
```

### Step 4: Run the application
Run the Streamlit application using:
```bash
streamlit run app.py
```
