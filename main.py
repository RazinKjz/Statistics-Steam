import polars as pl


def main():
    q = (
        pl.scan_csv("data/penguins.csv")
        # .filter(pl.col("sepal_length") > 5)
        # .group_by("species")
        # .agg(pl.all().sum())
    )
    df = q.collect()
    print(df)

if __name__ == "__main__":
    main()
