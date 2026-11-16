# Mission 2 - Terminal and file management

## 1. Task / objective
Practise file commands inside the repository and explain flags, pipes and package managers.

## 2. Work completed
### 2.1 Commands and observations

Before the file practice, the expected result was a text file containing two lines and a second file with the same contents.

| Command | Purpose | Result observed |
| --- | --- | --- |
| `pwd` | Show the current full path | Ended in `mission-02-terminal` |
| `ls` | List visible entries | Initially showed `README.md` |
| `ls -l` | Show a detailed listing | Included permissions, size and modification time |
| `cd ..` | Move to the parent directory | The path changed to the repository root |
| `mkdir terminal-practice` | Create a folder | A new practice directory was created |
| `touch terminal-practice/notes.txt` | Create an empty file | The file was available for writing |
| `cp` | Copy a file | Original and backup both existed |
| `mv` | Move or rename a file | `backup.txt` became `notes-backup.txt` |
| `cat` | Print file contents | Both lines appeared in order |

Commands were run from this mission folder; `cd ..` was checked in a separate shell. All practice files stayed inside `terminal-practice`.

### 2.2 Changing files

```sh
printf 'First line: terminal practice.\n' > terminal-practice/notes.txt
printf 'Second line: added without replacing the first.\n' >> terminal-practice/notes.txt
cp terminal-practice/notes.txt terminal-practice/backup.txt
mv terminal-practice/backup.txt terminal-practice/notes-backup.txt
cat terminal-practice/notes.txt
```

- `>` creates or replaces the file contents. `>>` adds text at the end.
- `cp` makes another file and keeps the source. `mv` changes its location or name.
- `pwd` shows exactly which directory a relative command will use.
- `ls` helps check spelling and see whether a file was actually created.

### 2.3 Flags and pipes

`ls` left out `.hidden-example`. `ls -lah` showed it, along with `.` and `..`.
The `-l` option gives details, `-a` includes hidden entries, and `-h` uses readable sizes such as `79B`.

In `ls -l terminal-practice | head -n 3`, the left side produces a listing. The pipe sends that text to `head`, which keeps the first three lines. Here the `total` line counts as one of those three lines.

### 2.4 Package managers

Homebrew was already installed: version **7.0.9**. `brew list --formula` displayed installed packages, including Git, Node and Python.
A package manager keeps track of software and its dependencies. It provides consistent commands to install, update or remove packages. No packages were installed or removed for this mission.

## 3. Commands / tools used
`pwd`, `ls`, `cd`, `mkdir`, `touch`, `printf`, `cp`, `mv`, `cat`, `head`, `brew --version` and `brew list --formula`. Their purposes and results are listed above.

## 4. My understanding
The terminal uses the current directory as the starting point for relative paths. File commands do different jobs: copying preserves the original, moving changes a path, and appending preserves existing text. A pipe passes output between commands; it does not create a backup file.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- [Recorded commands and results](../evidence/mission-02-terminal.txt)
- [Original text](terminal-practice/notes.txt)
- [Renamed backup](terminal-practice/notes-backup.txt)
- [Hidden practice file](terminal-practice/.hidden-example)

## 8. Commit details
Commit message: `Complete Terminal and file management mission`.

Published in this repository's [commit history](https://github.com/Mayanksuthar07/digital-detective-8508/commits/main/).
