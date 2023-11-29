
class ReverseInt:
    def reverse(self, x: int) -> int:
            value = 0
            z = x
            while(x != 0):
                if(x > 0):
                    value = (value * 10) + (x%10)
                    x = x//10
                elif(x < 0):
                    value = (value * 10) + (-x%10)
                    x = -x//10

            if (x == 0 and z < 0):
                value = -value
            if(0 > value >= -2**31):
                return(value)
            elif (0 < value <= 2**31-1):
                return(value)
            else:
                return(0)

if __name__ == "__main__":
     ri = ReverseInt()
     x = 123
     print(ri.reverse(x))

