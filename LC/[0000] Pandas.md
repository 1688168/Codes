### > Regular Expression and String Pattern Matching

[1517]

- raw string

```
def valid*emails(users: pd.DataFrame) -> pd.DataFrame:
    # Note how we use a raw string (putting an `r` in front) to avoid having to escape the backslash
    # Also note that we escaped the `@` character, as it has a special meaning in some regex flavors
    return users[users["mail"].str.match(r"^[a-zA-Z]a-zA-Z0-9*.-]\*\@leetcode\.com$")]
```

[1527]

- regular expression for string pattern matching

```
def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].str.contains(r"\bDIAB1", regex=True)]
```

[177] Nth Highest Salary

```
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[["salary"]].drop_duplicates()  #remove duplicate
    if len(df) < N:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]}) # construct empty dataframe
    return df.sort_values("salary", ascending=False).head(N).tail(1) #sorting[["salary"]]
```

### > unique values:

- nunique (Series or dataframe)
