import pandas as pd

def combined(person:pd.DataFrame, address:pd.DataFrame)->pd.DataFrame:
    combined_data = pd.merge(person, address, on='personId', how='left')
    # combined_data = combined_data.iloc[:,[1,3,4]]
    combined_data = combined_data[['firstName','city','state']]
    print(combined_data)



if __name__ == '__main__':
    person_keys_values = {
                        'personId':['a1001','a1002','a1003','a1004','a1005'], 
                        'firstName':['joe','ron','dan','noah','sam'], 
                        'age':[39,42,31,44,33]}
    person = pd.DataFrame(data=person_keys_values)

    address_key_values = {
                        'city':['dallas','norman','sarasota'],
                        'state':['texas','oklahoma','florida'],
                        'personId':['a1001','a1003','a1005']
    }

    address = pd.DataFrame(data=address_key_values)
    combined(person, address)