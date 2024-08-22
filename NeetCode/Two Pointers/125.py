def isPalindrome(s: str):
    newstr = ""
    oldstr = ""
    for w in s:
        if w.isalnum():
            oldstr+=w
    for word in s[::-1]:
        if word.isalnum():
            newstr+=word
    return newstr.lower() == oldstr.lower()


def main():
    print(isPalindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
    main()
