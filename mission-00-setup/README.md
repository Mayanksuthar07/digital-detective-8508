# Mission 0 - Workspace setup

## 1. Task / objective
Prepare the repository and one folder for each mission.

## 2. Work completed
The existing public repository is `digital-detective-8508`. Its local folder has the same name. There are nine mission folders, a root README and an evidence folder. Python and Git were checked again on 16 November 2026.

| Tool | Version observed |
| --- | --- |
| Python | 3.14.7 |
| Git | 2.54.0 (Apple Git-157) |

The original repository already had the required empty mission files. This update fills the setup notes and adds `.gitignore`. The tracked Finder metadata file is removed from the current version.

## 3. Commands / tools used
- `git clone`: download the existing repository and its history.
- `python3 --version` and `git --version`: check the installed tools.
- `git status`, `git add`, `git commit`, `git push`: review and publish the setup change.

## 4. My understanding
A repository stores project files and their version history. Separate mission folders make it easier to find the notes and evidence for one topic without mixing everything together.

## 5. Difficulties faced
The first clone attempt could not resolve github.com inside the restricted command environment.

## 6. How I resolved them
The clone was retried with network access and completed. Python and Git were already available; no installation was needed.

## 7. Evidence / files
[Tool versions](../evidence/mission-00-tools.txt), [root README](../README.md) and [.gitignore](../.gitignore).

## 8. Commit details
Commit message: `Complete workspace setup and tool checks`.

Published in this repository's [commit history](https://github.com/Mayanksuthar07/digital-detective-8508/commits/main/).
