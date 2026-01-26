# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 19:53:13 2026

@author: k
"""

# -*- coding: utf-8 -*-
#pip install numpy scipy matplotlib
#pip install pipwin
#pipwin install pyaudio

import pyaudio
import numpy as np
import tkinter as tk
from scipy.fft import fft, fftfreq

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ================= CONFIG =================
FS = 44100
CHUNK = 4096
FORMAT = pyaudio.paInt16
CHANNELS = 1

p = pyaudio.PyAudio()

# ================= FUNÇÃO =================
def medir():
    dur = int(slider.get())
    status.config(text=f"Medindo {dur}s...")
    root.update()

    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=FS,
        input=True,
        frames_per_buffer=CHUNK
    )

    frames = []

    for _ in range(int(FS / CHUNK * dur)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(np.frombuffer(data, dtype=np.int16))

    stream.stop_stream()
    stream.close()

    signal = np.concatenate(frames).astype(np.float32)
    signal -= np.mean(signal)

    yf = fft(signal)
    xf = fftfreq(len(signal), 1 / FS)

    mask = (xf > 0) & (xf < 100)

    ax.clear()
    ax.plot(xf[mask], np.abs(yf[mask]), color="#13ffcc", linewidth=1.5)
    ax.set_xlim(0, 100)
    ax.set_title("Assinatura 0–100 Hz", color="white")
    ax.set_xlabel("Frequência (Hz)", color="white")
    ax.set_ylabel("Amplitude", color="white")
    ax.tick_params(colors="white")
    ax.grid(True, alpha=0.3)

    fig.patch.set_facecolor("#111111")
    ax.set_facecolor("#111111")

    canvas.draw()
    status.config(text="Pronto")

# ================= GUI =================
root = tk.Tk()
root.title("Monitor Industrial 0–100 Hz (PyAudio)")
root.geometry("900x520")
root.configure(bg="#111111")

frame = tk.Frame(root, bg="#111111")
frame.pack(fill=tk.BOTH, expand=True)

btn = tk.Button(
    frame,
    text="▶ MEDIR",
    command=medir,
    bg="#00ffdd",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=12
)
btn.pack(pady=8)

slider = tk.Scale(
    frame,
    from_=1,
    to=20,
    orient=tk.HORIZONTAL,
    label="Segundos de Aquisição",
    bg="#111111",
    fg="white",
    highlightthickness=0,
    troughcolor="#333333"
)
slider.set(5)
slider.pack(fill=tk.X, padx=20)

status = tk.Label(frame, text="Aguardando", bg="#585858", fg="white")
status.pack(pady=5)

fig, ax = plt.subplots(figsize=(9, 4))
fig.patch.set_facecolor("#4D4D4D")

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

root.mainloop()

p.terminate()

