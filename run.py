import tkinter as tk
from tkinter import filedialog
from functions import extract_embedded_files
import os
import glob

folder_path = os.path.expanduser('~') + '/Downloads'

class PDFtoXMLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XML Extractor for E-Invoices")
        self.create_widgets()
        self.refresh_files()

    def create_widgets(self):
        self.select_button = tk.Button(self.root, text="Change Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.file_listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE)
        self.file_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        self.extract_button = tk.Button(self.root, text="Extract Embedded Files", command=self.extract_files)
        self.extract_button.pack(pady=10)

    def select_folder(self):
        global folder_path; folder_path = filedialog.askdirectory()
        print(folder_path)
        if folder_path:
            self.refresh_files()

    def extract_files(self):
        selected_files = self.file_listbox.curselection()
        for i in selected_files:
            pdf_path = self.file_listbox.get(i)
            extract_embedded_files(pdf_path)
            os.rename(pdf_path, pdf_path.replace('.pdf', '') + '/' + pdf_path.split('\\')[-1])
            self.refresh_files()

    def refresh_files(self):
        self.file_listbox.delete(0, tk.END)
        pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
        pdf_files.sort(key=os.path.getctime, reverse=True)
        for pdf_file in pdf_files:
            self.file_listbox.insert(tk.END, pdf_file)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = PDFtoXMLApp(root)
    root.mainloop()