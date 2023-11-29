import json

class ZigZag:
    def convert(self, s: str, numRows: int) -> str:
        
        inc_positions = []
        converted_string = ''
        pos = 0
        break_value = numRows*2-2
        if ((len(s) == 1) or (numRows == 1) or (len(s) < numRows)):
            return s
        else:
            while ((len(s))<= (break_value+1)):
                s += '$'

            if (len(s)>(break_value+1)):
                temp_value = round(len(s)/(break_value))
                while(len(s)<=temp_value*(break_value+1)):
                    s += '$'

            while(pos < len(s)):
                converted_string += s[pos]
                inc_positions.append(pos)
                pos += break_value
            inc = 1
            while (inc < (numRows - 1)):
                for i in inc_positions:
                    
                    if i == 0:
                        converted_string += s[i+inc]
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
            converted_string = converted_string.replace('$','')
            return(converted_string)

if __name__ == '__main__':
    zigzag = ZigZag()
    with open("zigzagInputFile.json", "r") as fopen:
        data = json.load(fopen)
    output = {}
    for key, value in data.items():
        output["output_of_" + key] = zigzag.convert(value['string'], value['numRows'])
    with open ("zigzagOutputFile.json", "w") as fwrite:
        json.dump(output, fwrite, indent=4)