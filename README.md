# Python_Praco

Small Python practice repo with two tiny scripts that show basic function definitions, control flow, and a simple command-line interface.

## What’s Inside

- `return.py` prints a New Year countdown and demonstrates an early `return`.
- `definition.py` adds three numbers and prints the result from the command line.

## Quick Start

Run either script directly with Python:

```powershell
python return.py
python definition.py
```

## Examples

### Countdown

```powershell
python return.py
```

Output:

```text
Three...
Two...
One...
Happy New Year!
```

### Add Three Numbers

```powershell
python definition.py 1 2 3
```

Output:

```text
1.0 + 2.0 + 3.0 = 6.0
```

If you skip arguments, `definition.py` uses default values:

```powershell
python definition.py
```

## Why This Repo Exists

This repo is a lightweight sandbox for Python basics:

- defining functions
- using `if __name__ == "__main__"`
- reading command-line arguments
- returning early from a function

## Notes

- No external dependencies are required.
- Works with standard Python 3.