# Caesar Cipher Decoder

A simple Python-based Caesar cipher decoder that performs brute-force decryption by testing all 26 possible alphabet shifts. It preserves uppercase and lowercase letters while keeping numbers, symbols, spaces, and other non-alphabetic characters unchanged.

---

## Version

**v2.0.0**

---

## Features

- Decode Caesar ciphers using brute-force decryption.
- Automatically test all 26 possible alphabet shifts (0–25).
- Preserve uppercase and lowercase characters.
- Maintain spaces, numbers, punctuation, and special characters.
- Use list-based string construction with `append()` and `join()`.
- Display all possible decoded results in a single execution.
- Support repeated decoding through a continuous input loop.
- Display shift values alongside their corresponding decoded results.
- Include type annotations for improved code readability.
- Use only Python's built-in functionality.

---

## Project Structure

```text
code-decoder/
├── main.py
├── README.md
└── LICENSE
```

---

## Explanation

The program uses a brute-force approach to decode Caesar ciphers by testing every possible alphabet shift.

Instead of requiring the user to know the original encryption key, it generates all 26 possible combinations and displays them for inspection.

The complete pipeline is:

```text
User Input
    ↓
Initialize Alphabets
    ↓
Generate Shift Values (0–25)
    ↓
Process Individual Characters
    ↓
Decode Alphabetic Characters
    ↓
Preserve Non-Alphabetic Characters
    ↓
Construct Decoded String
    ↓
Display All Possible Results
```

### Alphabet Initialization

The program defines two alphabet strings:

```python
lower_alphabet: str = "abcdefghijklmnopqrstuvwxyz"
upper_alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
```

These strings allow the program to process lowercase and uppercase characters independently.

### Brute-Force Decryption

The program uses:

```python
for shift in range(26):
```

This generates all possible Caesar cipher shifts, from 0 to 25.

Each shift represents a possible decryption key.

### Character Processing

Each character in the input phrase is processed individually.

The program checks whether the character belongs to the lowercase or uppercase alphabet.

**Lowercase characters:**

```python
result.append(lower_alphabet[lower_alphabet.index(letter)-shift])
```

**Uppercase characters:**

```python
result.append(upper_alphabet[upper_alphabet.index(letter)-shift])
```

The character's alphabet index is reduced by the current shift value to obtain the decoded character.

Python's negative indexing allows the alphabet to wrap around automatically.

**Non-alphabetic characters:**

```python
else:
    result.append(letter)
```

Characters that are not part of either alphabet are appended without modification.

This preserves spaces, punctuation, numbers, and special characters.

### String Construction

Instead of repeatedly concatenating strings, the program uses a list to collect decoded characters.

```python
result: list[str] = []
```

Each decoded character is added using:

```python
result.append(letter)
```

After processing all characters, the list is converted into a string using:

```python
"".join(result)
```

This approach avoids repeatedly creating intermediate strings during character processing.

### Result Display

Each possible decoded phrase is displayed alongside its corresponding shift value.

```python
print(f"{shift:<3} : {"".join(result)}")
```

The `<3` formatting aligns the shift numbers into a three-character-wide field.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/philip-euste/ceasar-cipher-decoder.git

cd code-decoder
```

### Requirements

- Python 3.12+
- No external dependencies.

---

## Usage

Run the program:

```bash
python main.py
```

Enter the encrypted phrase when prompted:

```text
Enter the code:
```

The program will generate and display all 26 possible decoded results.

The input prompt will repeat continuously, allowing multiple phrases to be decoded without restarting the program.

---

## Example

```text
--------------------------------------------------
Enter the code: Khoor Zruog

0   : Khoor Zruog
1   : Jgnnq Yqtnf
2   : Ifmmp Xpsme
3   : Hello World
4   : Gdkkn Vnqkc
...
25  : Lipps Asvph
```

<text color="secondary" size="xs">Example output abbreviated for readability.</text>

In this example, shift 3 produces the original phrase: `Hello World`.

---

## Dependencies

**Python 3.12+**

Standard Library / Built-in Functionality:

- `range()` — Generates the possible shift values.
- `input()` — Collects user input.
- `print()` — Displays the decoded results.
- `str.index()` — Finds character positions in the alphabet.
- `list.append()` — Adds decoded characters to the result list.
- `str.join()` — Combines decoded characters into a string.
- String indexing — Retrieves the corresponding shifted characters.
- Type annotations — Specify expected variable and function types.

No additional packages or installations are required.

---

## Limitations

- Only supports the standard English alphabet (A–Z).
- Does not automatically identify which result is the correct plaintext.
- Requires the user to inspect the 26 possible results.
- Does not encrypt messages.
- Does not support custom alphabets.
- Runs continuously without a built-in exit command.

---

## Future Improvements

- [ ] Automatically identify the most likely decoded phrase.
- [ ] Add frequency analysis.
- [ ] Add encryption functionality.
- [ ] Allow users to specify a known shift value.
- [ ] Add support for custom alphabets.
- [ ] Improve terminal output formatting.
- [ ] Add an option to decode a single phrase and exit.
- [ ] Extract decoding logic into a separate function.

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.