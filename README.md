# EndSteamAlready: Giving Steam the Boot, Literally!

> **Note:** This repository is a clone of the original project by [ToClickx](https://github.com/ToClickx/fully-close-steam). It has been modified to address issues encountered during execution.

Sick of Steam staying in the background when you think you've closed it? With EndSteamAlready, one click is all it takes—puff—and Steam is really gone from your system, freeing up resources instantly. It's a completely safe Steam process-killer, perfect for when you're ready to shut down or just need to declutter.

EndSteamAlready provides a simple, intuitive graphical user interface (GUI) for completely closing all Steam processes.

## 🚀 Features

- **One-Click Solution**: Terminate all Steam processes with a single click.
- **User-Friendly Interface**: Simple and easy-to-navigate GUI.

## 📦 Installation Options

### 1. **Best Option**: Download the Latest Release

To save time and avoid the need for installation, you can simply download the latest pre-built executable from the [Releases](https://github.com/Christian-Rau/SteamBoot/releases) page:

1. Go to the [Releases](https://github.com/Christian-Rau/SteamBoot/releases) page.
2. Download the latest release (`SteamBoot.exe`).
3. Run the executable directly—no installation needed.
4. Lock it to taskbar (Optional)

### 2. Clone or Download the Repository and Build the Executable

If you'd like to build the executable yourself, follow these steps:

#### Step 1: Clone the Repository

````bash
git clone https://github.com/Christian-Rau/EndSteamAlready.git
cd SteamBoot```

#### Step 2: Set Up a Virtual Environment

Create a virtual environment in your terminal:

```bash
python -m venv venv
````

#### Step 3: Activate the Virtual Environment

- For Windows (PowerShell):

  ```bash
  venv\Scripts\Activate.ps1
  ```

- For macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

#### Step 4: Install Dependencies

Inside the virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```

#### Step 5: Build the Executable

To package the application into a standalone executable, use `pyinstaller`:

```bash
pyinstaller --onefile --windowed --icon=icon.ico --name=SteamBoot main.py
```

This will generate an executable file named `SteamBoot.exe` in the `dist` directory.

### 3. Clone or Download and Run the Script Directly

If you prefer to run the script directly, you can do so without building an executable:

1. Clone the repository as described above.
2. Install the dependencies inside a virtual environment.
3. Run the script directly:

   ```bash
   python main.py
   ```

## 📁 Project Structure

The project structure before building the executable is as follows:

```bash
SteamBoot├── gui.py
├── icon.ico
├── main.py
├── process_handler.py
├── README.md
└── requirements.txt
```

### When manually creating the executeable

After building the executable, the project structure looks like this:

```bash
SteamBoot├── dist
│   └── EndSteamAlready.exe # executable
├── gui.py
├── icon.ico
├── main.py
├── process_handler.py
├── README.md
└── requirements.txt
```

## Set PowerShell Execution Policy

The most common reason for this error is that PowerShell's execution policy is set to Restricted or AllSigned, which prevents scripts from being executed.

Open PowerShell as Administrator:

Right-click the Start menu and select _Windows PowerShell (Admin)_.
Set the execution policy to RemoteSigned:
Run the following command to allow PowerShell to execute local scripts that are not digitally signed:

powershell

```bash
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

You may be prompted with a warning message. Type Y and press Enter to confirm.

## 🛠️ Customization

The code is modular and easily customizable. You can modify it to suit your specific needs. For example, you can add additional processes to terminate or change the design of the GUI by tweaking `gui.py`.

## 🤝 Contributing

Contributions are welcome! If you encounter bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Original project by [ToClickx](https://github.com/ToClickx/fully-close-steam)
- [PyInstaller](https://www.pyinstaller.org/) for packaging Python applications

---

Happy coding! If you find this project helpful, please consider giving it a ⭐️ on GitHub.
