import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    if (len(employee) > 1):
        # sorting the dataframe by salary column
        sorting = employee.sort_values(by='emp_salary', ascending=True)

        # trying to filter the top second value
        temp = sorting.iloc[[1],[1]]

        #renaming the column name
        second_highest = temp.rename(columns={'emp_salary':'SecondHighestSalary'})

        return second_highest
    else:
        temp_df = pd.DataFrame({'SecondHighestSalary':[None]})
        return temp_df

if __name__ == '__main__':
    emp_details = {
        'emp_id':[1001,1002,1003],
        'emp_salary':[10000,20000,30000]
    }
    employee = pd.DataFrame(data=emp_details)
    # print(employee)
    print(second_highest_salary(employee))