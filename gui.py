import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntrys


def show_process_selection_window():
    global root
    root.withdraw()  # Ocultar la ventana principal
    process_selection_window = tk.Toplevel(root)
    process_selection_window.title("Selección de Proceso")
    
    def execute_process1():
        messagebox.showinfo("Proceso 1", "Ejecutando Proceso 1")
    
    def execute_process2():
        messagebox.showinfo("Proceso 2", "Ejecutando Proceso 2")
    
    # Botones para seleccionar los procesos
    button_process1 = tk.Button(process_selection_window, text="Proceso 1", command=execute_process1)
    button_process1.pack(pady=10)
    button_process2 = tk.Button(process_selection_window, text="Proceso 2", command=execute_process2)
    button_process2.pack(pady=10)
    
    # Manejador del evento "Cerrar Ventana"
    def on_process_selection_window_close():
        root.deiconify()  # Volver a mostrar la ventana principal
        process_selection_window.destroy()
    
    process_selection_window.protocol("WM_DELETE_WINDOW", on_process_selection_window_close)


def submit_credentials():
    username = entry_username.get()
    password = entry_password.get()
    selected_date = calendar.get_date()
    
    if not username or not password or not selected_date:
        messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos.")
    else:
        messagebox.showinfo("Datos ingresados", f"Usuario: {username}\nContraseña: {password}\nFecha: {selected_date}")
        show_process_selection_window()


# Crear la ventana principal
root = tk.Tk()
root.title("Ingreso de Datos")

# Etiquetas y campos de entrada
label_username = tk.Label(root, text="Usuario:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

label_date = tk.Label(root, text="Fecha:")
label_date.pack()
calendar = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
calendar.pack(pady=5)

# Botón de envío
button_submit = tk.Button(root, text="Enviar", command=submit_credentials)
button_submit.pack(pady=10)

root.mainloop()