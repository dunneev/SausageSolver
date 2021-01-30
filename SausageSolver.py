#!/usr/bin/env python3

import tkinter as tk
from Controller import Controller

if __name__ == '__main__':
    window = tk.Tk()
    # window.withdraw()
    app = Controller(window)
    window.mainloop()