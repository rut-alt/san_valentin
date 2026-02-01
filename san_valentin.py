import tkinter as tk
import random

# Ventana principal
root = tk.Tk()
root.title("💘 San Valentín 💘")
root.geometry("800x500")
root.configure(bg="#ffe6f0")

# Texto principal
label = tk.Label(
    root,
    text="Hola Jorge mi amor, ¿Quieres una cita conmigo el 14 de febrero? 💖",
    font=("Helvetica", 24, "bold"),
    bg="#ffe6f0",
    fg="#cc0052",
    wraplength=700
)
label.pack(pady=40)

# Función cuando dice que SÍ
def yes_clicked():
    for widget in root.winfo_children():
        widget.destroy()

    final_label = tk.Label(
        root,
        text="🥰 Sabía que dirías que sí 🥰\n\nPrepárate para una cita inolvidable 💕",
        font=("Helvetica", 26, "bold"),
        bg="#ffe6f0",
        fg="#990033",
        wraplength=700
    )
    final_label.pack(expand=True)

# Botón SÍ (grande y visible)
yes_button = tk.Button(
    root,
    text="SÍ 💘",
    font=("Helvetica", 30, "bold"),
    bg="#ff4d88",
    fg="white",
    activebackground="#ff1a66",
    padx=40,
    pady=20,
    command=yes_clicked,
    borderwidth=0
)
yes_button.pack(pady=20)

# Botón NO (escapista profesional)
no_button = tk.Button(
    root,
    text="NO 🙄",
    font=("Helvetica", 14),
    bg="#cccccc",
    fg="black"
)
no_button.place(x=350, y=350)

# Función para mover el botón NO
def move_no_button(event):
    x = random.randint(0, root.winfo_width() - 100)
    y = random.randint(0, root.winfo_height() - 50)
    no_button.place(x=x, y=y)

# El botón NO huye cuando el ratón se acerca
no_button.bind("<Enter>", move_no_button)

root.mainloop()
