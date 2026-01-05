# English Fixer

A powerful grammar correction tool for Linux that works with global hotkeys. Uses OpenAI's GPT for advanced grammar correction and text reformulation.

## Features

✨ **AI-Powered Correction:**
- Uses GPT-3.5-turbo for accurate grammar correction
- Intelligent text reformulation for clarity
- Supports English and French

🎯 **Key Features:**
- Global hotkey activation (works in any application)
- Automatic clipboard integration
- Single instance protection (only one process at a time)
- Fast and lightweight
- Works with X11/Wayland on Linux

## Installation

### Prerequisites

- Python 3.7+
- Linux (tested on Linux Mint, Ubuntu, Debian)
- `xdotool` and `xclip` utilities

### Step 1: Install System Dependencies

```bash
sudo apt update
sudo apt install -y xdotool xclip python3-pip default-jre
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install openai pynput
```

## Configuration

### OpenAI Version Setup

1. Get your OpenAI API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Open `english_fixer_openai.py`
3. Replace this line:
   ```python
   client = OpenAI(api_key="######## YOU_OPEN-AI-KEY-HERE ########")
   ```
   WSetup Your OpenAI API Key

1. Get your OpenAI API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Open `english_fixer_openai.py`
3. Replace this line:
   ```python
   client = OpenAI(api_key="######## YOU_OPEN-AI-KEY-HERE ########")
   ```
   With your actual API key:
   ```python
   client = OpenAI(api_key="sk-proj-YOUR_ACTUAL_KEY_HERE")
   ```
4. Save the file

```bash
python3 english_fixer_openai.py
```

### Hotkey

Select any text in any application and press **Ctrl+Alt+R**

#### Option 1: Linux Mint Startup Applications (GUI)

1. Open **Startup Applications**
2. Click **Add**
3. Set:
   - **Name**: English Fixer
   - **Command**: `/usr/bin/python3 /path/to/english_fixer_openai.py`
   - **Comment**: Grammar correction tool
4. Click **Add**

#### Option 2: Create a Systemd Service (Recommended)

Create `/etc/systemd/user/english-fixer.service`:
```ini
[Unit]
Description=English Grammar Fixer
After=graphical-session.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 /path/to/english_fixer_openai.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=graphical-session.target
```

Enable and start:
```bash
systemctl --user enable english-fixer.service
systemctl --user start english-fixer.service
```

Check status:
```bash
systemctl --user status english-fixer.service
journalctl --user -u english-fixer.service -f
```

#### Option 3: Add to `.bashrc` or `.profile`

Add this line to `~/.bashrc` or `~/.profile`:
```bash
python3 /path/to/english_fixer_openai.py &
```

#### Option 4: Create a Desktop Shortcut

Create `~/.local/share/applications/english-fixer.desktop`:
```ini
[Desktop Entry]
Type=Application
Name=English Fixer
Exec=python3 /path/to/english_fixer_openai.py
NoDisplay=true
X-GNOME-Autostart-enabled=true
```

Then make it executable:
```bash
chmod +x ~/.local/share/applications/english-fixer.desktop
```

## Dependencies

### OpenAI Version (`requirements_openai.txt`)
- `openai>=1.0.0` - OpenAI API client
- `pynput>=1.7.6` - Global hotkey listening
- `xdotool` - System tool for keyboard/mouse automation
- `xclip` - System tool for clipboard management

### Python Packages (`requirements.txt`)
- `openai>=1.0.0` - OpenAI API client
- `pynput>=1.7.6` - Global hotkey listening

### System Tools
- `xdotool` - Keyboard/mouse automation
- `xclip` - Clipboard management
3. Sends text to OpenAI GPT-3.5-turbo
4. Replaces original text with corrected version
5. Returns to waiting state

### Local Version
1. Listens for global hotkey press (Ctrl+Shift+F)
2. Reads selected text from clipboard
1. Listens for global hotkey press (Ctrl+Alt+R)
2. Reads selected text from clipboard
3. Sends text to OpenAI GPT-3.5-turbo for correction
### "xclip not found"
```bash
sudo apt install xclip
```

### "No text selected" message
- Make sure you have text selected before pressing the hotkey
- Some applications may not support X11 clipboard operations

### API Key errors (OpenAI version)
- Verify your API key is correct
- Check your OpenAI account has sufficient credits
- Ensure the key starts with `sk-proj-`

### LanguageTool timeout (Local version)
- This happens on first run while downloading language rules
- Subsequent runs will be faster

## Security Note

⚠️ **IMPORTANT**: Never commit your OpenAI API key to version control!
- Add `english_fix
- Verify your API key is correct
- Check your OpenAI account has sufficient credits
- Ensure the key starts with `sk-proj-`
```

Then set the environment variable:
```bash
export OPENAI_API_KEY="your-key-here"
```

## Performance

- **OpenAI Version**: ~2-3 seconds per request (depends on internet speed and API latency)
- **Local Version**: ~1-2 seconds on first run, ~0.5 seconds after that

## Supported Languages

- **English**: Full support
- **French**: Supported by both versions

## License

Free to use and modify

## Contributing

Feel free to fork and improve!

## Keyboard Shortcuts Summary

| Action | Shortcut |
|--------|----------|
| Fix text (OpenAI) | Ctrl+Alt+R |
| Fix text (Local) | Ctrl+Shift+F |
| Exit | Ctrl+C |

---

**Happy writing!** ✨


| Action | Shortcut |
|--------|----------|
| Fix text | Ctrl+Alt+R