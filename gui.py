import tkinter as tk
import os

from process_handler import kill_steam_processes

def on_enter(e):
    e.widget['background'] = '#37005c'  # Change to hover background color
    e.widget['foreground'] = '#ececec'  # Change to hover text color

def on_leave(e):
    e.widget['background'] = '#ececec'  # Revert to original background color
    e.widget['foreground'] = '#37005c'  # Revert to original text color

def create_gui():
    """
    Creates a GUI with a button to terminate all processes with 'steam' in their name.
    """
    # Create the main window
    root = tk.Tk()
    root.title("EndSteamAlready")
    root.geometry("300x140")  # Set the window size

    # Optional: Set window icon if the file exists
    icon_path = 'icon.ico'
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        print(f"Icon file '{icon_path}' not found. Using default icon.")
    
    # Set background color
    root.configure(bg='#37005c')  # A dark background color

    # Create a custom-styled button using tk.Button
    button = tk.Button(root, text="Terminate Steam Processes", command=kill_steam_processes,
                       font=("Helvetica", 12, "bold"),
                       bg="#ececec",  # Button background color
                       fg="#37005c",  # Button text color
                       activebackground="#37005c",  # Button background when pressed
                       activeforeground="#ececec",  # Button text color when pressed
                       padx=10, pady=5)  # Padding inside the button
    # Adjusted pady to move the button down by 30px
    button.pack(pady=(40, 10))  # 50 pixels above, 10 pixels below for padding

    # Bind hover events to the button
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

    # Add a label with custom font and styling
    label = tk.Label(root, text="Enough Steam! - GitHub: Christian-Rau",
                     font=("Helvetica", 10),
                     fg="#9b65ff",  # Text color
                     bg='#37005c')  # Match background color of the window
    label.pack(side=tk.BOTTOM, pady=10)  # Position the label at the bottom

    # Start the GUI event loop
    root.mainloop()
