# Mission 4 - How programs run

## 1. Task / objective
Create and run a simple Python program and compare compilers with interpreters.

## 2. Work completed
Created `hello.py` and added a compiler/interpreter comparison.

## 3. Commands / tools used
- From the repository root, `python3 mission-04-programs/hello.py` ran the program and printed `Hello from Python`.

### Compiler and interpreter comparison

| Point | Compiler | Interpreter |
|---|---|---|
| When translation/execution happens | Translates source before execution | Reads and executes instructions at runtime |
| Typical output | Executable or intermediate form | Direct execution, usually no standalone executable |
| One example | C or C++ compiler | CPython executing Python |
| One advantage | A compiler can optimize code before execution | Easier rapid testing and debugging |

In this context, a compiler translates source code before a program runs, whereas an interpreter executes source instructions during runtime. Real implementations can combine compilation and interpretation, as Python implementations may compile source into bytecode before execution.

## 4. My understanding
Python source can be tested quickly because an interpreter reads and executes it. Compilation trades an earlier translation step for a separately produced executable or intermediate form.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
`hello.py` and this README.

## 8. Commit details
Commit message: `Compare compilers and interpreters`
