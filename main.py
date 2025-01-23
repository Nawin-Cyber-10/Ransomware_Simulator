import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import os
import time
import threading

# Simulated encryption and decryption functions
def encrypt_folder(folder_path):
    """Simulate file encryption by changing file extensions to '.locked'"""
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                encrypted_file_path = file_path + ".locked"
                os.rename(file_path, encrypted_file_path)
        # Simulating creation of a ransom note
        ransom_note = os.path.join(folder_path, "readme.txt")
        with open(ransom_note, "w") as note:
            note.write("Your files have been encrypted. Pay the ransom to decrypt them!")
        return True
    except Exception as e:
        print(f"Error during encryption: {e}")
        return False

def decrypt_folder(folder_path):
    """Simulate file decryption by changing '.locked' extensions back to original."""
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".locked"):
                    file_path = os.path.join(root, file)
                    decrypted_file_path = file_path.replace(".locked", "")
                    os.rename(file_path, decrypted_file_path)
        # Create a safety note after decryption
        safety_note = os.path.join(folder_path, "safety_note.txt")
        with open(safety_note, "w") as note:
            note.write("Stay safe! Do not click suspicious files or links. Install good antivirus software.")
        return True
    except Exception as e:
        print(f"Error during decryption: {e}")
        return False

# Function to open the "Learn My Lesson" window
def open_learn_my_lesson():
    learn_window = tk.Toplevel()
    learn_window.title("Learn My Lesson")
    learn_window.geometry("600x400")
    learn_window.configure(bg="#2c3e50")

    # Display game file icon and simulate file execution
    game_icon = Image.open("assets/gta6_cracked.png")
    game_icon = game_icon.resize((100, 100), Image.Resampling.LANCZOS)
    game_icon = ImageTk.PhotoImage(game_icon)

    game_button = tk.Button(learn_window, image=game_icon, text="GTA 6 Cracked", compound="top", font=("Arial", 14),
                            bg="#34495e", fg="#ecf0f1", command=lambda: show_defender_popup(game_button))
    game_button.image = game_icon  # Keep a reference to prevent garbage collection
    game_button.pack(pady=50)

    learn_window.mainloop()

# Function to show Windows Defender-like pop-up
def show_defender_popup(game_button):
    defender_popup = tk.Toplevel()
    defender_popup.title("Windows Defender")
    defender_popup.geometry("400x250")
    defender_popup.configure(bg="#2c3e50")

    defender_image = Image.open("assets/windows_defender.png")
    defender_image = defender_image.resize((50, 50), Image.Resampling.LANCZOS)
    defender_icon = ImageTk.PhotoImage(defender_image)

    defender_label = tk.Label(defender_popup, image=defender_icon, text="Potential Risk Detected!",
                              font=("Arial", 16), fg="#ecf0f1", bg="#2c3e50")
    defender_label.image = defender_icon
    defender_label.pack(pady=20)

    warning_label = tk.Label(defender_popup, text="Please do not execute this file.\nClick 'Ignore' to continue or 'Turn Off Protection' to disable.",
                             font=("Arial", 12), fg="#ecf0f1", bg="#2c3e50")
    warning_label.pack(pady=20)

    def on_ignore():
        defender_popup.destroy()

    def on_turn_off():
        defender_popup.destroy()
        open_installation_window()

    ignore_button = tk.Button(defender_popup, text="Ignore This", command=on_ignore, font=("Arial", 12), bg="#e74c3c", fg="#ecf0f1")
    ignore_button.pack(side="left", padx=30, pady=10)

    turn_off_button = tk.Button(defender_popup, text="Turn Off Protection", command=on_turn_off, font=("Arial", 12), bg="#e74c3c", fg="#ecf0f1")
    turn_off_button.pack(side="right", padx=30, pady=10)

    defender_popup.mainloop()

