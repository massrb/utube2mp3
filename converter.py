
import tkinter as tk
from tkinter import filedialog
import subprocess
import yaml
import os

CONFIG = 'config.yml'
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = f"{THIS_DIR}/{CONFIG}"

class MyWindow:
  def __init__(self, win):
    self.win = win
    self.video_label=tk.Label(win, text='YouTube playlist or video')
    self.dir_label=tk.Label(win, text='Output directory')

    self.video_entry=tk.Entry(bd=3)
    self.dir_entry=tk.Entry()

    self.btn_process=tk.Button(win, text='Process')
    self.btn_select_output=tk.Button(win, text='Browse')

    self.video_label.place(x=100, y=50)
    self.dir_label.place(x=100, y=100)

    self.video_entry.place(x=270, y=50)
    self.dir_entry.place(x=270, y=100)
    self.btn_process.place(x=450, y=50)
    self.btn_select_output.place(x=450, y=100)
    self.btn_process.bind('<Button-1>', self.extract)
    self.btn_select_output.bind('<Button-1>', self.select_output)
    self.message = tk.Text(win, height = 5, width = 52)
    # self.message.pack()
    self.message.place(x=100, y=200)
    if os.path.isfile(CONFIG_PATH):
      self.load_config()
    else:
      self.save_config()

  # load configuration file
  def load_config(self):
    with open(CONFIG_PATH) as stream:
      try:
        self.config = yaml.safe_load(stream)
        self.dir_entry.insert(0, self.config['dir_path'])
      except yaml.YAMLError as exc:
        print(exc)
  
  def save_config(self):
    if not hasattr(self, 'config'):
      self.config = dict(dir_path = '')
    with open(CONFIG_PATH, 'w') as outfile:
      yaml.dump(self.config, outfile, default_flow_style=False)  

  # set output directory for mp3 files
  def select_output(self, event):
    self.dirname = filedialog.askdirectory()
    self.dir_entry.insert(0, self.dirname)
    self.config['dir_path'] = self.dirname
    self.save_config()

  def extract(self, event):
    url=self.video_entry.get()
    output_dir = self.config['dir_path']
    print('URL:' + url)
    self.message.delete('1.0', tk.END)
    self.message.insert(1.0, 'extracted mp3 from video')

    command = f"cd /tmp/tracks; rm *.mp3; yt-dlp  -x --audio-format mp3 '{url}'"
    print('Run: ' + command)
    ret = subprocess.run(command, capture_output=True, shell=True)
    print(ret.stdout.decode())

window=tk.Tk()
mywin=MyWindow(window)
window.title('Convert YouTube to MP3')
window.geometry("=600x300+10+10")
window.mainloop()