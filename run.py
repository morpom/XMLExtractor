import tkinter as tk
from tkinter import filedialog
from functions import extract_embedded_files
import os
import glob

folder_path = os.path.expanduser('~') + '/Downloads'

class XMLExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("XML Extractor for E-Invoices")
        self.move_pdf = tk.BooleanVar()
        self.show_summary = tk.BooleanVar()
        self.create_widgets()
        self.refresh_files()

    def create_widgets(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.refresh_button = tk.Button(self.button_frame, text="Refresh Files", command=self.refresh_files)
        self.refresh_button.pack(side=tk.LEFT)
    
        self.select_button = tk.Button(self.button_frame, text="Change Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.show_summary_button = tk.Checkbutton(self.button_frame, text="Show Summary", variable=self.show_summary)
        self.show_summary_button.pack(pady=10)

        self.move_pdf_checkbutton = tk.Checkbutton(self.button_frame, text="Move PDFs to Subfolders", variable=self.move_pdf)
        self.move_pdf_checkbutton.pack(side=tk.RIGHT)

        self.file_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.file_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.extract_button = tk.Button(self.root, text="Extract Embedded Files", command=self.extract_files)
        self.extract_button.pack(pady=10)

    def select_folder(self):
        global folder_path; folder_path = filedialog.askdirectory()
        if folder_path:
            self.refresh_files()

    def extract_files(self):
        log = "The following files were extracted:\n"
        pdf_with_embedded_files = {}
        selected_files = self.file_listbox.curselection()
        for i in selected_files:
            pdf_path = self.file_listbox.get(i)
            pdf_with_embedded_files[os.path.basename(pdf_path)] = extract_embedded_files(pdf_path)
            if self.move_pdf.get():
                subfolder = os.path.splitext(pdf_path)[0]
                os.rename(pdf_path, os.path.join(subfolder, os.path.basename(pdf_path)))
        self.refresh_files()
        for pdf, files in pdf_with_embedded_files.items():
            log += "\n" + pdf + ":\n"
            for file in files:
                log += " ┕╸" + file + "\n"
        if self.show_summary.get():
            self.show_message(log)

    def refresh_files(self):
        self.file_listbox.delete(0, tk.END)
        pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
        pdf_files.sort(key=os.path.getctime, reverse=True)
        for pdf_file in pdf_files:
            self.file_listbox.insert(tk.END, pdf_file)

    def show_message(self, message):
        print('showing message')
        message_box = tk.Toplevel()
        message_box.title("Extraction Summary")
        message_box.geometry("600x200")
        message_label = tk.Label(message_box, text=message, justify="left")
        message_label.pack(pady=10)
        ok_button = tk.Button(message_box, text="OK", command=message_box.destroy)
        ok_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = XMLExtractor(root)
    root.mainloop()