import tkinter as tk

root = tk.Tk()
main_frame = tk.Frame(master=root)
chat_listbox = tk.Listbox(master=main_frame, height=200, width=50)
scroll_bar = tk.Scrollbar(master=main_frame)
speak_button = tk.Button(master=root, text='Speak', command=lambda: None)


def set_speak_command(command):
    speak_button.configure(command=command)


speak_button.pack(side=tk.LEFT, anchor=tk.SW)


def speak(text):
    chat_listbox.insert('end', f'Assistant: {text}')


scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
chat_listbox.pack(fill=tk.Y, side=tk.RIGHT)
scroll_bar.configure(command=chat_listbox.yview)
chat_listbox.configure(yscrollcommand=scroll_bar.set)
main_frame.pack(fill=tk.BOTH)
root.geometry('700x500')
root.minsize(700, 500)
root.wm_title('Desktop assistant')
root.resizable(False, True)
mainloop = root.mainloop
