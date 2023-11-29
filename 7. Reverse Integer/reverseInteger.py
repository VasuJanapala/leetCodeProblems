import json

class ReverseInteger:
    def reverse(self, x: int) -> int:
        r = ''
        m = x
        if (x == 0):
            return 0
        while(x!=0):
            if(x<0):
                x = -(x)
                r += str(x%10)  #remainder
                x = x//10   # quotient
            else:
                r += str(x%10)  #remainder
                x = x//10       # quotient
        r = int(r)
        if m<0:
            dummy = str(r)
            dummy = '-' + dummy
            dummy = int(dummy)
            if dummy > -(2**31):
                return int(dummy)
            else:
                return 0
        if m > 0 and r <= (2**31-1):
            return r
        return 0
if __name__ == "__main__":
    reverseInterger = ReverseInteger()
    with open ("reverseInputFile.json", "r") as fopen:
        data = json.load(fopen)
    
    output = {}
    for key, value in data.items():
        output['Output_' + key] = reverseInterger.reverse(value)
    
    with open ("reverseOutputFile.json", "w") as fwrite:
        json.dump(output, fwrite, indent=4)
    
    