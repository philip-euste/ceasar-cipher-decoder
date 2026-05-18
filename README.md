# 🔐 Caesar Cipher Brute Force Decoder

A simple Python tool that attempts every possible Caesar Cipher shift to help decode encrypted messages.

This project brute-forces all 26 possible shifts of the alphabet and displays every result so the user can identify the correct decoded phrase.

---

# ✨ Features

* 🔎 Tries all 26 Caesar Cipher shifts
* 🧠 Beginner-friendly Python logic
* 💬 Supports spaces and symbols
* ⚡ Instant terminal output
* 🔁 Infinite loop for multiple decoding attempts

---

# 🛠️ Technologies Used

* Python 3

No external libraries required.

---

# ▶️ How It Works

The program:

1. Takes a coded phrase from the user
2. Shifts each letter backward through the alphabet
3. Prints every possible decoded result

Example:

```text id="xpwth2"
Enter the code: khoor

0 : khoor
1 : jgnnq
2 : ifmmp
3 : hello
...
```

In this example:

```text id="djmyal"
khoor
```

decoded with shift `3` becomes:

```text id="0m64t6"
hello
```

---

# ▶️ Running the Program

```bash id="dkm0sk"
python CaesarCipherDecoder.py
```

---

# 📚 What This Project Demonstrates

This project uses:

* loops
* string manipulation
* indexing
* conditionals
* brute-force searching
* basic cryptography concepts

---

# 🚧 Possible Future Improvements

* 🔐 Add encryption mode
* 🔓 Add direct decryption mode
* 🔠 Preserve uppercase letters
* 📊 Add frequency analysis
* 🖥️ Create a GUI version
* 📁 Save results to a text file

---

# 📖 About Caesar Ciphers

The Caesar Cipher is one of the oldest known encryption techniques.

Each letter in a message is shifted forward or backward through the alphabet by a fixed amount.

Example with a shift of `3`:

```text id="pn4lm1"
a → d
b → e
c → f
```

---

# 📄 License

Free to use for learning and educational purposes.
