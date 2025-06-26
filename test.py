import numpy as np
import matplotlib.pyplot as plt

# Bauteilwerte
R = 100       # Ohm
L = 10e-3     # Henry
C = 1e-6      # Farad

# Eingangssignal
f = 1000      # Frequenz 1 kHz
omega = 2 * np.pi * f
t = np.linspace(0, 5/f, 1000)  # 5 Perioden

# Eingangsspannung (Amplitude 1V)
U_in = np.sin(omega * t)

# Impedanzen
Z_R = R
Z_L = 1j * omega * L
Z_C = 1 / (1j * omega * C)

# Gesamtimpedanz seriell
Z_total = Z_R + Z_L + Z_C

# Strom (komplex)
I = U_in[0] / abs(Z_total)  # Stromamplitude (bei 1V Eingang)

# Berechnung komplexer Strom mit Phase:
# Phase von Gesamtimpedanz: phi = arg(Z_total)
phi = np.angle(Z_total)
I_t = I * np.sin(omega * t - phi)

# Spannungen:
U_R = R * I_t
U_L = omega * L * I * np.cos(omega * t - phi)  # U_L = L * dI/dt = L * I * omega * cos(...)
U_C = (1 / (omega * C)) * I * np.cos(omega * t - phi - np.pi/2)  # Spannung am C = (1/omega C)*I*cos(... - 90°)

# Alternative: Berechnung über komplex Rechnung (korrekt)
I_complex = (1 / Z_total) * 1  # Eingangsspannung 1V, komplexer Strom
U_R_complex = I_complex * Z_R
U_L_complex = I_complex * Z_L
U_C_complex = I_complex * Z_C

# Jetzt im Zeitbereich:
U_R_t = np.abs(U_R_complex) * np.sin(omega * t + np.angle(U_R_complex))
U_L_t = np.abs(U_L_complex) * np.sin(omega * t + np.angle(U_L_complex))
U_C_t = np.abs(U_C_complex) * np.sin(omega * t + np.angle(U_C_complex))

plt.figure(figsize=(10,6))
plt.plot(t*1e3, U_in, label='Eingangssignal (U_in)', color='black', linewidth=2)
plt.plot(t*1e3, U_R_t, label='Spannung am Widerstand (U_R)', color='red')
plt.plot(t*1e3, U_L_t, label='Spannung an der Spule (U_L)', color='blue')
plt.plot(t*1e3, U_C_t, label='Spannung am Kondensator (U_C)', color='green')

plt.xlabel('Zeit (ms)')
plt.ylabel('Spannung (V)')
plt.title('Spannungen im Seriellen RLC-Kreis bei 1 kHz')
plt.legend()
plt.grid(True)
plt.show()