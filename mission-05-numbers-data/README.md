# Mission 5 - Numbers and data

## 1. Task / objective
Show conversion steps, verify them with Python, build a decimal converter and explain text encoding.

## 2. Work completed
### 5.1 Conversion working

[Handwritten working for all seven conversions (PDF)](manual-conversions.pdf).

**Decimal 13 to binary:**

```text
13 / 2 = 6 remainder 1
 6 / 2 = 3 remainder 0
 3 / 2 = 1 remainder 1
 1 / 2 = 0 remainder 1
Read remainders upward: 1101
Check: 8 + 4 + 0 + 1 = 13
```

**Decimal 25 to binary:**

```text
25 / 2 = 12 remainder 1
12 / 2 =  6 remainder 0
 6 / 2 =  3 remainder 0
 3 / 2 =  1 remainder 1
 1 / 2 =  0 remainder 1
Read remainders upward: 11001
Check: 16 + 8 + 0 + 0 + 1 = 25
```

| Conversion | Working | Answer |
| --- | --- | --- |
| Binary `1010` to decimal | 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 2 | 10 |
| Binary `1101` to decimal | 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 1 | 13 |
| Hex `A` to decimal | A represents ten; 10×16⁰ | 10 |
| Hex `1F` to decimal | 1×16¹ + 15×16⁰ = 16 + 15 | 31 |
| Binary `1111` to hex | 8 + 4 + 2 + 1 = 15; hex digit for 15 is F | F |

### 5.2 Python verification

| Expression | Result | Matches working? |
| --- | --- | --- |
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(10)` | `0xa` | Yes, A represents 10 |
| `hex(31)` | `0x1f` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))` | `0xf` | Yes |

### 5.3 Converter

From the repository root:

```sh
python3 mission-05-numbers-data/number_converter.py
```

| Test input | Binary | Hexadecimal |
| --- | --- | --- |
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |
| 0 | `0b0` | `0x0` |

`input()` reads text. `int()` converts that text to an integer. `bin()` and `hex()` return strings representing the same integer in base 2 and base 16.
The prefixes `0b` and `0x` identify the base; they are not extra digits in the value. Hexadecimal letters are lowercase in Python's output.

The program accepts zero and positive integers. Letters, fractions, blank input and negative values produce a short message instead of a traceback. End of input is also handled.

### 5.4 Text encoding

`ord('A')` is **65** and `ord('a')` is **97**. Uppercase and lowercase letters are different characters, so their codes differ.

An encoding defines how characters are represented as bytes so software can store and read the same text consistently. Basic ASCII covers 128 characters; UTF-8 can encode Unicode characters from many languages.
For example, `अ` is not part of basic ASCII. In UTF-8 it uses the bytes `E0 A4 85`.

A bit is one binary digit, 0 or 1. Eight bits make one byte. A character can take more than one byte.

## 3. Commands / tools used
Python 3 interactive checks and the converter; `input()`, `int()`, `bin()`, `hex()`, `ord()` and `encode()`. The converter was also run as a separate process for each test input.

## 4. My understanding
The number stays the same when its base changes; only the written representation changes. Binary place values double from right to left, while hexadecimal place values multiply by 16. Text needs an agreed encoding because a byte value alone does not tell us which character it represents.

## 5. Difficulties faced
Invalid input cannot be converted to an integer. This was deliberately checked with letters, a fraction and an empty line.

## 6. How I resolved them
The program catches ValueError, checks negative values separately and handles EOFError. The valid cases and these error paths were run successfully.

## 7. Evidence / files
- [Handwritten manual conversions](manual-conversions.pdf)
- [number_converter.py](number_converter.py)
- [Python expression checks](../evidence/mission-05-python-checks.txt)
- [Nine input checks and outputs](../evidence/mission-05-converter-tests.txt)

## 8. Commit details
Commit message: `Build number converter and practise data representation`.

Handwritten notes added with commit message: `Add handwritten Mission 5 conversion notes`.

Published in this repository's [commit history](https://github.com/Mayanksuthar07/digital-detective-8508/commits/main/).
