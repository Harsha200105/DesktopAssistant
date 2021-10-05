import tkinter as tk


root = tk.Tk()
root.wm_title('Desktop assistant')
speak_button = tk.Button(master=root, text='Speak', command=lambda: pass)


def set_speak_command(command):
    speak_button.configure(command=command)


speak_button.pack()
output_label = tk.Label(master=root, text='')


def display_output(output):
    output_label['text'] = output


output_label.pack()
root.resizable(False, False)
mainloop = root.mainloop
