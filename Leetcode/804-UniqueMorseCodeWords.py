class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Words: words = ["gin","zen","gig","msg"]
        MORSE_CODE_DICT = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..'
                }
        transformations = set()
        for word in words:
            # After each word iteration, we're going to reset the cipher text to behave as a new string.
            cipher = ""
            for letter in word:
                cipher+= MORSE_CODE_DICT[letter.upper()]
            # Once the Ciphering is done, let's add it to transformations
            transformations.add(cipher)
            # Let's make the string empty again for next new cipher

        # Once we're compelte with the transformations, let's count the unique amount of transformations

        return len(transformations)

                