# Function to open the "I Have Learned My Lesson" window
def open_i_have_learnt_my_lesson():
    lesson_window = tk.Toplevel()
    lesson_window.title("I Have Learned My Lesson")
    lesson_window.geometry("600x400")
    lesson_window.configure(bg="#2c3e50")

    awareness_label = tk.Label(lesson_window, text="Awareness: Please agree to the terms to proceed.",
                               font=("Arial", 14), fg="#ecf0f1", bg="#2c3e50")
    awareness_label.pack(pady=20)

    def on_agree():
        # When the user agrees, the 'Agree' button changes to 'Save Me'
        agree_button.config(state="disabled")
        save_me_button.pack(pady=20)

    agree_button = tk.Button(lesson_window, text="Agree", command=on_agree, font=("Arial", 14), bg="#e74c3c", fg="#ecf0f1")
    agree_button.pack(pady=50)

    def on_proceed():
        folder_path = filedialog.askdirectory(title="Select Folder with Encrypted Files")
        if folder_path:
            decrypt_folder(folder_path)
            messagebox.showinfo("Decryption Complete", "Your files have been decrypted!\nSafety precautions have been saved.")

    save_me_button = tk.Button(lesson_window, text="Proceed to Save Me", command=on_proceed, font=("Arial", 14), bg="#2ecc71", fg="#ecf0f1")
    save_me_button.pack_forget()  # Initially hide the button until 'Agree' is clicked

    lesson_window.mainloop()

# Function to open installation window for folder selection and encryption
def open_installation_window():
    install_window = tk.Toplevel()
    install_window.title("Install GTA 6 Cracked")
    install_window.geometry("600x400")
    install_window.configure(bg="#2c3e50")

    install_label = tk.Label(install_window, text="Select Installation Location for GTA 6 Cracked",
                             font=("Arial", 14), fg="#ecf0f1", bg="#2c3e50")
    install_label.pack(pady=20)

    def on_select_folder():
        folder_path = filedialog.askdirectory(title="Select Folder for Installation")
        if folder_path:
            # Creating a progress bar
            progress_label = tk.Label(install_window, text="Installing...", font=("Arial", 14), fg="#ecf0f1", bg="#2c3e50")
            progress_label.pack(pady=10)

            progress = Progressbar(install_window, length=400, mode="determinate", maximum=100, value=0)
            progress.pack(pady=10)

            install_window.update_idletasks()

            # Simulating file encryption process
            for i in range(101):
                time.sleep(0.05)
                progress["value"] = i
                install_window.update_idletasks()

            encryption_thread = threading.Thread(target=encrypt_folder, args=(folder_path,))
            encryption_thread.start()
            encryption_thread.join()

            messagebox.showinfo("Installation Complete", "Installation complete. Your files have been encrypted.")

    select_folder_button = tk.Button(install_window, text="Select Folder", command=on_select_folder, font=("Arial", 14), bg="#e74c3c", fg="#ecf0f1")
    select_folder_button.pack(pady=50)

    install_window.mainloop()

# Main window
def main_window():
    root = tk.Tk()
    root.title("Ransomware Simulator")
    root.geometry("800x600")
    root.configure(bg="#2c3e50")

    # Main logo for the window
    logo_image = Image.open("assets/ransomware_logo.png")
    logo_image = logo_image.resize((200, 200), Image.Resampling.LANCZOS)
    logo_image = ImageTk.PhotoImage(logo_image)

    logo_label = tk.Label(root, image=logo_image, bg="#2c3e50")
    logo_label.image = logo_image  # Keep a reference to prevent garbage collection
    logo_label.pack(pady=50)

    # Buttons to open respective windows
    learn_button = tk.Button(root, text="Learn My Lesson", command=open_learn_my_lesson, font=("Arial", 14), bg="#e74c3c", fg="#ecf0f1")
    learn_button.pack(pady=20)

    lesson_button = tk.Button(root, text="I Have Learned My Lesson", command=open_i_have_learnt_my_lesson, font=("Arial", 14), bg="#2ecc71", fg="#ecf0f1")
    lesson_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_window()
