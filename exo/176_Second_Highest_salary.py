import polars as pl 

data = [[1,100], [2,200], [3,300]]

employee = pl.DataFrame(data,
                        schema={'id':pl.Int64,
                        'salary':pl.Int64})
print(employee)

def second_highest_salary(employee: pl.DataFrame) -> pl.DataFrame:
    salaries = employee['salary'].unique()
    if len(salaries) <2 :
        return pl.DataFrame({'SecondHighestSalary':[None]})
    else :
        second_salary = (salaries.sort(descending=True).slice(1, 1).item())
        df_second_slary = pl.DataFrame({'SecondHighestSalary': [second_salary]})
        print(df_second_slary)
        return df_second_slary
    
if __name__=='__main__':
    second_highest_salary(employee)
