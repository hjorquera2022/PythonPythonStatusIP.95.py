import os
import socket
import time
import tkinter as tk

# Función para obtener el estado de la dirección IP
def get_status(ip):
    try:
        # Intenta conectarse al puerto 80 de la dirección IP
        socket.create_connection((ip, 80), timeout=1)
        return "VERDE"
    except:
        # Si no se puede conectar, intenta hacer ping a la dirección IP
        response = os.system("ping -c 1 " + ip)
        if response == 0:
            return "AMARILLO"
        else:
            return "ROJO"

# Configuración de la ventana de la aplicación
root = tk.Tk()
root.title("Tablero de control")
root.geometry("300x600")

# Creación de los widgets para las luces
ip_labels = []
status_labels = []

for i, ip in enumerate(["1.82 - 14", "1.83 - 10", "0.85 - 01", "0.86 - RE", "0.87 - 07","0.89 - 15","0.92 - 11","0.95 - 13","0.143 - 15","0.84 - 06"]):
    # Label para mostrar la dirección IP
    ip_label = tk.Label(root, text=f"IP {ip}", font=("Arial", 12))
    ip_label.grid(row=i, column=0, padx=10, pady=10)
    ip_labels.append(ip_label)
    
    # Label para mostrar el estado de la dirección IP
    status_label = tk.Label(root, bg="white", width=5, height=2)
    status_label.grid(row=i, column=1, padx=10, pady=10)
    status_labels.append(status_label)

# Ciclo principal de la aplicación
while True:
    for i, ip in enumerate(["10.55.1.82", "10.55.1.83", "10.55.0.85", "10.55.0.86", "10.55.0.87", "10.55.0.89","10.55.0.92","10.55.0.95","10.55.0.143","10.55.0.84"]):
        # Obtención del estado de la dirección IP
        status = get_status(ip)

        # Cambio del color de las luces según el estado
        if status == "ROJO":
            status_labels[i].config(bg="red")
        elif status == "AMARILLO":
            status_labels[i].config(bg="yellow")
        elif status == "VERDE":
            status_labels[i].config(bg="green")

    # Actualización de la ventana y espera de 5 segundos
    root.update()
    time.sleep(5)