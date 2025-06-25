class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create an empty string to store only letters and numbers

        cleaned_string=""

        for char in s:
            if char.isalnum():
                  #alphanumeric means letters or numbers , no symbols
                  cleaned_string+=char.lower()
        if cleaned_string==cleaned_string[::-1]:
            return True
        else:
            return False



        