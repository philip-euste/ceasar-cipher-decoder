def main() -> None:
    lower_alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while True:
        print("-"*50)
        phrase: str = input("Enter the code: ")
        for shift in range(26):
            result: list[str] = []
            for letter in phrase:
                if letter in lower_alphabet:
                    result.append(lower_alphabet[lower_alphabet.index(letter)-shift])
                elif letter in upper_alphabet:
                    result.append(upper_alphabet[upper_alphabet.index(letter)-shift])
                else:
                    result.append(letter)
            print(f"{shift:<3} : {"".join(result)}")

if __name__ == "__main__":
    main()