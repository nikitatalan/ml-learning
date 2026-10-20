import numpy as np
import pandas as pd

# creating Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# creating DataFrames
dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
print(df2.dtypes)

# viewing data
print(df.head(7))
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.to_numpy()) #always the same data type for the entire array
print(df.describe())
print(df.T == df.transpose()) #transpose

print(df.sort_index(axis=1, ascending=False)) # abcd -> dcba
print(df.sort_values(by="B"))

#selection by values

#columns
a = df["A"]
a = df.A
b = df[["A", "B"]]

#rows
c = df[0:3]
d1 = df.loc[dates[0]] #selecting a row matching a label
d2 = df.loc[:, ["A", "B"]] #selecting all rows and cols A, B
d3 = df.loc["20130102":"20130104", ["A", "B"]]
scalar = df.loc[dates[0], "A"]
scalar_fast = df.at[dates[0], "A"] #`faster version of the previous line

#selection by position

