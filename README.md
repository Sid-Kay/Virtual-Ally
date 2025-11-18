# Virtual-Ally

**Virtual-Ally** is a personal multi-agent assistant that mixes fashion, architecture, 90s rom‑com vibes, light workouts, and tiny movie-inspired micro-games — packaged as a clean, beginner-friendly Python project suitable for a Kaggle Capstone submission.

This repository is intentionally safe to publish publicly: **no API keys or personal data are included**. If you'd like to hook up a real LLM (like OpenAI), follow the steps in `config.py` and use environment variables locally — **do not** commit any secret keys.

---

## Quick demo (what it does)
Run the project locally and it will:
- Simulate LLM responses for stylist, architecture, game and workout agents
- Save a `outputs/package.json` with the combined results
- Create placeholder moodboard image files in `outputs/`

---

## Project structure
```
virtual-ally/
├── main.py
├── helpers.py
├── config.py
├── agents.py
├── tools.py
├── prompts/
│   ├── style_prompt.txt
│   ├── arch_prompt.txt
│   └── game_prompt.txt
├── requirements.txt
├── .gitignore
├── README.md
├── LICENSE
└── outputs/ (created at runtime)
```

---

## How to run locally (VSCode / terminal)
1. Extract this repo folder.
2. Make and activate a Python virtual environment:
   - `python -m venv venv`
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install dependencies:
   - `pip install -r requirements.txt`
4. (Optional) If you want to use a real OpenAI key, create a `.env` file locally **(do NOT commit it)** and add:
   ```
   OPENAI_API_KEY=sk-...
   ```
   The project will **not** run with a real API key by default — it falls back to a simulated LLM so it's safe to publish.
5. Run:
   - `python main.py`
6. Check `outputs/package.json` and the placeholder images in `outputs/`

---

## How to upload safely to GitHub (no leaks)
1. Make sure `.gitignore` (included) exists — it already ignores `.env`, `outputs/`, `*.key`, and common sensitive files.
2. Do **NOT** create or upload any file named `.env` or with keys inside.
3. Create a new GitHub repo (e.g., `Virtual-Ally`) and either drag-and-drop the project files into the web UI or use `git` CLI:
   - `git init`
   - `git add .`
   - `git commit -m "Initial commit"`
   - `git branch -M main`
   - `git remote add origin https://github.com/<yourname>/Virtual-Ally.git`
   - `git push -u origin main`
4. Once uploaded, copy the GitHub repo URL and paste it into your Kaggle write-up.

---

## Kaggle write-up tip
- Add a short link to your GitHub repo under a section **Code & Repo**.
- If you use real API keys in Kaggle, use Kaggle Secrets, not a committed `.env`.

---

If you want, I can also:
- Create a polished Kaggle Notebook (copy-paste cells) from this code
- Make a short video script for your submission
- Help push to GitHub with CLI commands on your machine

Enjoy exploring Virtual-Ally! ✨
