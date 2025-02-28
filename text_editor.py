import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text.delete(1.0, tk.END)
    status_label.config(text="New file created")

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())
        status_label.config(text=f"Opened: {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully!")
        status_label.config(text=f"Saved: {file_path}")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")
root.config(bg="#f4f4f4")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app)

root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())

text = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), fg="black", bg="#f0f0f0", relief="solid", bd=2)
text.pack(expand=tk.YES, fill=tk.BOTH, padx=10, pady=10)

status_bar = tk.Frame(root, bg="#333", height=20)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

status_label = tk.Label(status_bar, text="Welcome to the Text Editor!", fg="white", bg="#333", anchor="w", padx=10)
status_label.pack(fill=tk.X)

root.mainloop()
