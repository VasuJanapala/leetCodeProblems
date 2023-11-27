
class ZigZag:
    def convert(self, s: str, numRows: int) -> str:
        
        inc_positions = []
        converted_string = ''
        pos = 0
        break_value = numRows*2-2
        if ((len(s) == 1) or (numRows == 1) or (len(s) < numRows)):
            return s
        else:
            
            while(pos < len(s)):
                converted_string += s[pos]
                inc_positions.append(pos)
                pos += break_value
            # print(inc_positions)
            # print(converted_string)
            inc = 1
            while (inc < (numRows - 1)):
                for i in inc_positions:
                    
                    if i == 0:
                        converted_string += s[i+inc]
                        if len(inc_positions) == 1:
                            pass

                    else:
                        if ((i+inc) < len(s)):
                            converted_string += s[i-inc]
                            converted_string += s[i+inc]
                        elif ((i-inc) < len(s)):
                            converted_string += s[i-inc]
                inc += 1
            else:
                for i in inc_positions:
                    if ((i+inc) < len(s)):
                        converted_string += s[i+inc]
            return(converted_string)
        # PINALSIGYAHRPI
if __name__ == '__main__':
    zigzag = ZigZag()
    str = 'ABCDEFGHI'
    rows = 6
    print(zigzag.convert(str, rows))