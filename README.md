# **Company Analyzer Helper 📊**  
An AI-powered tool to analyze competitors, uncover their strengths and weaknesses, and generate actionable business insights.

---

## **Overview**  
The **Company Analyzer Helper** is an interactive web application designed to assist businesses in performing competitive analysis effortlessly. Built with advanced neural search and generative AI, the app identifies competitors, analyzes their strengths and weaknesses, and provides concise, actionable reports for strategic decision-making.

---

## **Features**  
- **Competitor Identification**: Automatically find similar companies based on a provided company URL.  
- **Actionable Insights**: AI-generated summaries of competitors' strengths, weaknesses, and areas of improvement.  
- **Interactive Reports**: Easy-to-read, professional-grade business intelligence reports.  
- **Custom Neural Search**: Advanced competitor identification using Exa AI's neural search capabilities.  
- **AI-Driven Content**: Leverages Google Gemini generative AI for insightful summaries.

---

## **Tech Stack**  
- **Frontend**: [Streamlit](https://streamlit.io) for a modern, responsive UI.  
- **AI Models**: Google Gemini (Generative AI) for content generation.  
- **Search Engine**: Exa AI for neural search and competitor discovery.  
- **Environment Management**: dotenv for secure API key handling.  
- **Programming Language**: Python.  

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher installed on your local machine.
- API keys for:
  - **Google Gemini** ([Get API Key](https://aistudio.google.com/app/apikey))  
  - **Exa AI** ([Get API Key](https://exa.ai/))  

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/Company-Analyzer-Helper.git
   cd Company-Analyzer-Helper
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up API keys:
   - Create a `.streamlit/secrets.toml` file in the project directory:
     ```toml
     [EXA]
     EXA_API_KEY = "your_exa_api_key"
     
     [GOOGLE]
     GOOGLE_API_KEY = "your_google_api_key"
     ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

6. Open the app in your browser at `http://localhost:8501`.

---

## **How to Use**

1. **Enter a Company URL**:
   - Input the URL of the company you want to analyze (e.g., `https://example.com`).
2. **Discover Competitors**:
   - The app identifies up to 10 similar companies using Exa AI's neural search.
3. **Select a Competitor**:
   - Choose a competitor from the list for in-depth analysis.
4. **Generate Insights**:
   - View AI-generated reports summarizing the competitor's strengths, weaknesses, and recommendations for improvement.

---
