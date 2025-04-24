## 📋 Meeting Automater  
**End-to-End NLP Pipeline**  
> Upload a meeting audio file and get a smart summary, and structured action items with owners and due dates — all in one click.

---

### 🚀 Live Demo  
- **Frontend (Streamlit)**: [https://meeting-notes-autometer.streamlit.app/](#)  

---

### 🧠 Overview

This project turns messy meeting audio into structured, actionable text. It combines **speech-to-text**, **text cleanup**, **summarization**, and **LLM-powered task extraction** in one seamless pipeline:

#### 1. **Upload** your meeting audio  
#### 2. **Transcribe** and clean the text  
#### 3. **Summarize** key points using `bart-large-cnn`  
#### 4. **Extract action items** (who does what, by when) via a prompt to **Mistral LLM**  
#### 5. **Download or copy** the result for documentation, follow-up, or delegation

---

### ✅ Features

- **Speech-to-text** using Assembly AI
- **Text cleanup**: filler removal, punctuation restoration, grammar/spell check
- **Summarization** via Hugging Face API (`bart-large-cnn`)
- **Task extraction** using Mistral (`mistralai/Mistral-7B-Instruct-v0.1`)
- Streamlit UI for easy upload & result viewing
- FastAPI backend for extensibility
- Dockerized + GitHub Actions CI/CD for deployment

---

### 🏗️ Architecture

```
Audio Upload (UI)
       ↓
FastAPI: /extract
       ↓
Speech Recognition (Aseembly AI)
       ↓
Text Preprocessing → Punctuation → Spelling Correction
       ↓
Summarization via BART (Hugging Face Inference API)
       ↓
Prompt to Mistral LLM (Together API)
       ↓
→ Summary + Action Items (JSON response)
```

---

### 📦 Tech Stack

| Layer           | Tool / Library                            |
|------------------|--------------------------------------------|
| Transcription    | `Assembly AI` |
| Preprocessing    | `nltk`, `spacy`, `deepmultilingualpunctuation`, `symspellpy` |
| Summarization    | `facebook/bart-large-cnn` via Hugging Face API |
| Task Extraction  | `mistralai/Mistral-7B-Instruct-v0.1` via Together API |
| Backend API      | FastAPI + Pydantic                         |
| Frontend UI      | Streamlit                                 |
| Containerization | Docker                                     |
| CI/CD            | GitHub Actions → Render                    |

---

### 🛠️ How to Run Locally

#### 1. Clone the repo
```bash
git clone https://github.com/yourusername/meeting-automater.git
cd meeting-automater
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```

#### 3. Run backend API
```bash
uvicorn app.main:app --reload
```

> Set your `API_URL` in the UI file or via `.env`

---

### 🐳 Run with Docker

```bash
docker build -t meeting-automater .
docker run -p 8000:8000 meeting-automater
```

---

### 📈 Example Output

**Input**: 4-minute meeting recording  
**Output**:
```json
{
  "summary": "The team discussed upcoming deadlines...",
  "action_items": [
    {
      "task": "Send client proposal",
      "assigned_to": "Alex",
      "deadline": "Friday"
    },
    {
      "task": "Prepare demo slides",
      "assigned_to": "Nina",
      "deadline": "Tomorrow"
    }
  ]
}
```

---

### 💡 Use Cases

- Post-meeting summaries for managers  
- Auto-documentation for remote teams  
- Follow-up generation in CRM/workspaces  
- Delegation tracking and compliance

---

### 🔐 Environment Variables

Set via `.env` or Render Dashboard:

```env
API_TOKEN=your_huggingface_token
BART_URL=https://api-inference.huggingface.co/models/facebook/bart-large-cnn
MISTRAL_URL=https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1
```

---

### ✍️ Author  
**Mohannad Karim**  
_NLP & Machine Learning Engineer | MLOps_  
[Portfolio](https://www.upwork.com/freelancers/~01683e506def8e06a2?mp_source=share)

---
