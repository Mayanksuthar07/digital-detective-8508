# Mission 3 - Operating system

## 1. Task / objective
Observe the OS, account, storage, running processes, paths and file permissions.

## 2. Work completed
### 3.1 System observations

| Check | What it tells us | Result |
| --- | --- | --- |
| `sw_vers` / `uname -s` | OS version and kernel family | macOS 27.2.1; Darwin |
| `whoami` | The account used by the shell | Checked; account name redacted |
| `df -h .` | Space on the filesystem containing the project | 926 GiB size, 272 GiB used, 626 GiB available, 31% capacity |
| `ps -axo pid,pcpu,pmem,comm` | A brief process and resource-use snapshot | TextEdit, WindowServer and launchd appeared |

Storage and activity figures are a snapshot, not permanent specifications. Used plus available need not equal the displayed total because filesystem accounting, reserved space and rounding affect the figures.

### 3.2 Processes

A process is a running instance of a program. PID means process identifier: the OS uses this number to distinguish running processes.
The practice file was opened in TextEdit. In the recorded snapshot, TextEdit had PID `49235`; WindowServer had PID `609` and handled the graphical display. A program may start several processes, and PIDs can change after a restart.

### 3.3 Paths and permissions

From the repository root, moving into `mission-02-terminal/terminal-practice` added those folder names to the current path.

- Absolute path example, with private directories redacted: `/[redacted]/digital-detective-8508/mission-02-terminal/terminal-practice/notes.txt`. The real path returned by `pwd` begins with `/` and works independently of the current directory.
- Relative path from the repository root: `mission-02-terminal/terminal-practice/notes.txt`.

The original file listing showed `-rw-r--r--` (macOS may also display `@` for extended attributes). The first character identifies a regular file. The owner's next three characters are `rw-`: read and write are allowed, execute is not.

| Permission | Meaning for a file | Example |
| --- | --- | --- |
| `r` | Read the contents | `cat notes.txt` |
| `w` | Change the contents | Append another line |
| `x` | Execute the file | Start an executable script |

For a directory, `x` permits traversal. Reading a Python file through `python3` does not require the file itself to have execute permission.

### 3.4 OS responsibilities

| Responsibility | Explanation | Example |
| --- | --- | --- |
| Process management | Share CPU time among running programs | Browser and editor run together |
| Memory management | Allocate and protect working memory | Give an editor memory for an open document |
| Device management | Coordinate access to hardware | Send print data to a printer |
| File management | Organise files, folders and storage | Save and rename a text file |
| User interface / shell | Provide ways to give commands | Finder windows or a Terminal shell |
| Security and permissions | Control access to files and resources | Prevent another account from editing a private file |

## 3. Commands / tools used
`sw_vers`, `uname -s`, `whoami`, `df -h .`, `ps`, `pwd`, `cd`, `ls -l`, and TextEdit. Only selected process fields were recorded; no system permissions were changed.

## 4. My understanding
The OS coordinates programs and hardware. A saved program is a file; a process is that program running. Paths locate files, while permissions decide which operations an account can perform.

## 5. Difficulties faced
The restricted command environment blocked the process-list read. Opening TextEdit by its short name also failed.

## 6. How I resolved them
The process check was rerun with permitted desktop access. TextEdit opened using its full application path. Only selected output was saved, with account and device details omitted.

## 7. Evidence / files
[Selected system output](../evidence/mission-03-system.txt) and the [practice file](../mission-02-terminal/terminal-practice/notes.txt).

## 8. Commit details
Commit message: `Document operating system and file management`.

Published in this repository's [commit history](https://github.com/Mayanksuthar07/digital-detective-8508/commits/main/).
