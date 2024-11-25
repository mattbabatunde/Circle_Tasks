class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Set to store characters in the current window
        char_set = set()
        left = 0  # Left pointer of the sliding window
        max_length = 0  # To store the maximum length of substring

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # If character is in the set, we need to shrink the window
            while s[right] in char_set:
                # Remove the character at the left pointer and move the left pointer right
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the max_length
            max_length = max(max_length, right - left + 1)

        return max_length