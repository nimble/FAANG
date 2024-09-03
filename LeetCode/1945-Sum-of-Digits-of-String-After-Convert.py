class Solution:
    def getLucky(self, s: str, k: int) -> int:
        letter_to_num = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26
        }

        # Complete our initial transform
        total_num_string = ""
        for char in s:
            total_num_string += str(letter_to_num[char])
        # print(total_num_string)

        # Now that we've got our initial number, it's time to begin the transforms and deduct 1 from k.
        transform_string = total_num_string
        print(transform_string)
        total_sum = 0
        while k > 0:
            total_sum = 0  # Reset total_sum for each iteration
            for num in transform_string:
                total_sum += int(num)
            print(total_sum)
            transform_string = str(total_sum)
            k -= 1
        
        return total_sum
