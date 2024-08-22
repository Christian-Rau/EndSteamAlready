import psutil
from tkinter import messagebox

def kill_steam_processes():
    """
    Terminates all processes with 'steam' in their name.
    """
    terminated = False
    # Iterate over all running processes
    for process in psutil.process_iter(['pid', 'name']):
        try:
            # Check if "steam" is in the process name (case insensitive)
            if 'steam' in process.info['name'].lower():
                # Print information about the process being terminated
                print(f"Terminating process: {process.info['name']} (PID: {process.info['pid']})")
                # Terminate the process
                process.terminate()
                terminated = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    
    # Show a message box with the result
    if terminated:
        messagebox.showinfo("Success", "All 'steam' processes have been terminated.")
    else:
        messagebox.showinfo("No Processes Found", "No processes with 'steam' in their name were found.")
