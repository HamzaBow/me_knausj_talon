from talon import Context, actions, app
import os

ctx = Context()
ctx.matches = r"""
os: windows
"""

ctx.lists["self.launch_command"] = {
    "sound": "control mmsys.cpl sounds",
    "bluetooth": "control bthprops.cpl",
    "applications": "control appwiz.cpl",
    "display": "control desk.cpl",
    "taskbar": "control /name Microsoft.Taskbar",
    "programs and features": "control /name Microsoft.ProgramsAndFeatures",
    "Power": "control powercfg.cpl",
    "Mouse": "control main.cpl",
    "Keyboard": "control main.cpl keyboard",
    "Network": "control /name Microsoft.NetworkAndSharingCenter",
    "System Properties": "control sysdm.cpl",
    "User Accounts": "control userpasswords",
    "Internet Options": "control inetcpl.cpl",
    "Date and Time": "control timedate.cpl",
    "Device Manager": "control /name Microsoft.DeviceManager",
    "Ease of Access Center": "control /name Microsoft.EaseOfAccessCenter",
    "Administrative Tools": "control /name Microsoft.AdministrativeTools",
    "Default Programs": "control /name Microsoft.DefaultPrograms",
    "Windows Update": "control /name Microsoft.WindowsUpdate"
    # "Notifications": "control /name Microsoft.NotificationAreaIcons",
}

if app.platform == "windows":
    one_drive_path = os.path.expanduser(os.path.join("~", "OneDrive"))

    # this is probably not the correct way to check for onedrive, quick and dirty
    if os.path.isdir(os.path.expanduser(os.path.join("~", r"OneDrive\Desktop"))):
        default_folder = os.path.join("~", "Desktop")

        ctx.lists["self.directories"] = {
            "applications": "shell:AppsFolder",
            "desk": os.path.join(one_drive_path, "Desktop"),
            "docks": os.path.join(one_drive_path, "Documents"),
            "downloads": os.path.expanduser("~/Downloads"),
            "pictures": os.path.join(one_drive_path, "Pictures"),
            "one drive": one_drive_path,
            "user": os.path.expanduser("~"),
            "profile": os.path.expanduser("~"),
            "program files": os.path.expandvars("%ProgramFiles%"),
            "talent home": os.path.expandvars("%AppData%\\Talon"),
            "talent user": os.path.expandvars("%AppData%\\Talon\\user"),
            "talent recordings": os.path.expandvars("%AppData%\\talon\\recordings"),
            "talent plugins": os.path.expandvars(
                "%ProgramFiles%\\Talon\\talon_plugins"
            ),
            "root": "\\",
        }

    else:
        ctx.lists["self.directories"] = {
            "applications": "shell:Applications",
            "desk": os.path.expanduser("~/Desktop"),
            "docks": os.path.expanduser("~/Documents"),
            "downloads": os.path.expanduser("~/Downloads"),
            "pictures": os.path.expanduser("~/Pictures"),
            "user": os.path.expanduser("~"),
            "profile": os.path.expanduser("~"),
            "program files": os.path.expandvars("%ProgramFiles%"),
            "talent home": os.path.expandvars("%AppData%\\Talon"),
            "talent user": os.path.expandvars("%AppData%\\Talon\\user"),
            "talent recordings": os.path.expandvars("%AppData%\\talon\\recordings"),
            "talent plugins": os.path.expandvars(
                "%ProgramFiles%\\Talon\\talon_plugins"
            ),
            "root": "\\",
        }


@ctx.action_class("user")
class UserActionsWin:
    def exec(command: str):
        actions.user.system_command_nb(command)

    def system_shutdown():
        shutdown("s")

    def system_restart():
        shutdown("r")

    def system_hibernate():
        shutdown("h")

    def system_lock():
        actions.key("super-l")

    def system_show_desktop():
        actions.key("super-d")

    def system_task_view():
        actions.key("super-tab")

    def system_switcher():
        actions.key("ctrl-alt-tab")

    def system_search():
        actions.key("alt-space")

    def system_last_application():
        actions.key("alt-tab")

    def system_open_directory(path):
        actions.user.exec(f'explorer.exe "{path}"')

    def system_show_clipboard():
        actions.key("super-v")


def shutdown(flag: str):
    actions.key("super-r")
    actions.sleep("650ms")
    actions.insert(f"shutdown /{flag}")
