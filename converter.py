
import tkinter as tk
import subprocess

class MyWindow:
    def __init__(self, win):
        self.video_label=tk.Label(win, text='YouTube playlist or video')
        self.dir_label=tk.Label(win, text='Output directory')

        self.video_entry=tk.Entry(bd=3)
        self.dir_entry=tk.Entry()

        self.btn_process=tk.Button(win, text='Process')

        self.video_label.place(x=100, y=50)
        self.dir_label.place(x=100, y=100)

        self.video_entry.place(x=270, y=50)
        self.dir_entry.place(x=270, y=100)
        self.btn_process.place(x=450, y=50)

        self.btn_process.bind('<Button-1>', self.extract)
        self.message = tk.Text(win, height = 5, width = 52)
        # self.message.pack()
        self.message.place(x=100, y=200)
        
    def extract(self, event):
        url=self.video_entry.get()
        print('URL:' + url)
        self.message.delete('1.0', tk.END)
        # self.message.insert(tk.END, 'this is a message')
        self.message.insert(1.0, 'extracted mp3 from video')

        command = f"cd /tmp/tracks; yt-dlp  -x --audio-format mp3 '{url}'"
        print('Run: ' + command)
        ret = subprocess.run(command, capture_output=True, shell=True)
        print(ret.stdout.decode())
        # root = Tk()
        #win.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        # print (root.filename)

#        process = subprocess.Popen(['echo', 'Hello, World!'], stdout=subprocess.PIPE)
#        output, error = process.communicate()
#        print(output.decode())
        # out, err = process.communicate(commands)

window=tk.Tk()
print('WINDOW')
print(window)
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("=600x300+10+10")
window.mainloop()