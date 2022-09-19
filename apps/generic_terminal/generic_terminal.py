from talon import Module, actions
import subprocess
import random
from time import sleep

mod = Module()


@mod.action_class
class Actions:
    # implements the function from generic_terminal.talon for unix shells

    def terminal_list_directories():
        """Lists directories"""

    def terminal_list_all_directories():
        """Lists all directories including hidden"""

    def terminal_list_all_directories_tree(number: int):
        """Lists all directories including hidden in tree"""

    def terminal_change_directory(path: str):
        """Lists change directory"""

    def terminal_change_directory_root():
        """Root of current drive"""

    def terminal_clear_screen():
        """Clear screen"""

    def terminal_run_last():
        """Repeats the last command"""

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""

    def terminal_kill_all():
        """kills the running command"""
    def create_draft_file():
        "create a draft file"
        filepath = f"/tmp/{random.randint(1000, 9999)}"
        print('filepath:', filepath)
        print("touch {filepath}")
        copied_text = actions.clip.text()
        subprocess.run(f"echo -n \"{copied_text}\" >> {filepath}", shell=True)
        sleep(1)
        print("code -n {filepath}")
        subprocess.run(f"code -n {filepath}", shell=True)