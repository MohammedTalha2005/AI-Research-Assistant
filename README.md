# NEXUS - Multi-Agent Research System

NEXUS is a modern, Flask-based research assistant that orchestrates a pipeline of specialized AI agents to gather, analyze, and synthesize information on any given topic. Powered by the Gemini 2.5 Flash model, NEXUS leverages real-time Google Search to provide up-to-date insights beyond its training data.

![NEXUS UI](https://raw.githubusercontent.com/MohammedTalha2005/AI-Research-Assistant/main/screenshot.png) (Replace with an actual screenshot if available)

## 🚀 Features

- **Multi-Agent Pipeline**: Specialized agents for:
  - 🔎 **Research**: Gathers facts using Google Search.
  - 🧠 **Analysis**: Synthesizes and reasons through evidence.
  - ✍️ **Writer**: Drafts a comprehensive structured report.
  - ⚖️ **Chart**: Visualises data.
- **Real-Time Data**: Bypasses knowledge cutoffs with live search tools.
- **Glassmorphic UI**: High-fidelity dark-themed interface with progress visualization.
- **Export Ready**: Save your research reports as PDF for easy sharing.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **LLM**: Google Gemini 2.5 Flash via Generative Language API
- **Frontend**: Vanilla HTML/CSS/JS with Chart.js and JSPDF

## ⚙️ Setup Instructions

### 1. Prerequisites

- Python 3.8+
- A Google Gemini API Key ([Get one here](https://aistudio.google.com/app/apikey))

### 2. Clone the Repository

```bash
git clone https://github.com/MohammedTalha2005/AI-Research-Assistant.git
cd AI-Research-Assistant
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run the Application

You can start the server using the provided batch script:

```bash
run.bat
```

Or manually with Python:

```bash
python app.py
```

Access the UI at `http://localhost:5000`

## 📄 License

This project is licensed under the MIT License.
