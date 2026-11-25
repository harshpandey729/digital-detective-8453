# Mission 3 - Understand the operating system

## 1. Task / objective
Explore system information, processes, storage, paths and file permissions.

## 2. Work completed
Recorded privacy-safe system observations and operating-system responsibilities.

## 3. Commands / tools used
- `sw_vers`: displayed the macOS product name and version.
- `whoami`: identifies the active account, with identifying output redacted in documentation.
- `df -h /`: displayed available and used root-storage capacity.
- `ps -ax -o pid,comm`: displayed a process snapshot and PID column.
- `pwd`, `cd`, `ls -l`: explored paths and permissions.

### Task 3.1

| Information | What it tells you | Observation |
|---|---|---|
| Operating system | Which OS services and tools are present | macOS 27.0.1, build 26A434 |
| Current account | Which local account runs commands | `[redacted]` |
| Storage | Capacity and amount currently used | Root volume snapshot: about 926 GiB total, 13 GiB used and 801 GiB available (about 2% used). |
| System activity | A brief view of running processes | Process snapshot was reviewed |

### Task 3.2

A process is a running instance of a program. The PID column is the unique process identifier used by the system. Examples observed included `launchd` and `logd`.

### Task 3.3

An absolute path begins at the filesystem root, while a relative path starts at the current directory. Example absolute path: `/Users/[redacted]/Desktop/Diwali Assignment/digital-detective-8453/mission-02-terminal`. Example relative path: `mission-02-terminal/terminal-practice`.

The practice text file displayed `-rw-r--r--`: its owner can read and write it, but not execute it; other users can read it. `r` means read, `w` write and `x` execute.

### Task 3.4

| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts, schedules and stops running programs | Launching an editor and ending it |
| Memory management | Allocates and tracks memory used by processes | Keeping an application and browser in RAM |
| Device management | Coordinates hardware through drivers | Writing to the keyboard or display |
| File management | Organises, locates and protects files | Creating and opening repository files |
| User interface / shell | Provides the graphical or command interface | macOS Finder or Terminal |
| Security and permissions | Controls access to resources and settings | Read/write permissions on a file |

## 4. My understanding
The OS is a resource manager between programs and hardware. It tracks processes, memory, devices, files and permissions while presenting usable interfaces.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
Privacy-safe observations and tables in this README.

## 8. Commit details
Commit message: `Document operating system and file management`
