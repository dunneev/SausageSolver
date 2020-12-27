#!/usr/bin/python

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Sausage Files", "*.csv"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, newline="") as file:
        window.title(f"Sausage Solver - {filepath}")
        reader = csv.reader(file)

        r = 0
        for row in reader:
            fr_map.columnconfigure(r, weight=1)
            fr_map.rowconfigure(r, weight=1)
            c = 0
            for col in row:
                frame = tk.Frame(
                    master=fr_map,
                    relief=tk.RAISED,
                    borderwidth=1
                )

                # Set propagate to false to prevent frames from wrapping content
                frame.propagate(0)
                frame.grid(row=r, column=c, sticky="nsew")

                label = tk.Label(master=frame, text=col)
                label.pack()

                c += 1
            r += 1
        

def save_file():
    """Save the current file as a new file."""

    filepath = asksaveasfilename(

        defaultextension="txt",
        filetypes=[("Sausage Files", "*.csv"), ("All Files", "*.*")],
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)

    window.title(f"Sausage Solver - {filepath}")



window = tk.Tk()
window.title("Sausage Solver")

# One row, which grows proportionally
window.rowconfigure(0, weight=1, minsize=200)

# The main window has two columns, the first of which has a fixed width,
# and this one, which will grow and shrink proportionally
window.columnconfigure(1, weight=3, minsize=200)

fr_map = tk.Frame(window)
# txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)


fr_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")
fr_map.grid(row=0, column=1, sticky="nesw")


window.mainloop()