# 🌐 BrowserStack Selenium Automation – End-to-End Testing Solution

---

## 📌 Project Summary

This project demonstrates a complete automation testing workflow built using Selenium and executed across cloud devices using BrowserStack.

The solution performs automated web scraping from the El País Opinion section, integrates with a translation API, performs text analytics, and validates cross-browser compatibility using parallel cloud execution.

This project simulates a real-world Customer Engineering scenario involving:
- Customer environment validation
- Automation reliability
- Cloud test execution
- API + automation integration

---

## 🎯 Problem Statement

Build an automation solution that:

- Scrapes articles from a live news website
- Integrates with an external translation API
- Performs text analysis
- Executes cross-browser validation on real devices
- Runs tests in parallel on BrowserStack cloud infrastructure

---

## 🏗 System Architecture

            ┌─────────────────────┐
            │   Local Python App  │
            │  (Selenium Scripts) │
            └──────────┬──────────┘
                       │
                       │ HTTP Requests
                       ▼
          ┌─────────────────────────┐
          │     El País Website     │
          │  (Article Data Source)  │
          └─────────────────────────┘

                       │
                       │ Article Titles
                       ▼

          ┌─────────────────────────┐
          │  RapidAPI Google        │
          │  Translation Service    │
          └─────────────────────────┘

                       │
                       │ Translated Titles
                       ▼

          ┌─────────────────────────┐
          │ Text Processing Engine  │
          │ Word Frequency Analysis │
          └─────────────────────────┘

                       │
                       │ Test Execution Requests
                       ▼

          ┌─────────────────────────┐
          │ BrowserStack Cloud      │
          │ Parallel Device Testing │
          └─────────────────────────┘

                       │
                       ▼
               Execution Logs + Results

---

## 🔄 Execution Flow

### Phase 1 — Data Collection
- Open El País Opinion section
- Extract first 5 valid articles
- Extract Spanish article content
- Download article images

---

### Phase 2 — Data Processing
- Translate article titles using Google Translate API
- Normalize text data
- Perform word repetition analysis

---

### Phase 3 — Cloud Test Execution
- Connect to BrowserStack Automate
- Execute Selenium tests on:
  - Windows Chrome
  - Windows Edge
  - macOS Safari
  - Samsung Galaxy S22
  - iPhone 13
- Run all tests in parallel

---

## ☁ BrowserStack Test Strategy

| Category | Coverage |
|---|---|
| Desktop Browsers | Chrome, Edge, Safari |
| Mobile Devices | Android + iOS |
| Execution Mode | Parallel |
| Test Type | Functional Validation |

---


## ⚙ Technology Stack

### Automation
- Selenium 4
- WebDriver Manager

### Backend Processing
- Python 3
- Requests Library
- Collections (Text Analytics)

### Cloud Testing
- BrowserStack Automate
- Parallel Execution (Threading)

### API Integration
- RapidAPI Google Translate

---
# 🔐 Environment Variables (.env Setup)

⚠ **Important:**
This project uses environment variables to securely store API credentials.
Do NOT hardcode sensitive keys in the source code.

---

## Step 1: Create `.env` File

Create a file named:

```
.env
```

Add the following:

```
# ==========================
# RapidAPI - Google Translate
# ==========================
RAPIDAPI_KEY=your_rapidapi_key_here

# ==========================
# BrowserStack Credentials
# ==========================
BROWSERSTACK_USERNAME=your_browserstack_username
BROWSERSTACK_ACCESS_KEY=your_browserstack_access_key
```

---

## Step 2: Install dotenv

```bash
pip install python-dotenv
```

---

## Step 3: Load Environment Variables in Python

```python
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
BROWSERSTACK_USERNAME = os.getenv("BROWSERSTACK_USERNAME")
BROWSERSTACK_ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
```

---

## Step 4: Add `.env` to `.gitignore`

Create or update `.gitignore`:

```
.env
```

This prevents secrets from being pushed to GitHub.

---
## 🚀 Setup Instructions

### Install Dependencies

---

### Run BrowserStack Parallel Execution
Update credentials:

---

### Run BrowserStack Parallel Execution
Update credentials:
USERNAME = "your_browserstack_username"
ACCESS_KEY = "your_access_key"

Run:
python browserstack_test.py

---

## 📊 Logging & Monitoring

The solution provides:

- Device-specific execution logs
- API response validation logs
- Scraping progress tracking
- Error-safe execution handling

---

## 🧠 Engineering Highlights

✔ Handles dynamic website loading  
✔ Uses explicit waits for stability  
✔ Implements cloud-based automation testing  
✔ Executes multi-device parallel testing  
✔ Integrates external APIs reliably  
✔ Maintains clean modular automation structure  

---

## 👨‍💻 Author

**Sanket Bauskar**  
Computer Engineering Student  

---

## ⭐ Key Learning Outcomes

- Real-world Selenium automation architecture
- Cloud test infrastructure integration
- Parallel execution design patterns
- API + Automation system integration
- Production-grade logging practices

---

## 🙏 Acknowledgements

- BrowserStack Cloud Testing Platform  
- Selenium Open Source Community  
- El País News Platform  
