# 📥 Telegram Video Downloader

A fast, browser-based Telegram video downloader built using **Python**, **Flask**, and **Telethon**.  
Supports public/private channels, real-time download progress, and direct browser downloads.

---

## 🚀 Features

- 🔐 Login & fetch from private or public channels
- 🎬 Preview and download videos directly in the browser
- ⚡ Fast download using `iter_download()` or `download_file()`
- 🌐 Simple responsive HTML frontend
- ✅ Supports long videos and large file sizes

---

## 🛠 Tech Stack

- Python 3
- Flask
- Telethon
- HTML/CSS
- JavaScript (for frontend interactivity)

---

## 🧪 Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/Codesickm/telegram-video-downloader.git
cd telegram-video-downloader

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
python app.py
```

---

## 🌐 Usage

1. Open `index.html` in your browser
2. Enter Telegram video link from a channel/chat
3. Click **Download**
4. ✅ File will be served directly from browser

---

## 📁 Folder Structure

```
telegram-video-downloader/
├── app.py
├── index.html
├── templates/ (optional)
├── static/    (optional)
├── downloads/ (auto-created)
```

> Note: `downloads/` folder is auto-created and ignored from Git using `.gitignore`.

---

## 📸 Preview

_Add a screenshot of your UI or terminal download preview here_

---

## 🧠 Created with 💛 by Mohit (a.k.a Codesickm)"# Telegram-Python-Video-Downloader" 
"# Telegram-Python-Video-Downloader" 
