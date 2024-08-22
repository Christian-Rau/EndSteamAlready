from unittest import mock
from process_handler import kill_steam_processes
import psutil

def test_kill_steam_processes_no_errors():
    # Mock psutil.process_iter to return an empty list (no processes)
    with mock.patch('psutil.process_iter', return_value=[]):
        # Mock messagebox.showinfo to avoid showing actual message boxes
        with mock.patch('tkinter.messagebox.showinfo') as mock_showinfo:
            try:
                # Run the function
                kill_steam_processes()

                # Check that messagebox.showinfo is not called since no processes were found
                mock_showinfo.assert_not_called()

            except Exception as e:
                # If any exception is raised, the test will fail
                assert False, f"kill_steam_processes() raised an exception: {e}"
