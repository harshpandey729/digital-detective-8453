# Mission 2 - Become comfortable with the Terminal

## 1. Task / objective
Practise safe Terminal operations, file management, flags, pipes and package-manager concepts.

## 2. Work completed
Created `terminal-practice/practice.txt`, backed it up, renamed a copy, and documented command behavior and observations.

## 3. Commands / tools used

| Operation / command | What it does | Observation |
|---|---|---|
| `pwd` | Prints the absolute current-directory path. | Shows the exact folder currently in use. |
| `ls` | Lists names in the current directory. | Reveals files and folders. |
| `ls -l` | Lists detailed metadata. | Shows permissions, owner category, size and date. |
| `cd ..` | Moves to the parent directory. | The current location changes upward. |
| `mkdir` | Creates a directory. | Creates `terminal-practice`. |
| `touch` | Creates an empty file or updates its timestamp. | Creates a new text file. |
| `cp` | Copies a file. | Leaves the original and creates a backup copy. |
| `mv` | Moves or renames a file. | Changes the file location or name. |
| `cat` | Displays file contents. | Shows both saved lines. |
| `ls -la` | Includes detailed listing and hidden files. | Adds hidden entries such as `.git`. |
| `ls -lh` | Shows human-readable sizes. | Size values are easier to read. |
| `ls -l | head` | Pipes the listing to `head`. | Only the first few listing lines appear. |

The pipe `|` sends the first command's output to the next command as input. `ls -l` creates the detailed list and `head` limits that list.

## 4. My understanding
Replacing a file usually overwrites its previous contents. Appending adds text to the end. Copying preserves the original while moving changes the original file's location. `pwd` identifies location; `ls` helps users inspect and navigate folders.

Package managers install, update and remove software consistently. Homebrew is available in this environment, and it would normally be checked with `brew --version` and `brew list`; this mission does not install or uninstall anything.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
`terminal-practice/practice.txt`, `practice-copy.txt` and this README.

## 8. Commit details
Commit message: `Complete Terminal and file management mission`
