class Solution:
    def count_chars(self, s: str):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        return count

    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_count = self.count_chars(s1)
        window_count = self.count_chars(s2[:len_s1])

        if s1_count == window_count:
            return True

        for i in range(len_s1, len_s2):
            start_char = s2[i - len_s1]
            end_char = s2[i]

            window_count[end_char] = window_count.get(end_char, 0) + 1
            window_count[start_char] -= 1

            if window_count[start_char] == 0:
                del window_count[start_char]

            if window_count == s1_count:
                return True

        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.checkInclusion(s1="adc", s2="dcda"))