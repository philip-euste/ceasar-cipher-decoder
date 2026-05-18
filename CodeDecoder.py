alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    phrase = input("Enter the code: ").lower()
    for shift in range(26):
        result = ""
        for letter in phrase:
            if letter in alphabet:
                result += alphabet[alphabet.index(letter)-shift]
            else:
                result += letter
        print(f"{shift} : {result}")
