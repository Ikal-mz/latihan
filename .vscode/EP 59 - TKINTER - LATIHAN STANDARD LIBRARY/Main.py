# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="gray")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa Dia!")

# variabel dan fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()

def tombol_click():
    tombol = f"Hello {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}, Mantap"
    showinfo(message=tombol)

# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen-komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. entri nama depan
nama_depan_entri = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entri.pack(padx=10,fill="x",expand=True)
# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entri nama belakang
nama_belakang_entri = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entri.pack(padx=10,fill="x",expand=True)
# 5. tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10)

# main loop window
window.mainloop()


