import tkinter as tk from tkinter import ttk import psutil
import time
class NetworkMonitorApp:
def  init (self, root): self.root = root
self.root.title("Network Monitor")
self.label_cpu = ttk.Label(root, text="CPU Usage:") self.label_cpu.grid(row=0, column=0, padx=10, pady=5, sticky="w")

self.label_memory = ttk.Label(root, text="Memory Usage:") self.label_memory.grid(row=1, column=0, padx=10, pady=5, sticky="w")
self.label_disk = ttk.Label(root, text="Disk Usage:") self.label_disk.grid(row=2, column=0, padx=10, pady=5, sticky="w")
self.label_network = ttk.Label(root, text="Network Traffic:") self.label_network.grid(row=3, column=0, padx=10, pady=5, sticky="w")

self.update_button = ttk.Button(root, text="Update", command=self.update_data)
self.update_button.grid(row=4, column=0, pady=10)
# Call the update_data method initially self.update_data()
def update_data(self): # Get CPU usage
cpu_percent = psutil.cpu_percent(interval=1)

# Get memory usage
memory_percent = psutil.virtual_memory().percent
# Get disk usage
disk_percent = psutil.disk_usage('/').percent
# Get network traffic
network_traffic = psutil.net_io_counters()

# Update labels with new data self.label_cpu.config(text=f"CPU Usage: {cpu_percent}%")
self.label_memory.config(text=f"Memory Usage: {memory_percent}%") self.label_disk.config(text=f"Disk Usage: {disk_percent}%") self.label_network.config(text=f"Network Traffic: Sent -
{network_traffic.bytes_sent}, Received - {network_traffic.bytes_recv}")

# Schedule the update_data method to be called after 1000 milliseconds (1 second)
self.root.after(1000, self.update_data)
if  name == " main ": root = tk.Tk()
app = NetworkMonitorApp(root) root.mainloop()