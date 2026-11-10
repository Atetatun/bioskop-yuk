import tkinter as tk
from tkinter import messagebox

class BioskopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bioskop Yuk! - UTS Pemrograman Dasar")
        self.root.geometry("600x500")
        self.root.configure(bg="#ffe4e1") # Soft pink theme

        # 1. Tipe Data & Variable (Ita)
        self.judul_label = tk.Label(root, text="🎟️ APLIKASI TIKET BIOSKOP 🎟️", font=("Arial", 16, "bold"), bg="#ffe4e1", fg="#d1477a")
        self.judul_label.pack(pady=20)

        # 2. List & Tuple / Katalog Film (Repa)
        self.daftar_film = [
            ("Avatar 3: Fire & Ash", 45000),
            ("Avengers: Secret Wars", 50000),
            ("Pengabdi Setan 3", 40000),
            ("Agak Laen 2", 35000)
        ]
        
        self.label_info = tk.Label(root, text="Silakan pilih film dan kursi pesanan Anda di bawah:", font=("Arial", 10), bg="#ffe4e1")
        self.label_info.pack(pady=10)

        # Frame untuk Konten (Viron, Apriyanti, Shireen)
        self.frame_konten = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
        self.frame_konten.pack(pady=10, fill="both", expand=True, padx=20)

        self.btn_keluar = tk.Button(root, text="Keluar", command=root.quit, bg="#ff69b4", fg="white", font=("Arial", 10, "bold"))
        self.btn_keluar.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BioskopApp(root)
    root.mainloop()
