import polars as pl

data = [[1, 'Will', None], [2, 'Jane', None], [3, 'Alex', 2], [4, 'Bill', None], [5, 'Zack', 1], [6, 'Mark', 2]]
customer = pl.DataFrame(data,
                        schema={
                            'id':pl.Int64,
                            'name':pl.Object,
                            'referee_id':pl.Int64
                        }
)
print(customer)

def find_customer_referee(customer: pl.DataFrame) -> pl.DataFrame:
    df = customer
    df = df.filter((pl.col('referee_id') != 2) | (pl.col('referee_id').is_null()))
    return df[['name']]

if __name__== '__main__':
    test = find_customer_referee(customer)
    print(test)
