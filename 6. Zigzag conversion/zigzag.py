
class ZigZag:
    def convert(self, s: str, numRows: int) -> str:
        
        inc_positions = []
        # print(s)
        converted_string = ''
        pos = 0
        break_value = numRows*2-2
        if ((len(s) == 1) or (numRows == 1) or (len(s) < numRows)):
            return s
        else:
            while ((len(s))<= (break_value+1)):
                # print("inside while loop one")
                s += '$'
            if (len(s)>(break_value+1)):
                temp_value = round(len(s)/(break_value+1))
                while(len(s)<=temp_value*break_value):
                    # print("inside while loop two")
                    s += '$'
            if '.' in s:
            
                while(pos < len(s)):
                    # print("inside while loop three")
                    print(s[pos])
                    converted_string += s[pos]
                    inc_positions.append(pos)
                    pos += break_value
                inc = 1
                while (inc < (numRows - 1)):
                    # print("inside while loop four")
                    for i in inc_positions:
                        
                        if i == 0:
                            print(s[i+inc])
                            converted_string += s[i+inc]
                        else:
                            if ((i+inc) < len(s)):
                                print(s[i-inc])
                                print(s[i+inc])
                                converted_string += s[i-inc]
                                converted_string += s[i+inc]
                            elif ((i-inc) < len(s)):
                                print(s[i-inc])
                                converted_string += s[i-inc]
                    inc += 1
                else:
                    # print("inside while loop else block")
                    for i in inc_positions:
                        if ((i+inc) < len(s)):
                            converted_string += s[i+inc]
                converted_string = converted_string.replace('$','')
                return(converted_string)

if __name__ == '__main__':
    zigzag = ZigZag()
    str = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
    rows = 3
    print(zigzag.convert(str, rows))