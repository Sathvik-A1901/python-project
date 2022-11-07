import threading
import time
import tkinter as tk


class CountdownTimer:
        
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("600x500")
        self.root.title("Timer")
        self.root.config(bg="#000")
        self.root.resizable(False,False)
        
        self.heading=tk.Label(self.root,text="Timer",font="arial 30 bold",bg="#000",fg="#ea3548")
        self.heading.grid(row=0,column=1,columnspan=3,padx=2,pady=5)
        
        self.hour=tk.Label(self.root,text="hours",font="arial 12",bg="#000",fg="#fff")
        self.hour.grid(row=1,column=1,padx=0,pady=5)
        self.minute=tk.Label(self.root,text="min",font="arial 12",bg="#000",fg="#fff")
        self.minute.grid(row=1,column=2,padx=0,pady=5)
        self.secs=tk.Label(self.root,text="sec",font="arial 12",bg="#000",fg="#fff")
        self.secs.grid(row=1,column=3,padx=0,pady=5)
        
        self.time_hours=tk.Entry(self.root,font=('Helvetica',30),width=2)
        self.time_hours.grid(row=2,column=1,padx=1,pady=5)
        
        self.time_minute=tk.Entry(self.root,font=('Helvetica',30),width=2)
        self.time_minute.grid(row=2,column=2,padx=1,pady=5)
        
        self.time_seconds=tk.Entry(self.root,font=('Helvetica',30),width=2)
        self.time_seconds.grid(row=2,column=3,padx=1,pady=5)
        
        self.start_button=tk.Button(self.root,font=("Helvetica",30),text="Start/Resume",command=self.start_thread)
        self.start_button.grid(row=3,column=1,padx=5,pady=5)
        
        self.stop_button=tk.Button(self.root,font=("Helvetica",30),text="Reset",command=self.stop)
        self.stop_button.grid(row=3,column=2,padx=5,pady=5)
        
        self.pause_button =tk.Button(self.root, text='Pause', font=('Helvetica',30), bg="red", fg="white",command=self.pause_time)
        self.pause_button.grid(row=3,column=3,padx=5,pady=5)
        
        self.time_label=tk.Label(self.root,font=("Helvetica",30),text="Time: 00:00:00")
        self.time_label.grid(row=4,column=1,columnspan=3,padx=5,pady=5)
        
        self.resume_time=0
        self.stop_loop=False
        self.pause=False
        
        self.root.mainloop()
        
    
        
    def start_thread(self):
        t=threading.Thread(target=self.start)
        t.start()
        
    def start(self):
        self.stop_loop=False
        self.pause=False
        
        hours, minutes, seconds = 0, 0, 0
        
        if self.time_hours.get():
            hours=self.time_hours.get()
        
        if self.time_minute.get():
            minutes=self.time_minute.get()
        
        if self.time_seconds.get():
            seconds=self.time_seconds.get()
        
        
        
        hours=int(hours)
        minutes=int(minutes)
        seconds=int(seconds)
        
        
        self.full_seconds=hours*3600 +minutes*60+seconds
        if self.resume_time>0:
            self.full_seconds=self.resume_time
        
        while self.full_seconds>0 and not self.stop_loop:
            self.full_seconds-=1
            
            minutes,seconds=divmod(self.full_seconds,60)
            hours,minutes=divmod(minutes,60)
            
            self.time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
            if self.pause == True:
                break
            
    def pause_time(self):
        self.pause = True

        mins, secs = divmod(self.full_seconds, 60)
        hours = 0
        if mins > 60:
            # hour minute
            hours, mins = divmod(mins, 60)
        
        self.resume_time=self.full_seconds

        self.time_label.config(text=f"Time: {hours:02d}:{mins:02d}:{secs:02d}")
        self.time_label.update()
    
    
    
    def stop(self):
        self.stop_loop=True
        self.time_label.config(text="Text: 00:00:00")

CountdownTimer()
        
