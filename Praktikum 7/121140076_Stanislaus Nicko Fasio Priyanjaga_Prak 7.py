import tkinter as tk
import random

class TebakAngkaGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tebak Angka")

        self.target = random.randint(1, 100)
        self.tries = 0

        self.label = tk.Label(master, text="Tebak angka dari 1-100")
        self.label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.button = tk.Button(master, text="Tebak", command=self.tebak)
        self.button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

    def tebak(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.result_label.config(text="Masukkan angka yang valid")
            return

        self.tries += 1

        if guess == self.target:
            self.result_label.config(text="Anda benar! Angka yang dicari adalah " + str(self.target) + ". Jumlah tebakan: " + str(self.tries))
        elif guess < self.target:
            self.result_label.config(text="Terlalu kecil, coba lagi")
        else:
            self.result_label.config(text="Terlalu besar, coba lagi")

    def reset(self):
        self.target = random.randint(1, 100)
        self.tries = 0
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)

root = tk.Tk()
tebak_angka_gui = TebakAngkaGUI(root)
root.mainloop()
