import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def ucapan_ulang_tahun():
    nama = entry_nama.get()
    umur = entry_umur.get()
    if not nama or not umur.isdigit():
        messagebox.showerror("Error", "Masukkan nama yang valid dan umur sebagai angka.")
        return
    umur = int(umur)
    pesan = f"Selamat Ulang Tahun, {nama}!\n"
    pesan += f"Semoga di umur yang ke-{umur} ini, kamu selalu diberikan kesehatan, kebahagiaan, dan kesuksesan.\n"
    pesan += "Semoga semua impian dan harapanmu tercapai. Selamat merayakan hari istimewamu!"
    messagebox.showinfo("Ucapan Ulang Tahun", pesan)

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Ucapan Ulang Tahun")
root.geometry("500x500")
root.configure(bg='#f0f8ff')

# Menambahkan gambar kue ulang tahun
image = Image.open("cake.png")
image = image.resize((200, 200), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=photo, bg='#f0f8ff')
label_image.pack(pady=10)

# Menambahkan teks "Happy Birthday"
label_happy_birthday = tk.Label(root, text="Happy Birthday!", font=("Helvetica", 20, 'bold'), bg='#f0f8ff', fg='#ff69b4')
label_happy_birthday.pack()

# Membuat frame
frame = tk.Frame(root, bg='#f0f8ff')
frame.pack(pady=20)

# Membuat dan menempatkan label dan entry untuk nama
label_nama = tk.Label(frame, text="Nama:", font=("Helvetica", 12), bg='#f0f8ff')
label_nama.grid(row=0, column=0, padx=10, pady=10, sticky='w')
entry_nama = tk.Entry(frame, font=("Helvetica", 12))
entry_nama.grid(row=0, column=1, padx=10, pady=10)

# Membuat dan menempatkan label dan entry untuk umur
label_umur = tk.Label(frame, text="Umur:", font=("Helvetica", 12), bg='#f0f8ff')
label_umur.grid(row=1, column=0, padx=10, pady=10, sticky='w')
entry_umur = tk.Entry(frame, font=("Helvetica", 12))
entry_umur.grid(row=1, column=1, padx=10, pady=10)

# Membuat dan menempatkan tombol untuk mengucapkan ulang tahun
button = tk.Button(root, text="Ucapan Ulang Tahun", font=("Helvetica", 12, 'bold'), bg='#00bfff', fg='white', command=ucapan_ulang_tahun)
button.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
