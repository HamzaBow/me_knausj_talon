tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file

lisa:
    user.terminal_list_directories()
lisa all:
    user.terminal_list_all_directories()
lisa down [<number>]:
    user.terminal_list_all_directories_tree(number or 2)
katie [<user.text>]: user.terminal_change_directory(text or "")
katie root: user.terminal_change_directory_root()
go <user.system_path>: insert("cd \"{system_path}\"\n")
clear screen: user.terminal_clear_screen()
run last: user.terminal_run_last()
rerun [<user.text>]: user.terminal_rerun_search(text or "")
rerun search: user.terminal_rerun_search("")
kill all: user.terminal_kill_all()

copy paste:
    edit.copy()
    sleep(50ms)
    edit.paste()



disk:
    key(escape)
    insert(":w")
    key(enter)


go back: insert("cd ..\n")

clock: key(ctrl-l)

motion:
    key(escape)
    key(s)

draft it:
  key(escape)
  key(0)
  key(v)
  key($)
  key(ctrl-x)
  key(c)
  sleep(200ms)
  user.create_draft_file()