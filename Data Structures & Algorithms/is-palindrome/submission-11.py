class Solution:
    def isPalindrome(self, s: str) -> bool:
        no_space="".join(s.split())
        no_space=no_space.lower()
        new_string=""
        for s in no_space:
            if s.isalnum():
                new_string+=s
        if new_string==new_string[::-1]:
            return True
        else:
            return False

        