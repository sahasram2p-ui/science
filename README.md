# Science Tutor 🔬

A domain-specific AI chatbot that answers **only Science-related questions**
— Physics, Chemistry, Biology, Earth Science, Astronomy, and the scientific
method. Any off-topic question is politely declined.

Built with a clean Flask REST API backend and a modern, responsive,
SaaS-style chat UI.

---

## Features

- ⚛️ Strict domain restriction — only answers Science-related questions
- ⚡ Flask REST API (`/api/chat`) powered by the Gemini API
- 🎨 Modern, premium, responsive chat interface (desktop, tablet, mobile)
- 💬 Suggested questions and quick subject categories (Physics, Chemistry, Biology...)
- ⌨️ Enter-to-send, smooth auto-scroll, typing indicator, graceful error handling
- 🔒 API key kept server-side only, loaded from `.env` (never exposed to the browser)

---

## Technologies used

- **Backend:** Python, Flask, Flask REST API
- **AI:** Google GenAI Python SDK (Gemini API)
- **Frontend:** HTML, CSS, JavaScript (no frameworks)

---

## Folder structure

```
project/
├── app.py              # Flask app and /api/chat endpoint
├── config.py            # Loads .env config + domain system prompt
├── requirements.txt      # Python dependencies
├── .env                  # API key & model name (not committed to git)
├── .gitignore
├── README.md
├── templates/
│   └── index.html         # Chat UI markup
└── static/
    ├── style.css           # Premium, responsive styling
    └── script.js            # Chat logic (fetch, rendering, UX)
```

---

## Installation

### 1. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your `.env` file

Open the `.env` file in the project root and add your real Gemini API key:

```
GEMINI_API_KEY=your_actual_api_key_here
GEMINI_MODEL=gemini-3.8-flash
```

> Get an API key from [Google AI Studio](https://aistudio.google.com/).
> Never share this key or commit the `.env` file to GitHub —
> it is already listed in `.gitignore`.

### 4. Run the application

```bash
python app.py
```

### 5. Open in your browser

```
http://127.0.0.1:5000
```

---

## Domain restriction explanation

The chatbot is instructed (via a system prompt defined in `config.py`) to
only answer questions related to **Science** — Physics, Chemistry, Biology,
Earth Science, Astronomy, the scientific method, and related school/college
curriculum topics.

If a user asks something unrelated (cooking, sports scores, politics,
entertainment, etc.), the assistant responds with:

> "Sorry, I can answer only Science-related questions."

This restriction is enforced entirely through the system prompt sent to
Gemini with every request — no keyword filtering is used, so the assistant
can still understand naturally phrased science questions while rejecting
anything outside its domain.

---

## API reference

**POST** `/api/chat`

Request body:
```json
{ "message": "Why is the sky blue?" }
```

Success response:
```json
{ "success": true, "reply": "..." }
```

Error response:
```json
{ "success": false, "error": "..." }
```
