import polars as pl

data = [[1,'john@example.com'], [2,'bob@example.com'], [3, 'john@example.com']]
person = pl.DataFrame(data,
                      schema={'id':pl.Int64,
                      'email':pl.Object})
print(person)

def delete_duplicate_emails(person: pl.DataFrame) -> None:
    person = person.sort(by='id')
    person = person.unique(subset='email',keep='first', maintain_order=True)
    return person

if __name__ == '__main__':
    test = delete_duplicate_emails(person)
    print(test)
