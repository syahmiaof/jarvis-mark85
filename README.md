# 👑 J.A.R.V.I.S. // Mark 85 Holographic HUD & Voice Assistant

<div align="center">

![JARVIS Banner](https://img.shields.io/badge/J.A.R.V.I.S.-MARK%2085-00f5ff?style=for-the-badge&logo=probot&logoColor=white)
![Architect](https://img.shields.io/badge/ARCHITECT-SYAHMI-ff6600?style=for-the-badge)
![License](https://img.shields.io/badge/COST-RM%200.00%20FREE-00ff88?style=for-the-badge)
![Deployment](https://img.shields.io/badge/DEPLOYMENT-VERCEL%20%2B%20CLOUDFLARE-000000?style=for-the-badge&logo=vercel&logoColor=white)

**An ultra-sleek, billionaire-tier Iron Man holographic interface and autonomous hands-free voice assistant engineered by Syahmi.**

[🌐 Live Holographic Web HUD](https://jarvis.syahmiaof.my) • [🚀 Features](#-key-features) • [⚡ Quickstart](#-quickstart) • [🧠 AI Architecture](#-ai-architecture)

</div>

---

## ✨ Key Features

- **🦾 Minimalist Mark 85 Arc Reactor HUD:** Obsidian dark glassmorphism with counter-rotating cyan & amber plasma energy rings.
- **🎙️ Real-Time Dual-Language Speech Recognition:** Seamlessly understands **Bahasa Melayu** and **English** with zero typing required.
- **🔊 Microsoft Ryan Neural British TTS:** Authentic, crisp Iron Man Jarvis voice synthesis powered by Edge Neural Voice.
- **⚡ Hands-Free Continuous Conversational Loop:** Eliminates repetitive button pressing or claps—speak naturally back-and-forth.
- **🧠 Dual AI Engine (Zero Cost - RM 0.00):**
  - **Cloud Intelligence:** OpenRouter Free Tier (*MiniMax M3.1 Flash / Qwen 2.5 / DeepSeek*).
  - **Local Hardware Intelligence:** Offline Ollama (*Llama 3.2 1B / Qwen 3.5 2B*).
- **🛡️ Cloud & Local Versatility:** Deployable on Vercel with serverless AI proxy or runnable completely offline on local laptop hardware.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Frontend HUD** | HTML5, CSS3 Glassmorphism, Web Audio API, Canvas 2D |
| **Voice Synthesis** | Microsoft Ryan Neural (`en-GB-RyanNeural`) / Web Speech API |
| **Speech-to-Text** | Web Speech API (`ms-MY` & `en-US`) / SpeechRecognition |
| **Cloud AI Gateway** | Vercel Edge Serverless Function (`/api/chat`) |
| **Cloud LLM Provider** | OpenRouter (`minimax/minimax-m3.1-flash:free`, `openrouter/free`) |
| **Local LLM Engine** | Ollama (`llama3.2:1b`, `qwen3.5:2b`) |
| **Domain & DNS** | Cloudflare Edge DNS (`jarvis.syahmiaof.my`) |

---

## 🚀 Quickstart

### Option A: Web Holographic HUD (Vercel / Browser)

1. Clone the repository:
   ```bash
   git clone https://github.com/syahmiaof/jarvis-mark85.git
   cd jarvis-mark85
   ```
2. Open `index.html` directly in your browser or deploy instantly to Vercel:
   ```bash
   vercel
   ```
3. Set your environment variable in Vercel:
   - `OPENROUTER_API_KEY`: Your free OpenRouter API key.

---

### Option B: Local Python Continuous Voice Assistant (`jarvis_voice.py`)

Run JARVIS natively on your laptop with double-clap detection, terminal HUD, and local speaker output:

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your free API key (optional, falls back to local Ollama automatically):
   ```bash
   # Windows PowerShell
   $env:OPENROUTER_API_KEY="sk-or-v1-your-key-here"
   ```
3. Start JARVIS:
   ```bash
   python jarvis_voice.py
   ```
4. Clap your hands twice 👏 or press **[Enter]** to engage JARVIS!

---

## 👑 Author

**Syahmi**  
- GitHub: [@syahmiaof](https://github.com/syahmiaof)  
- Website: [syahmiaof.my](https://syahmiaof.my)  
- Project HUD: [jarvis.syahmiaof.my](https://jarvis.syahmiaof.my)

---

<div align="center">
  <sub>Engineered with precision for autonomous AI interaction. J.A.R.V.I.S. Mark 85 Neural Matrix.</sub>
</div>
