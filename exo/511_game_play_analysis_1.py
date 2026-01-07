import polars as pl

data = [[1, 2,'2016-03-01', 5], [1, 2,'2016-05-02', 6], [2, 3,'2017-06-25', 1], [3, 1,'2016-03-02', 0], [3, 4,'2018-07-03', 5]]
activity = pl.DataFrame(
    data,
    schema={
        "player_id": pl.Int64,
        "device_id": pl.Int64,
        "event_date": pl.Utf8,
        "games_played": pl.Int64
    }
).with_columns(
    pl.col("event_date").str.strptime(pl.Date, "%Y-%m-%d")
)

print(activity)

def game_analysis(activity: pl.DataFrame) -> pl.DataFrame:
    activity = activity.sort(by='event_date')
    activity = activity.unique(subset='player_id', keep='first', maintain_order=True)
    activity = activity.sort(by='player_id')
    activity = activity.rename({'event_date':'first_login'})
    return activity[['player_id','first_login']]

if __name__ == '__main__':
    test = game_analysis(activity)
    print(test)
