# Mission 5 - Numbers and data

## 1. Task / objective
Convert numbers manually and with Python, build a decimal converter and explain text encoding.

## 2. Work completed
Added manual calculations, Python verification, a working converter and text-encoding answers.

## 3. Commands / tools used
- `python3`: opened interactive or script execution.
- `bin()`: converted decimal integers to binary strings.
- `int(value, 2)`: converted binary strings to decimal.
- `hex()`: converted decimal integers to hexadecimal strings.
- `int(value, 16)`: converted hexadecimal strings to decimal.
- `input()`: obtained decimal text from the user.
- `int()`: converted input text to an integer.

### Task 5.1 - Manual conversions

| Question | Working and answer |
|---|---|
| Decimal 13 to binary | 13 = 8+4+1, or `1101₂` |
| Decimal 25 to binary | 25 = 16+8+1, or `11001₂` |
| Binary 1010 to decimal | (1x8)+(0x4)+(1x2)+(0x1)=10 |
| Binary 1101 to decimal | (1x8)+(1x4)+(0x2)+(1x1)=13 |
| Hexadecimal A to decimal | A=10, so 10 |
| Hexadecimal 1F to decimal | (1x16)+15=31 |
| Binary 1111 to hexadecimal | 1111₂ = 15₁₀ = F₁₆ |

### Task 5.2 - Python verification

| Expression | Result | Match |
|---|---|---|
| `bin(13)` | `0b1101` | Yes |
| `bin(25)` | `0b11001` | Yes |
| `int("1010", 2)` | `10` | Yes |
| `int("1101", 2)` | `13` | Yes |
| `hex(10)` | `0xa` | Yes |
| `int("1F", 16)` | `31` | Yes |
| `hex(int("1111", 2))` | `0xf` | Yes |

### Task 5.3 - Documented converter cases

| Test number | Binary output | Hexadecimal output |
|---|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 42 | `0b101010` | `0x2a` |

`bin()` uses base 2 and prefixes a string with `0b`. `hex()` uses base 16 and prefixes a string with `0x`.

### Task 5.4 - Converter tests executed during this review

These six inputs were run with Python 3.9.6. Each run printed the prompt `Enter a positive decimal number: ` followed by the output shown below.

| Input | Observed output |
|---|---|
| `13` | `Binary: 0b1101`; `Hexadecimal: 0xd` |
| `25` | `Binary: 0b11001`; `Hexadecimal: 0x19` |
| `42` | `Binary: 0b101010`; `Hexadecimal: 0x2a` |
| `0` | `Please enter a valid positive decimal integer.` |
| `-5` | `Please enter a valid positive decimal integer.` |
| `abc` | `Please enter a valid positive decimal integer.` |

### Task 5.5 - Text encoding

- ASCII decimal code for `A`: 65
- ASCII decimal code for `a`: 97
- Encoding standards give characters a consistent numeric representation so computers and programs interpret text correctly.
- An example outside basic ASCII is `é`, `₹`, or `日`.

## 4. My understanding
Different bases are alternative representations of the same number. ASCII covers basic characters, while UTF-8 can encode much broader Unicode text.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
`number_converter.py`, conversion tables and Python verification in this README.

## 8. Commit details
Commit message: `Build number converter and practise data representation`
