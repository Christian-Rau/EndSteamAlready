# test_kill_steam_processes.py
from unittest import mock
from process_handler import kill_steam_processes


def test_kill_steam_processes_no_errors():
    # Mock psutil.process_iter to return an empty list (no processes)
    with mock.patch('psutil.process_iter', return_value=[]):
        # Mock messagebox.showinfo to avoid showing actual message boxes
        with mock.patch('tkinter.messagebox.showinfo'):
            try:
                # Run the function
                kill_steam_processes()
                # If no exception is raised, the test will pass
            except Exception as e:
                # If any exception is raised, the test will fail
                assert False, f"kill_steam_processes() raised an exception: {e}"
