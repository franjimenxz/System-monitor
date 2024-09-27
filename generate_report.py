import matplotlib.pyplot as plt
import pandas as pd

log_file = '/var/log/sys_monitor.log'
df = pd.read_csv(log_file, sep=', ', engine='python', names=['Timestamp', 'CPU', 'RAM', 'Disk'])

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['CPU'], label='CPU Usage (%)')
plt.plot(df['Timestamp'], df['RAM'], label='RAM Usage (%)')
plt.xlabel('Time')
plt.ylabel('Usage (%)')
plt.title('System Resource Usage Over Time')
plt.legend()
plt.grid(True)
plt.savefig('system_usage_report.png')
plt.show()
