# Mission 6 - Git and GitHub

## 1. Task / objective
Learn the basic Git workflow, branches and Pull Requests.

## 2. Work completed
Set up local Git history, used mission-specific commits, and documented the branch and Pull Request workflow.

## 3. Commands / tools used
- `git init -b main`: initialises the repository and selects `main`.
- `git status`: checks changed and untracked files.
- `git add`: stages selected changes.
- `git commit`: records a staged snapshot.
- `git log --oneline`: views recent commits.
- `git branch`: creates or lists branches.
- `git switch`: changes the active branch.
- `git push`: publishes commits to a remote repository.
- `git pull`: retrieves and integrates remote changes.

### Task 6.1

| Git operation | Purpose |
|---|---|
| Check status | Reports changed, staged and untracked files |
| Stage selected changes | Adds chosen file contents to the next commit |
| Create a commit | Records a snapshot in local Git history |
| View history | Shows commit IDs, messages and sequence |

Staging chooses which changes belong in the next commit; committing records those staged changes permanently as a new local snapshot.

### Branch and Pull Request workflow

Create `update-about`, add the `My Learning` section to the root README, commit it and publish the branch. On GitHub, compare `update-about` with `main` and open a Pull Request. Merge only if instructed. Local Git can then switch to `main` and run `git pull`.

A branch is an independent line of development. A Pull Request proposes and reviews one branch's changes before merging. These tools help contributors isolate work and review differences.

### Git glossary

- `git init`: initialise a Git repository.
- `git status`: inspect the working tree.
- `git add`: stage changes.
- `git commit`: save staged changes in history.
- `git log`: view commit history.
- `git branch`: create or list branches.
- `git switch`: switch to another branch.
- `git push`: publish local branches or commits to a remote.
- `git pull`: fetch and integrate remote changes.

## 4. My understanding
Git records and compares project snapshots locally, while GitHub hosts the repository for sharing and collaboration.

## 5. Difficulties faced
GitHub authentication was not configured through the GitHub CLI or SSH.

## 6. How I resolved them
Completed the local repository and commits first. Publishing must use an authenticated HTTPS credential or an SSH key added to the GitHub account.

## 7. Evidence / files
Commit history, this README and the planned `update-about` branch activity.

## 8. Commit details
Commit message: `Complete Git and GitHub collaboration mission`
