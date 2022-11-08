def isPalindrome(s: str):
    newstr = ""
    for word in s[::-1]:
        if word.isalnum():
            newstr+=word
    return newstr.lower() == s


def main():
    print(isPalindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
    main()
