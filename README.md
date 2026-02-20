# 🎯 Dual-Strategy Sentiment Analyzer: Reasoning vs. Reliability

### *Advanced NLP Classification using LangChain & Gemini 2.5 Flash*

---

## 📖 Overview

This project is a sophisticated **Sentiment Analysis** engine designed to demonstrate the power of **Prompt Engineering** in LLMs. Unlike standard classifiers, this system processes text through two independent logical pipelines—**Reasoning (Chain-of-Thought)** and **Reliability (Direct Mapping)**—to ensure that the final sentiment is both transparent and highly accurate.

## 🧠 Analysis Methodologies

The engine evaluates inputs using a dual-lens approach:

1. **Reasoning Approach**: Forces the LLM to provide a step-by-step breakdown of emotional triggers and context before deciding the final sentiment. This ensures transparency and "explainable AI".
2. **Reliability Approach**: Focuses on raw classification performance, optimized to reduce variance and provide a consistent, structured response.

## ✨ Core Highlights

* **⚡ Gemini 2.5 Flash Powered:** High-speed inference with zero-shot accuracy.
* **🏗️ LCEL Architecture:** Built using LangChain Expression Language for modular and scalable AI chains.
* **📊 JSON Grounding:** Guaranteed structured output for both approaches, making it ready for integration into larger systems.
* **🛡️ Reliability-Driven:** Comparative analysis helps detect edge cases where sentiment might be ambiguous.

---

## 🛠️ Technical Stack

| Component | Technology | Role |
| --- | --- | --- |
| **Language** | `Python 3.9+` | Core Logic |
| **Orchestration** | `LangChain` | Prompt Chaining & Template Management |
| **LLM** | `Gemini 2.5 Flash` | Analytical Intelligence |
| **Environment** | `python-dotenv` | Secure API Key Management |

---

## 📁 Project Structure

```bash
.
├── 📂 venv/              # Isolated virtual environment
├── 📄 .env               # API Configuration (Sensitive)
├── 🐍 main.py            # Main Analysis Engine
├── 📦 requirements.txt   # Dependency Manifest
└── 📝 output.json        # Structured Analysis Results

```

---

## 🚀 Setup & Deployment

### 1️⃣ Installation

```bash
git clone https://github.com/minasamy01/Sentiment-analysis-using-LLM.git
cd Sentiment-analysis-using-LLM
pip install -r requirements.txt

```

### 2️⃣ Configuration

Create a `.env` file and insert your credentials:

```env
GOOGLE_API_KEY=your_gemini_api_key_here

```

---

## 👨‍💻 Author

# **Mina Samy**
### *AI & NLP Engineer*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mina-data-ai/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BaJL%2F1WTcT2eyQjurm1ZczQ%3D%3D) 
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/minasamy01)

---

