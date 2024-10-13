import tkinter as tk
from tkinter import ttk, messagebox
import os
import json

from util.methods import open_main_window, path_open


class MainWindow:

    def __init__(self, path):
        self.window = tk.Tk()
        self.window.title('lol')
        self.window.geometry('500x500')
        self.path = path
        self.file = self.get_file()
        self.citizens = self.get_citizens()
        # TODO: citizens - список, поэтому можно будет просто по нему пройтись
        # насчет сохранения и изменения пока не знаю, надо как то пересобирать файл в нужный формат

    def get_file(self):
        file = path_open(self.path)
        return json.loads(file)

    def get_citizens(self):
        return self.file.get('citizens')


class OpenerClass:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Opener')
        self.root.geometry('200x100')
        self.init_path_opener()

    def init_path_opener(self):
        label = tk.Label(self.root, text='Path')
        label.pack(anchor='nw', padx=5, pady=5)

        path_entry = tk.Entry(self.root)
        path_entry.pack(anchor='nw', padx=5, pady=5)

        open_btn = ttk.Button(
            text='OPEN',
            command=lambda child=MainWindow, entry=path_entry: self.check_and_open(child, entry))
        open_btn.pack(anchor='nw', padx=5, pady=5)

    def check_and_open(self, child, entry):
        path = entry.get().strip()
        if path and os.path.isfile(path):
            open_main_window(self.root, child, path)
        else:
            messagebox.showerror("Error", f"Could not find file: {path}")


opener = OpenerClass()
