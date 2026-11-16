# Mission 6 - Git and GitHub

## 1. Task / objective
Practise staging and committing, publish update-about, open a pull request and explain the workflow.

## 2. Work completed
### 6.1 Status, stage, commit and history

The root README was updated with converter instructions and a project overview.
`git status --short` showed it as modified. `git add README.md` staged that file, and `git diff --cached --stat` showed what the next commit would include.
The commit `1f7fde0` (Add converter instructions and project overview) was pushed to `main`. `git log --oneline -4` then showed it at the top of the recent history.

| Operation | Meaning |
| --- | --- |
| `git status` | Check the working tree and staging area |
| `git add README.md` | Select the current README changes for the next commit |
| `git commit -m "message"` | Save a version of the staged changes in local history |
| `git log --oneline` | Show recent commits in a compact list |

Staging chooses what goes into a commit. Committing records that selection in history. Neither command publishes the changes online; `git push` does that.

### 6.2 Branch activity

The branch was created with `git switch -c update-about`.
A **My Learning** section was added to the root README with three points about append redirection, number bases and staging.
After checking status and the staged diff, the change was committed as `7f8a2a1` and published with `git push -u origin update-about`.

### 6.3 Pull request

[PR #1: Add My Learning section to README](https://github.com/Mayanksuthar07/digital-detective-8508/pull/1)

- Source branch: `update-about`
- Target branch: `main`
- Change reviewed: six added README lines, no program changes
- Status: **Open; not merged**

The assignment says to merge only if the instructor requests it, so the PR stays open. The local checkout was switched back to `main` to continue the other missions. The branch's My Learning section can be read in the PR; the main README already has a separate learning summary.

A branch gives a change its own line of development. A pull request presents that change for discussion and review before it is merged. This helps teammates see exactly what will change instead of overwriting each other's work.

### 6.4 Git glossary

| Command | Purpose |
| --- | --- |
| `git init` | Start Git tracking in a local folder |
| `git clone URL` | Download an existing repository and its history |
| `git status` | Show modified, staged and untracked files |
| `git add path` | Stage selected changes |
| `git commit -m "message"` | Record staged changes locally |
| `git log` | Read commit history |
| `git branch` | List branches |
| `git branch name` | Create a branch without switching to it |
| `git switch name` | Switch the working checkout to that branch |
| `git switch -c name` | Create a branch and switch to it |
| `git push` | Publish local commits to the remote repository |
| `git fetch` | Retrieve remote history without merging it |
| `git pull --ff-only` | Fetch changes and advance the current branch only when it can fast-forward |

`git init` and the post-merge `git pull` command are glossary examples here. This repository was cloned, and no PR merge was performed.

## 3. Commands / tools used
`git status`, `git add`, `git diff --cached`, `git commit`, `git log`, `git switch`, `git branch`, `git push`, and GitHub pull requests.

## 4. My understanding
Git is the version-control tool on the computer. GitHub hosts a remote copy and provides review tools. A local commit can exist without being on GitHub, and an open PR can exist without changing main.

## 5. Difficulties faced
An earlier staging command used a wildcard from the parent directory and did not match the evidence files.

## 6. How I resolved them
The exact file paths were staged from the repository directory, then the commit and push succeeded. Checking status prevented the missing files from going unnoticed.

## 7. Evidence / files
[Git output](../evidence/mission-06-git.txt), [update-about branch](https://github.com/Mayanksuthar07/digital-detective-8508/tree/update-about), and [PR #1](https://github.com/Mayanksuthar07/digital-detective-8508/pull/1).

## 8. Commit details
Commit message: `Complete Git and GitHub collaboration mission`.

Published in this repository's [commit history](https://github.com/Mayanksuthar07/digital-detective-8508/commits/main/).
