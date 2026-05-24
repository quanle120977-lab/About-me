import tkinter as tk
from tkinter import messagebox, filedialog
import ctypes
import urllib.request
import sys
import os

# --- 1. UPDATE CONFIGURATION ---
CURRENT_VERSION = "2.0"
# These point exactly to your 'Raw' files on GitHub


VERSION_URL = "https://raw.githubusercontent.com/xuanbachle/BanhCode/main/version.txt"
UPDATE_URL = "https://raw.githubusercontent.com/xuanbachle/BanhCode/main/python%20music%20rock%20edition.py"



def check_for_updates():
    try:
        # Check version online
        with urllib.request.urlopen(VERSION_URL, timeout=5) as response:
            latest_version = response.read().decode('utf-8').strip()

        # If GitHub says 2.0 and we are 1.0, show the popup!
        if latest_version > CURRENT_VERSION:
            user_choice = messagebox.askyesno("Update Available", 
                f"Version {latest_version} is available! Download it?")
            
            if user_choice:
                # Overwrite this script file with the new code
                urllib.request.urlretrieve(UPDATE_URL, sys.argv[0])
                
                messagebox.showinfo("Success", "Updated! Restarting now...")
                # Restart the app
                os.execl(sys.executable, sys.executable, *sys.argv)
    except Exception as e:
        # If no internet or files aren't on GitHub yet, just print and keep going
        print(f"Update check skipped: {e}")

# Run the check immediately
check_for_updates()

# --- 2. MUSIC PLAYER LOGIC ---
winmm = ctypes.windll.winmm

def play_music():
    file_types = [("Audio Files", "*.mp3 *.wav *.wma *.m4a *.mid *.aac")]
    song_path = filedialog.askopenfilename(filetypes=file_types)
    
    if song_path:
        stop_music()
        open_cmd = f'open "{song_path}" type mpegvideo alias my_track'
        winmm.mciSendStringW(open_cmd, None, 0, 0)
        winmm.mciSendStringW("play my_track", None, 0, 0)
        song_name = song_path.split("/")[-1]
        label.config(text=f"Playing: {song_name}")

def stop_music():
    winmm.mciSendStringW("stop my_track", None, 0, 0)
    winmm.mciSendStringW("close my_track", None, 0, 0)
    label.config(text="Music Stopped")

# --- 3. UI SETUP ---
root = tk.Tk()
root.title(f"Music Player Rock Edition v{CURRENT_VERSION}")
root.geometry("400x250")
root.configure(bg="#ff3f3f")

# Icon safety - wrapped in a try/except so it doesn't crash
try:
    my_image = tk.PhotoImage(file=r'C:\Users\bachl\Music\icon.png')
    bigger_icon = my_image.zoom(2, 2)
    root.iconphoto(False, bigger_icon)
except:
    print("Icon file not found, using default.")

label = tk.Label(root, text="Pick any music file! Without poop", fg="white", bg="#3E00B1", font=("Arial", 12), pady=20)
label.pack()

play_btn = tk.Button(root, text="CHOOSE & PLAY", command=play_music, bg="#27ae60", fg="white", width=20, font=("Arial", 10, "bold"))
play_btn.pack(pady=10)

stop_btn = tk.Button(root, text="STOP", command=stop_music, bg="#e74c3c", fg="white", width=20, font=("Arial", 10, "bold"))
stop_btn.pack(pady=10)

root.mainloop()
