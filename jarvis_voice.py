"""
JARVIS Voice Assistant (TikTok Edition)
=======================================
Features:
- 👏 Double Clap Detection (Tepuk tangan 2 kali)
- 🎙️ Speech Recognition (English & Bahasa Melayu)
- 🧠 Dual AI Engine: Cloud (DeepSeek/OpenRouter) with Local Ollama Fallback (RM 0.00)
- 🔊 Iron Man British Voice (Microsoft Edge TTS: en-GB-RyanNeural)
- ⌨️ Press [ENTER] shortcut to speak instantly
"""

import os
import sys
import time
import asyncio
import threading
import tempfile
import winsound

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import numpy as np
import requests
import sounddevice as sd
import speech_recognition as sr
import edge_tts
import pygame

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# ANSI Color Codes
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

SYSTEM_PROMPT = (
    "You are J.A.R.V.I.S., the legendary British AI assistant engineered and developed by Boss Syahmi. "
    "Address the user as 'Boss Syahmi' or 'sir'. "
    "Respond in character: polite, sharp, witty, and concise. "
    "CRITICAL: Keep your spoken answer to 1 or 2 sentences maximum. "
    "Do NOT output internal thoughts or explanations. "
    "You can understand Bahasa Melayu and English, but speak back in your charming British style."
)

OLLAMA_URL = "http://127.0.0.1:11434"

def get_best_ollama_model():
    """Detect available Ollama models, prefer fast models like llama3.2:1b or qwen3.5:2b."""
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        if r.status_code == 200:
            models = [m["name"] for m in r.json().get("models", [])]
            for pref in ["llama3.2:1b", "llama3.2:3b", "qwen2.5:1.5b", "qwen3.5:2b"]:
                for m in models:
                    if m.startswith(pref):
                        return m
            if models:
                return models[0]
    except Exception:
        pass
    return "qwen3.5:2b"

def play_chime_activation():
    """Play a futuristic Iron Man HUD activation sound."""
    try:
        winsound.Beep(1200, 90)
        winsound.Beep(1800, 140)
    except Exception:
        pass

def play_chime_done():
    """Play a soft tone when speech capture completes."""
    try:
        winsound.Beep(900, 70)
    except Exception:
        pass

async def text_to_speech_file(text: str, output_path: str):
    """Generate British speech audio using edge-tts."""
    communicate = edge_tts.Communicate(text, voice="en-GB-RyanNeural", rate="+5%")
    await communicate.save(output_path)

def speak(text: str):
    """Speak text using Microsoft Ryan Neural British Voice."""
    if not text.strip():
        return
    print(f"\n{MAGENTA}{BOLD}🔊 JARVIS:{RESET} \"{text}\"")
    temp_mp3 = os.path.join(tempfile.gettempdir(), f"jarvis_{int(time.time()*1000)}.mp3")
    try:
        asyncio.run(text_to_speech_file(text, temp_mp3))
        pygame.mixer.music.load(temp_mp3)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)
        pygame.mixer.music.unload()
    except Exception as e:
        print(f"{RED}[TTS Error: {e}]{RESET}")
    finally:
        if os.path.exists(temp_mp3):
            try:
                os.remove(temp_mp3)
            except Exception:
                pass

