import json

class PalindromeNumber:
    def isPalindrome(self, x: int) -> bool:
        
        original_value = x
        value = 0

        INT_MAX = 2**31-1
        INT_MIN = -2**31

        if x<0:
            return False
        
        if x <= INT_MAX or x >= INT_MIN: 
            #reverse a number
            while(x!=0):
                rem = x % 10
                x = x//10
                value = (value * 10) + rem
            return(value == original_value)
        else:
            return False
        

if __name__ == '__main__':
    palindrome = PalindromeNumber()
    output = {}

    with open ("palindromeInputFile.json", "r") as fread:
        data = json.load(fread)
    
    for key, value in data.items():
        output['output_' + key] = palindrome.isPalindrome(value)

    with open ("palindromeOutputFile.json", "w") as fwrite:
        json.dump(output, fwrite, indent = 4)