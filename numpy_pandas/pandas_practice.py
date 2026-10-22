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

a = df.iloc[2:5, 0:2]
print(a)

b = df.iloc[[1, 2, 5], [0, 2]]
print(b)

i1 = df.iloc[1, 1]
i2 = df.iat[1, 1]
print(i1, i1 == i2)

# select rows where df.A is greater than 0
print(df[df["A"] > 0])

# select values from a DataFrame where a boolean condition is met
print(df[df > 0])

# isin function for filtering
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)
print(df2[df2["E"].isin(["two", "four"])])

# setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range("20130102", periods=6))
df["F"] = s1
# setting values by label and index
df.at[dates[0], "A"] = 0
df.iat[1, 1] = 0
print(df)

# setting by assigning with a NumPy array
df.loc[:, "D"] = np.array([5] * len(df))
df.iloc[3, :] = np.array([5] * len(df.columns))
print(df)

# Reindexing allows you to change/add/delete the index on a specified axis.

df1 = df.reindex(index = dates[0:4], columns = list(df.columns) + ["E"])
df1.loc[dates[0]:dates[1], "E"] = 1
print(df1)

# dropping nan values
print(df1.dropna(how="any"))
# filling missing values
print(df1.fillna(value=7))
print(df1.isna())

# stats
print(df.mean())
print(df.mean(axis=1))

# user defined functions
agg1 = df.agg(lambda x: np.mean(x) * 5.6, axis = 0)
print(agg1)
trans1 = df.transform(lambda x: x * 101.2)
print(trans1)

# value counts
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

# string methods
s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print(s.str.lower())

# concat dataframes and series
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
pieces = [df[0:3], df[3:7], df[7:]]
print(pd.concat(pieces))

# merging
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
print(left)
print(right)
merged = pd.merge(left, right, on="key")
print(merged)

# merge() on unique keys

left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
print(left)
print(right)
merged = pd.merge(left, right, on="key")
print(merged)

# grouping

'''
By “group by” we are referring to a process involving one or more of the following steps:

Splitting the data into groups based on some criteria
Applying a function to each group independently
Combining the results into a data structure
'''

df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print(df)
print(df.groupby("A")[["C", "D"]].sum())
# Grouping by multiple columns label forms MultiIndex.
print(df.groupby(["A", "B"]).sum())