def query_ai(user_prompt: str) -> str:
    """Query Cloud AI if available, otherwise seamlessly fallback to Local Ollama."""
    print(f"{CYAN}🧠 JARVIS is thinking...{RESET}", end="", flush=True)
    t0 = time.time()
    
    # 1. Try OpenRouter Cloud (minimax/minimax-m3.1-flash:free or openrouter/free)
    openrouter_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if openrouter_key and not openrouter_key.startswith("your_"):
        candidates = [
            os.environ.get("OPENROUTER_MODEL", "minimax/minimax-m3.1-flash:free"),
            "openrouter/free"
        ]
        for or_model in candidates:
            try:
                r = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {openrouter_key}",
                        "Content-Type": "application/json",
                        "HTTP-Referer": "https://openjarvis.ai",
                        "X-Title": "JARVIS Voice Assistant",
                    },
                    json={
                        "model": or_model,
                        "messages": [
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": user_prompt},
                        ],
                        "max_tokens": 150,
                        "temperature": 0.7,
                    },
                    timeout=10,
                )
                if r.status_code == 200:
                    msg = r.json()["choices"][0]["message"]
                    content = (msg.get("content") or "").strip()
                    if content:
                        latency = round(time.time() - t0, 2)
                        print(f" {GREEN}[OpenRouter {or_model} • {latency}s]{RESET}")
                        return content
            except Exception:
                continue

    # 2. Try DeepSeek Cloud if API key is provided
    deepseek_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
    if deepseek_key and not deepseek_key.startswith("your_"):
        try:
            r = requests.post(
                "https://api.deepseek.com/chat/completions",
                headers={
                    "Authorization": f"Bearer {deepseek_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": "deepseek-chat",
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    "max_tokens": 80,
                    "temperature": 0.7,
                },
                timeout=8,
            )
            if r.status_code == 200:
                content = r.json()["choices"][0]["message"]["content"].strip()
                latency = round(time.time() - t0, 2)
                print(f" {GREEN}[DeepSeek Cloud • {latency}s]{RESET}")
                return content
            elif r.status_code == 402:
                # Insufficient balance, fall through to local Ollama
                print(f" {YELLOW}[DeepSeek 402: Insufficient Balance -> Switching to Local Ollama]{RESET}")
        except Exception:
            pass

    # 2. Local Ollama (100% Free / RM 0.00 / Offline)
    best_model = get_best_ollama_model()
    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/chat",
            json={
                "model": best_model,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt},
                ],
                "stream": False,
                "options": {
                    "num_predict": 70,
                    "temperature": 0.7,
                },
            },
            timeout=30,
        )
        if r.status_code == 200:
            data = r.json()
            reply = data.get("message", {}).get("content", "").strip()
            # If model put everything in thinking or empty, try response field
            if not reply:
                reply = data.get("response", "").strip()
            if not reply:
                reply = "Indeed, sir. All systems are operating normally."
            latency = round(time.time() - t0, 2)
            print(f" {GREEN}[Ollama {best_model} • {latency}s]{RESET}")
            return reply
    except Exception as e:
        print(f" {RED}[Ollama Error: {e}]{RESET}")

    return "At your service, sir. I encountered a slight computational delay."

class JarvisAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = 300
        self.is_active = False
        self.running = True
        
        # Clap detector parameters
        self.clap_times = []
        self.clap_threshold = 0.25  # Initial threshold
        self.noise_floor = 0.03
        self.lock = threading.Lock()

    def calibrate_noise(self, duration=1.0):
        """Calibrate microphone ambient sound level to adjust clap threshold."""
        print(f"{YELLOW}🎙️ Calibrating ambient room noise for 1 second...{RESET}")
        try:
            recording = sd.rec(int(duration * 44100), samplerate=44100, channels=1, dtype='float32')
            sd.wait()
            rms = float(np.sqrt(np.mean(recording**2)))
            self.noise_floor = max(0.01, rms)
            # Threshold set to 4x ambient or minimum 0.18
            self.clap_threshold = max(0.18, min(0.60, self.noise_floor * 5.0))
            print(f"{GREEN}✓ Calibrated. Clap sensitivity set to {self.clap_threshold:.2f} (Ambient: {self.noise_floor:.3f}){RESET}\n")
        except Exception as e:
            print(f"{YELLOW}! Calibration fallback: using default threshold ({e}){RESET}\n")

    def audio_callback(self, indata, frames, time_info, status):
        """Continuous audio stream callback to detect double claps."""
        if self.is_active or not self.running:
            return
        
        peak = float(np.max(np.abs(indata)))
        now = time.time()

        if peak > self.clap_threshold:
            with self.lock:
                # Filter out ringing of the same clap (< 0.12s)
                if not self.clap_times or (now - self.clap_times[-1]) > 0.12:
                    self.clap_times.append(now)
                    # Keep only last 2 claps
                    self.clap_times = [t for t in self.clap_times if (now - t) < 1.0]

                    if len(self.clap_times) >= 2:
                        diff = self.clap_times[-1] - self.clap_times[-2]
                        if 0.15 <= diff <= 0.85:
                            print(f"\n{GREEN}{BOLD}👏 [DOUBLE CLAP DETECTED! (Δt={diff:.2f}s)]{RESET}")
                            self.clap_times.clear()
                            self.trigger_interaction("double_clap")

    def trigger_interaction(self, source="voice"):
        """Activate JARVIS and enter continuous conversational loop."""
        self.is_active = True
        try:
            play_chime_activation()
            print(f"\n{CYAN}{BOLD}⚡ [JARVIS CONVERSATION MODE ACTIVE]{RESET}")
            print(f"{CYAN}Bercakap je secara santai, tak payah tekan Enter lagi! (Cakap 'Goodbye' atau 'Standby' bila nak rehat){RESET}\n")
            
            consecutive_silence = 0
            while self.running:
                print(f"{GREEN}🎙️ [LISTENING] Speak anytime...{RESET}")
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.25)
                    try:
                        audio = self.recognizer.listen(mic, timeout=7, phrase_time_limit=12)
                        play_chime_done()
                        print(f"{YELLOW}🎙️ Transcribing speech...{RESET}")
                        
                        # Try English first, fallback to Malay
                        try:
                            text = self.recognizer.recognize_google(audio, language="en-US")
                        except Exception:
                            text = self.recognizer.recognize_google(audio, language="ms-MY")

                        print(f"{BOLD}👤 You said:{RESET} \"{text}\"")

                        # Exit / standby phrases
                        lower_text = text.lower()
                        if any(w in lower_text for w in ["exit", "quit", "stop", "tutup", "selesai", "bye jarvis", "goodbye", "standby", "tidur", "rehat"]):
                            speak("Standing down, sir. Call me whenever you need.")
                            break

                        # Query AI and speak
                        answer = query_ai(text)
                        speak(answer)
                        consecutive_silence = 0
                        time.sleep(0.3)

                    except sr.WaitTimeoutError:
                        consecutive_silence += 1
                        if consecutive_silence >= 2:
                            print(f"{YELLOW}⌛ Tiada percakapan dikesan. Kembali ke mod standby.{RESET}")
                            break
                    except sr.UnknownValueError:
                        print(f"{YELLOW}❓ Bunyi kurang jelas. Masih mendengar...{RESET}")
                    except Exception as e:
                        print(f"{RED}[Recognition Error: {e}]{RESET}")
                        break

        finally:
            self.is_active = False
            if self.running:
                print(f"\n{GREEN}🟢 [STANDBY] Ready! 👏 Tepuk 2 kali atau tekan [ENTER] bila-bila masa...{RESET}")

    def keyboard_listener(self):
        """Allow user to press Enter at any time to trigger JARVIS."""
        while self.running:
            try:
                line = sys.stdin.readline()
                if not self.running:
                    break
                if not self.is_active:
                    self.trigger_interaction("keyboard")
            except Exception:
                break

    def run(self):
        banner = f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════════════════════╗
