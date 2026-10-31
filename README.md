<div align="center">
  <h1>J.A.R.V.I.S. // Mark 85</h1>
  <p><strong>Iron Man Mark 85 Arc Reactor Holographic HUD & Autonomous Voice Assistant</strong></p>
  <p>
    <a href="https://jarvis.syahmiaof.my"><img src="https://img.shields.io/badge/Demo-Live-101713?style=for-the-badge&logoColor=60E1B5&labelColor=101713" alt="Demo" /></a>
    <a href="https://github.com/syahmiaof/jarvis-mark85"><img src="https://img.shields.io/badge/Source-GitHub-101713?style=for-the-badge&logo=github&logoColor=60E1B5&labelColor=101713" alt="GitHub" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-101713?style=for-the-badge&logoColor=60E1B5&labelColor=101713" alt="License" /></a>
    <a href="https://syahmiaof.my"><img src="https://img.shields.io/badge/Author-syahmiaof-101713?style=for-the-badge&logo=vercel&logoColor=60E1B5&labelColor=101713" alt="Author" /></a>
  </p>

  <img src="preview.png" alt="J.A.R.V.I.S. Mark 85 Holographic HUD Preview" width="100%" style="border-radius: 8px; box-shadow: 0 0 30px rgba(0,245,255,0.3);" />

  <br/><br/>

  <p><strong>An ultra-sleek, Iron Man holographic interface and autonomous hands-free voice assistant engineered by Syahmi.</strong></p>

  <p><a href="https://jarvis.syahmiaof.my">Live Holographic Web HUD</a> • <a href="#-key-features">Features</a> • <a href="#-quickstart">Quickstart</a> • <a href="#%EF%B8%8F-tech-stack">Tech Stack</a></p>
</div>

---

## ✨ Key Features

- **🦾 Minimalist Mark 85 Arc Reactor HUD:** Obsidian dark glassmorphism with counter-rotating cyan & amber plasma energy rings.
- **🎙️ Real-Time Dual-Language Speech Recognition:** Seamlessly understands **Bahasa Melayu** and **English** with zero typing required.
- **🔊 Microsoft Ryan Neural British TTS:** Authentic, crisp Iron Man Jarvis voice synthesis powered by Edge Neural Voice.
- **⚡ Hands-Free Continuous Conversational Loop:** Eliminates repetitive button pressing or claps—speak naturally back-and-forth.
- **🧠 Dual AI Engine (Zero Cost):**
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
| **Cloud AI Gateway** | Vercel Serverless Function (`/api/chat.js`) |
| **Cloud LLM Provider** | OpenRouter (`minimax/minimax-m3.1-flash:free`, `openrouter/free`) |
| **Local LLM Engine** | Ollama (`llama3.2:1b`, `qwen3.5:2b`) |
| **Domain & DNS** | Cloudflare Edge DNS (`jarvis.syahmiaof.my`) |
| **CI / Quality** | GitHub Actions, Node syntax validation |

---

## 🚀 Quickstart

### Option A: Web Holographic HUD (Vercel / Browser)

1. Clone the repository:
   ```bash
   git clone https://github.com/syahmiaof/jarvis-mark85.git
   cd jarvis-mark85
   ```
2. Validate syntax:
   ```bash
   npm run check
   ```
3. Open `index.html` directly in your browser or deploy instantly to Vercel:
   ```bash
   vercel
   ```
4. Set your environment variable in Vercel:
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

**Muhammad Syahmi**  
- GitHub: [@syahmiaof](https://github.com/syahmiaof)  
- Website: [syahmiaof.my](https://syahmiaof.my)  
- Project HUD: [jarvis.syahmiaof.my](https://jarvis.syahmiaof.my)

---

<div align="center">
  <sub>Engineered with precision for autonomous AI interaction. J.A.R.V.I.S. Mark 85 Neural Matrix.</sub>
</div>
