# Mission 4 - How programs run

## 1. Task / objective
Run a small Python program and compare compilers with interpreters.

## 2. Work completed
### 4.1 Python program

[hello.py](hello.py) contains one statement:

```python
print("Hello from Python")
```

From the repository root:

```sh
python3 mission-04-programs/hello.py
```

Expected and observed output: `Hello from Python`.

### 4.2 Compiler and interpreter

| Point | Compiler | Interpreter |
| --- | --- | --- |
| When translation / execution happens | Translates code into another form before that form is executed | Executes program instructions at runtime |
| Typical output | Object code, an executable, or intermediate code | Program results; a separate executable is not always produced |
| Example | Clang compiling a C program | CPython running a Python program |
| One advantage | A native executable can run without recompiling its source every time | Quick to edit a small script and run it again |

A compiler translates source code into another form before that result runs. An interpreter executes instructions while the program is running. The distinction is about implementations: CPython first compiles Python source into bytecode and then executes it in its interpreter. For this file, one `python3` command handles those steps and prints the message.

## 3. Commands / tools used
`python3` runs the script. `print()` sends the message to standard output.

## 4. My understanding
A `.py` extension identifies a Python source file, but saving it does not execute it. Passing the file to Python runs the statement. Compilation and interpretation can both be part of running the same program.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
[hello.py](hello.py) and [actual terminal output](../evidence/mission-04-hello.txt).

## 8. Commit details
Commit message: `Compare compilers and interpreters`.

Published in this repository's [commit history](https://github.com/Mayanksuthar07/digital-detective-8508/commits/main/).
