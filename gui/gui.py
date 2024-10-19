import tkinter as tk
from tkinter import ttk, messagebox
import os
import json

from util.methods import open_main_window, path_open


class ScrollableFrame:
    def __init__(self, window):
        self.canvas = tk.Canvas(window)
        scrollbar = tk.Scrollbar(window, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


class MainWindow:

    def __init__(self, path):
        self.window = tk.Tk()
        self.window.title('Renamer')
        self.window.geometry('800x500')
        self.window.resizable(False, False)
        self.path = path
        self.file = self.get_file()
        self.citizens = self.get_citizens()
        self.get_citizens_table()
        self.id_to_index = {citizen['humanID']: index for index, citizen in enumerate(self.citizens)}

        save_button = tk.Button(self.window, text="SAVE", command=self.save, bg='green', fg='white', width=15, height=2)
        save_button.pack(side="bottom", pady=10)

    def get_file(self):
        file = path_open(self.path)
        return json.loads(file)

    def get_citizens(self):
        return self.file.get('citizens')

    def get_citizens_table(self):
        scrollable_frame = ScrollableFrame(self.window)
        for index, cit in enumerate(self.get_citizens()):
            frame = tk.Frame(scrollable_frame.scrollable_frame, relief="groove", borderwidth=2)
            frame.grid(row=index // 2, column=index % 2, padx=10, pady=10, sticky="nsew")  # Add padding

            label1 = tk.Label(frame, text=f'humanID: {cit["humanID"]}', anchor="w")
            label1.grid(row=0, column=0, sticky="w")  # Align to the left
            label2 = tk.Label(frame, text=f'Name: {cit["citizenName"]}', anchor="w")
            label2.grid(row=1, column=0, sticky="w")
            label3 = tk.Label(frame, text=f'Casual Name: {cit["casualName"] if cit["casualName"] else "[empty]"}',
                              anchor="w")
            label3.grid(row=2, column=0, sticky="w")

            entry_name = tk.Entry(frame)
            entry_name.grid(row=1, column=1, sticky="ew")
            entry_cas_name = tk.Entry(frame)
            entry_cas_name.grid(row=2, column=1, sticky="ew")

            button = tk.Button(
                frame,
                text="Rename",
                command=lambda n=entry_name, cn=entry_cas_name, hm=cit["humanID"], l2=label2, l3=label3: self.submit_action(n, cn, hm, l2, l3),
                bg='#ADD8E6',
                fg='black'
            )
            button.grid(row=3, column=0, columnspan=2, sticky="ew", pady=10)

        scrollable_frame.canvas.configure(scrollregion=scrollable_frame.canvas.bbox("all"))

    def submit_action(self, entry_name, entry_cas_name, human_id, label_name, label_casual_name):
        name = entry_name.get()
        casual_name = entry_cas_name.get()

        self.rename(name, human_id, casual_name)

        label_name.config(text=f'Name: {name}')
        label_casual_name.config(text=f'Casual Name: {casual_name if casual_name else "[empty]"}')

    def rename(self, name, human_id, casual_name=''):
        first_name, sur_name = self.split_name(name)
        try:
            if name:
                self.file["citizens"][self.id_to_index[human_id]]['citizenName'] = name
                self.file["citizens"][self.id_to_index[human_id]]['firstName'] = first_name
                self.file["citizens"][self.id_to_index[human_id]]['surName'] = sur_name
            if casual_name:
                self.file["citizens"]['casualName'] = casual_name
        except KeyError:
            messagebox.showerror("Error", "Чет не получилось и я хз")

    def save(self):
        try:
            base_path, original_name = os.path.split(self.path)
            file_name, ext = os.path.splitext(original_name)
            project_folder = os.getcwd()
            new_path = os.path.join(project_folder, f"{file_name}.cit")
            data = self.file
            serialized_data = json.dumps(data)

            with open(new_path, 'w', encoding='utf-8') as outfile:
                outfile.write(serialized_data)

            messagebox.showinfo("Save", f"Changes saved successfully to {new_path}!")
        except Exception as e:
            print("Error", f"Failed to save file: {e}")
            messagebox.showerror("Error", f"Failed to save file: {e}")

    @staticmethod
    def split_name(name):
        return name.split(' ')


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
