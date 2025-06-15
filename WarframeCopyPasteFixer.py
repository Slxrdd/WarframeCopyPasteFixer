import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import webbrowser
from pynput.keyboard import Controller
import pyperclip
import threading
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
import keyboard

keyboard_controller = Controller()

class WarframeFixerApp:
    def __init__(self, root):
        self.root = root
        root.title("Warframe CopyPaste Fixer")
        root.geometry("800x600")
        root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = None
        self.set_background_image("https://i.ibb.co/bDSp3L9/dark-purple-anime-da6r86bm71p5y9iz.jpg")

        self.canvas.create_text(400, 60, text="Warframe Fixer", font=("Consolas", 36, "bold"),
                                fill="#d2a1f7")

        self.log = ScrolledText(root, font=("Consolas", 14), fg="white", bg="#7e3ac1", bd=0)
        self.log.place(relx=0.5, rely=0.7, anchor="center", width=750, height=120)

        label_font = ("Arial", 12)
        start_y = 140
        spacing_y = 40
        label_x = 180
        entry_x = 495
        entry_width = 10

        self.canvas.create_text(label_x, start_y, text="Touche pour le message de remerciement :",
                                fill="white", font=label_font, anchor="w")
        self.entry_thank = ttk.Entry(root, width=entry_width)
        self.entry_thank.place(x=entry_x, y=start_y - 12)
        self.entry_thank.insert(0, "-")

        self.canvas.create_text(label_x, start_y + spacing_y, text="Touche pour coller le contenu presse-papier :",
                                fill="white", font=label_font, anchor="w")
        self.entry_clip = ttk.Entry(root, width=entry_width)
        self.entry_clip.place(x=entry_x, y=start_y + spacing_y - 12)
        self.entry_clip.insert(0, "8")

        self.btn_apply = ttk.Button(root, text="Appliquer", command=self.update_hotkeys)
        self.btn_apply.place(relx=0.5, y=230, anchor="center", width=120, height=30)

        self.btn_reseaux = ttk.Button(root, text="Mes réseaux", command=self.open_website)
        self.btn_reseaux.place(relx=0.5, y=270, anchor="center", width=120, height=30)

        self.canvas.create_text(400, 550, text="Made by Slxrdd", font=("Arial", 10, "italic"),
                                fill="white")

        self.registered_hotkeys = []
        self.thank_key = self.entry_thank.get().strip()
        self.clip_key = self.entry_clip.get().strip()

        threading.Thread(target=self.monitor_keys, daemon=True).start()

    def set_background_image(self, url):
        try:
            with urlopen(url) as u:
                raw_data = u.read()
            im = Image.open(io.BytesIO(raw_data))
            im = im.resize((800, 600))
            self.bg_image = ImageTk.PhotoImage(im)
            self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        except Exception as e:
            self.log_message(f"Erreur chargement image de fond : {e}")

    def log_message(self, message):
        self.log.insert(tk.END, message + "\n")
        self.log.see(tk.END)

    def open_website(self):
        webbrowser.open("https://guns.lol/slxrdd")

    def send_fixed_message(self):
        fixed_message_base = ("Thank you for your purchase! Have a great evening/day and a good game with your purchase. "
                              "If you can put a review on WFM , I'll do it for you too <3")
        keyboard_controller.type(fixed_message_base)

    def send_clipboard(self):
        text = pyperclip.paste()
        keyboard_controller.type(text)

    def clear_hotkeys(self):
        for handler in self.registered_hotkeys:
            keyboard.remove_hotkey(handler)
        self.registered_hotkeys.clear()

    def register_hotkeys(self):
        self.clear_hotkeys()
        thank_key = self.entry_thank.get().strip()
        clip_key = self.entry_clip.get().strip()

        if thank_key:
            handler = keyboard.add_hotkey(thank_key, self.on_thank_pressed, suppress=True)
            self.registered_hotkeys.append(handler)
            self.log_message(f"Raccourci 'Merci' assigné à la touche : {thank_key}")
        if clip_key:
            handler = keyboard.add_hotkey(clip_key, self.on_clip_pressed, suppress=True)
            self.registered_hotkeys.append(handler)
            self.log_message(f"Raccourci 'Coller' assigné à la touche : {clip_key}")

        self.thank_key = thank_key
        self.clip_key = clip_key

    def update_hotkeys(self):
        thank = self.entry_thank.get().strip()
        clip = self.entry_clip.get().strip()
        if thank == "" or clip == "":
            self.log_message("Erreur : les touches ne peuvent pas être vides.")
            return
        self.register_hotkeys()
        self.log_message(f"Raccourcis mis à jour : Merci -> '{thank}', Coller -> '{clip}'")

    def on_thank_pressed(self):
        self.log_message(f"Touche '{self.thank_key}' détectée : envoi message remerciement")
        self.send_fixed_message()

    def on_clip_pressed(self):
        self.log_message(f"Touche '{self.clip_key}' détectée : envoi contenu presse-papier")
        self.send_clipboard()

    def monitor_keys(self):
        import time
        while True:
            time.sleep(1)

# Coucou toi qui a voulu décompiler le exe, tu as réussi soit heureux (même si je n'ai pas caché celui-ci mais bref, si tu es Dantes je m'en doutais si tu es quelqu'un d'autre.... Je sais pas ce que tu fou là mais bon toute façon tu ne pourra pas resell un script aussi bidon)

def main():
    root = tk.Tk()
    app = WarframeFixerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
