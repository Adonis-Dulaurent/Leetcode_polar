import polars as pl

# import polar Schema
data = [[1, 'Wang','Allen'], [2, 'Allice', 'Bob']]
person = pl.DataFrame(data,
                       schema={'personId':pl.Int64,
                       'firstName':pl.Object,
                   'lastName':pl.Object})
data =[[1,2,'New york City', 'New York'], [2,3, 'Leetcode', 'California']]
address = pl.DataFrame(data,
                       schema={'addressId':pl.Int64,
                       'personId':pl.Int64,
                   'city':pl.Object,
               'state':pl.Object}
                       )
print(person)
print(address)

def combine_two_tables(person:pl.DataFrame, address:pl.DataFrame)-> pl.DataFrame:
        person = person.join(address,how='left', on='personId')
        person = person.drop(['personId','addressId'])
        print(person)
        return person

if __name__=='__main__':
        combine_two_tables(person, address)