║             J.A.R.V.I.S. MARK 85 VOICE ASSISTANT                 ║
║               👑 DEVELOPED BY SYAHMI // RM 0.00                  ║
║               Continuous Hands-Free Neural Matrix                ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
{BOLD}Interactive Triggers:{RESET}
  👏  {BOLD}Double Clap:{RESET} Clap your hands twice rapidly!
  ⌨️   {BOLD}Press [ENTER]:{RESET} Hit Enter anytime on your keyboard to speak!
  🛑  {BOLD}To Quit:{RESET} Say "Goodbye Jarvis" or press Ctrl+C
"""
        print(banner)
        
        # Display detected model & key
        ollama_model = get_best_ollama_model()
        openrouter_key = os.environ.get("OPENROUTER_API_KEY", "").strip()
        or_model = os.environ.get("OPENROUTER_MODEL", "minimax/minimax-m3.1-flash:free")
        or_status = f"Active ({or_model})" if openrouter_key else "Not set"
        deepseek_key = os.environ.get("DEEPSEEK_API_KEY", "").strip()
        ds_status = "Configured" if deepseek_key else "Not set"
        print(f"• Local AI Model : {GREEN}{ollama_model} (Ollama RM 0.00){RESET}")
        print(f"• OpenRouter     : {GREEN}{or_status}{RESET}")
        print(f"• DeepSeek API   : {GREEN}{ds_status}{RESET}")
        print(f"• British Voice  : {GREEN}Microsoft Ryan Neural (Iron Man Jarvis){RESET}\n")

        # Calibrate room microphone
        self.calibrate_noise(duration=1.0)

        # Welcome message
        speak("All quantum neural systems online, Boss Syahmi. J.A.R.V.I.S. is ready at your command.")

        # Start keyboard listener thread
        kb_thread = threading.Thread(target=self.keyboard_listener, daemon=True)
        kb_thread.start()

        # Start sounddevice audio input stream for clap detection
        print(f"{GREEN}🟢 [STANDBY] Listening for 👏 Double Clap, or press [ENTER] to speak...{RESET}\n")
        try:
            with sd.InputStream(
                channels=1,
                samplerate=44100,
                blocksize=1024,
                callback=self.audio_callback,
            ):
                while self.running:
                    time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            print(f"\n{YELLOW}Jarvis shutting down. Have a splendid day, sir!{RESET}")

if __name__ == "__main__":
    assistant = JarvisAssistant()
    assistant.run()
