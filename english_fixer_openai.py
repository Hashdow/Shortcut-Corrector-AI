#!/usr/bin/env python3
"""
English and French Grammar Fixer with OpenAI - Corrects grammar and slightly reformulates text
"""

import subprocess
import time
import os
import signal
from pynput import keyboard
from threading import Lock
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="######## YOU_OPEN-AI-KEY-HERE ########")


class EnglishFixerOpenAI:
    def __init__(self):
        self.lock = Lock()
        self.pid_file = "/tmp/english_fixer_openai.pid"
        self.check_single_instance()
        print("✓ OpenAI Grammar Fixer ready!\n")
        
    def check_single_instance(self):
        """Ensure only one instance is running"""
        if os.path.exists(self.pid_file):
            try:
                with open(self.pid_file, 'r') as f:
                    old_pid = int(f.read().strip())
                os.kill(old_pid, signal.SIGTERM)
                time.sleep(0.5)
            except (ValueError, ProcessLookupError, OSError):
                pass
        
        with open(self.pid_file, 'w') as f:
            f.write(str(os.getpid()))
        
    def fix_text(self, text):
        """Fix English text and reformat using OpenAI"""
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an English and French grammar expert. Correct grammar and spelling errors, and slightly reformat the text if needed for clarity in the language you detect. Return ONLY the corrected text, nothing else."
                    },
                    {
                        "role": "user",
                        "content": f"Fix this text:\n\n{text}"
                    }
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            corrected = response.choices[0].message.content.strip()
            return corrected
            
        except Exception as e:
            print(f"Error: {e}")
            return text
    
    def on_hotkey(self):
        """Called when Ctrl+Alt+E is pressed"""
        if not self.lock.acquire(blocking=False):
            return
        
        try:
            # Read directly from X11 selection (PRIMARY) 
            result = subprocess.run(['xclip', '-selection', 'primary', '-o'], 
                                  capture_output=True, text=True, timeout=1)
            original = result.stdout
            
            if not original or len(original.strip()) < 2:
                print("No text selected")
                return
            
            print(f"Fixing text with OpenAI... ({len(original)} chars)")
            corrected = self.fix_text(original)
            
            if corrected == original:
                print("Text is already correct!")
                return
            
            # Copy corrected text to clipboard and paste it
            subprocess.run(['xclip', '-selection', 'clipboard', '-i'], 
                         input=corrected.encode(), check=False)
            time.sleep(0.1)
            subprocess.run(['xdotool', 'key', 'ctrl+v'], check=False)
            
            print(f"✓ Text corrected and pasted!")
            print(f"Original: {original}")
            print(f"Fixed:    {corrected}")
                
        except subprocess.TimeoutExpired:
            print("Timeout reading selection")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.lock.release()
    
    def start(self):
        """Start listening for hotkey"""
        print("English Fixer (OpenAI) is running!")
        print("Select text anywhere and press Ctrl+Alt+R to fix it")
        print("Press Ctrl+C to quit\n")
        
        hotkey = keyboard.GlobalHotKeys({
            '<ctrl>+<alt>+r': self.on_hotkey
        })
        hotkey.start()
        
        try:
            hotkey.join()
        except KeyboardInterrupt:
            print("\nStopping...")
            if os.path.exists(self.pid_file):
                os.remove(self.pid_file)


if __name__ == "__main__":
    try:
        import openai
        import pynput
    except ImportError as e:
        print(f"Missing: {e}")
        print("Install with: pip install openai pynput")
        exit(1)
    
    try:
        subprocess.run(['which', 'xdotool'], check=True, capture_output=True)
        subprocess.run(['which', 'xclip'], check=True, capture_output=True)
    except:
        print("xdotool or xclip not found. Install with: sudo apt install xdotool xclip")
        exit(1)
    
    fixer = EnglishFixerOpenAI()
    fixer.start()
