import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('scope_6.csv', skiprows=1, dtype=str)
df.columns = ['time', 'ch1', 'ch2']
df = df.iloc[::10, :]
df['time'] = df['time'].str.replace('+', '', regex=False).astype(float)
df['1'] = df['ch1'].str.replace('+', '', regex=False).astype(float)
df['2'] = df['ch2'].str.replace('+', '', regex=False).astype(float)


plt.figure(figsize=(10, 6))
plt.plot(df['time'] * 1e6, df['ch1'] * 1000, label='Kanal 1 (mV)', linewidth=1)
plt.plot(df['time'] * 1e6, df['ch2'] * 1000, label='Kanal 2 (mV)', linewidth=1)

plt.xlabel('time (µs)')
plt.ylabel('Spannung (mV)')
plt.title('Oszilloskop-Plot')

plt.show()