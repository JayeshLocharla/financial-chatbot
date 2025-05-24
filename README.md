# 🧠 Financial Chatbot (Flask)

This project was created as part of the **BCG GenAI Job Simulation**, designed to introduce participants to the intersection of financial analysis and AI-driven applications in a consulting context. The simulation places you in the role of a junior data scientist at Boston Consulting Group (BCG), where you build tools to extract, analyze, and interact with financial data using generative AI techniques.

---

## 💡 Features

- Responds to key financial queries:
  - Total Revenue
  - Net Income
  - Total Assets
  - Total Liabilities
  - Cash Flow from Operations
- Clean, responsive UI using Tailwind CSS
- Lightweight and beginner-friendly

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/financial-chatbot.git
cd financial-chatbot
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Example Queries

- What is Apple's net income?
- Tell me Tesla's total revenue.
- Microsoft total assets?

## ⚠️ Limitations

- Only responds to exact company + keyword combinations
- Static, hardcoded data (no database or dynamic scraping)
