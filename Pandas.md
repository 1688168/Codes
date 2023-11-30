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

> Group by

```
df=df.groupby('a_column', as_index=False)['the_column_to_aggregate'].sum()
```

> merge_asof(df1, df2, by='category', on='col1', direction='forward', allow_exact_matches=False, tolerance=pd.Timedelta('1s))

- df1 left join df2
- on is default looking 'backward'

> apply, map, applymap
`map on series`
```
# create a new column that maps values on another column from string to num
train['sex_num'] = train.Sex.map({'female':0, 'male':1})
```
`apply on Series`
```
# ex 1:
train['name_length'] = train.name.apply(len)

# ex 2:
def my_function(my_list, position):
    return my_list[position]
- train.name.str.split(',').apply(my_function, position=0)
```

`apply on dataframe`

```
# get max on each column (axis=0)
df.apply(max, axis=0)

# (apply on each row) which column (name) has the max value

df.apply(np.argmax, axis=1) 
```

`applymap`
```
# convert all values to flow
df.applymap(float)
```