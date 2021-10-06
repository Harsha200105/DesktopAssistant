import tkinter as tk
from tkscrolledframe import ScrolledFrame

root = tk.Tk()
scrolled_frame = ScrolledFrame(master=root)
main_frame = scrolled_frame.display_widget(tk.Frame)
speak_button = tk.Button(master=root, text='Speak', command=lambda: None)


def set_speak_command(command):
    speak_button.configure(command=command)


speak_button.pack(side=tk.LEFT, anchor=tk.SW)


def conversation_label(text):
    tk.Label(master=main_frame, text=text).pack()


def speak(text):
    conversation_label(f'Assistant: {text}')


scrolled_frame.pack(fill=tk.BOTH)
root.wm_title('Desktop assistant')
root.resizable(False, False)
mainloop = root.mainloop
