import tkinter as tk
from datetime import datetime
import pytz

paises = {
    "América - Nueva York": "America/New_York",
    "América - Buenos Aires": "America/Argentina/Buenos_Aires",
    "Europa - Londres": "Europe/London",
    "Europa - Berlín": "Europe/Berlin",
    "Asia - Tokio": "Asia/Tokyo",
    "Asia - Dubái": "Asia/Dubai",
    "África - El Cairo": "Africa/Cairo",
    "África - Johannesburgo": "Africa/Johannesburg",
    "Oceanía - Sídney": "Australia/Sydney",
    "Oceanía - Wellington": "Pacific/Auckland",
    "Antártida - Palmer": "Antarctica/Palmer",
    "Antártida - Rothera": "Antarctica/Rothera"
}


root = tk.Tk()
root.title("Reloj Mundial")
root.geometry("500x400")
root.config(bg="black")


tk.Label(root, text="🌍 Reloj Mundial", font=("Helvetica", 20, "bold"), fg="white", bg="black").pack(pady=10)

labels = {}

for city in paises:
    frame = tk.Frame(root, bg="black")
    frame.pack(pady=2)
    city_label = tk.Label(frame, text=city, width=25, anchor="w", fg="cyan", bg="black", font=("Consolas", 12))
    time_label = tk.Label(frame, text="", width=20, anchor="e", fg="white", bg="black", font=("Consolas", 12))
    city_label.pack(side="left")
    time_label.pack(side="right")
    labels[city] = time_label


def update_time():
    for city, tz in paises.items():
        timezone = pytz.timezone(tz)
        time = datetime.now(timezone).strftime('%H:%M:%S')
        labels[city].config(text=time)
    root.after(1000, update_time)


update_time()


root.mainloop()
