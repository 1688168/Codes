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

# <span style="color:green">====================</span>

# <span style="color:blue"> Input/Output</span>

# <span style="color:green">====================</span>

> write to pickle

```
team_splits.to_pickle(os.path.join("..", "some_file_name"))
```

> read pickle

```
df = pd.read_pickle(os.path.join('..', 'file.pickle'))
```

> read excel

```
df=pd.read_excel(os.path.join(input_filename), index_col=0)
```

# <span style="color:green">====================</span>

# <span style="color:blue"> prepare data/clean data</span>

# <span style="color:green">====================</span>

> drop columns

```

```

# <span style="color:green">====================</span>

# <span style="color:blue"> Manipulating Data</span>

# <span style="color:green">====================</span>

`apply on Series`: operate on each cell of a series

```
# ex 1:
train['name_length'] = train.name.apply(len)

# ex 2:
def my_function(my_list, position):
    return my_list[position]
- train.name.str.split(',').apply(my_function, position=0)
```

`apply on dataframe`: operate on columns

```
# get max on each column (axis=0)
df.apply(max, axis=0)

# (apply on each row) which column (name) has the max value

df.apply(np.argmax, axis=1)
```

`applymap`: Operate on each cell

```
# convert all values to flow
df.applymap(float)
```

> apply, map, applymap
> `map on series`: convert a series value to another value

```
# create a new column that maps values on another column from string to num
train['sex_num'] = train.Sex.map({'female':0, 'male':1})
```

> drop duplicates

```
df=df.drop_duplicates(keep='first')
```

### > unique values:

- nunique (Series or dataframe)

> merge_asof(df1, df2, by='category', on='col1', direction='forward', allow_exact_matches=False, tolerance=pd.Timedelta('1s))

- df1 left join df2
- on is default looking 'backward'

> drop duplicate

```
df=df.drop_duplicates(subset=['SubportfolioID'], keep='first)
```

> copy dataframe

```
df2 = df.copy()
```

> assign

```
df_all = df_all.assign(column_name=lambda x: (x['col1']/x[`col2`]))
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Timestamp</span>

# <span style="color:green">====================</span>

# <span style="color:green">====================</span>

# <span style="color:blue"> pivot/melt/stack/unstack </span>

# <span style="color:green">====================</span>

# <span style="color:green">====================</span>

# <span style="color:blue"> Groupby</span>

# <span style="color:green">====================</span>

> groupby, transform

> Transform groups

```
def transform_df(source_df): # original dataframe
    group_dfs=[]
    # group and process each groupped dataframe
    for name, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:, 'medium'] = fill_values(group_df['medium])
        group_dfs.append(filled_df)
    new_df = pd.concat(group_dfs)
    return new_df

#> using built-in transform


# transform will call the function for each groupped dataframe
# transform called on a group-dataframe
# operating on each groupped dataframe
# here we only select a column from the group, so the function called by transform receives a series
grouped_medium = df.groupby('artist')['medium']
df.loc[:, 'medium'] = grouped_medium.transform(fill_values) #call transform on groupped dataframe.
```

> filtering grouyp

```
grouped_titles = df.groupby('titles')
condition = lambda x: len(x.index) > 1 # x should be the dataframe of a group
filtered_df = grouped_titles.filter(condition) # remove groups that has only 1 row
```

```
grouped_titles = df.groupby('title')
# size of each group, count of each group
title_counts = grouped_titles.size().size().sort_values(ascending=False)
```

> groupby aggregation

```
grouped_acq_year = df.groupby('artist')['acquisitionYear']
min_acquisition_year = grouped_acq_year.agg(np.min)
or
min_acquisition_year = grouped_acq_year.min()

```

> apply diff aggregation on diff column

```
sector.agg("col1":"sum", "col2":"avg")
```

> Group by

```
df=df.groupby('a_column', as_index=False)['the_column_to_aggregate'].sum()
g=athletes.groupby('nationality')[['gold','silver','bronze']]
g.sum()

# group on multiple columns
atheletes.groupby(['sport', 'nationality'])['gold'].sum()

# first, last -> first/last group row


```

> custom function on group

```
# here custom_function takes a dataframe of a group (or series if only 1 column selected)
groupby.apply(custom_function)
```

> get dataframe of a group

```
sectors.get_group("Energy")
```

# <span style="color:green">====================</span>

# <span style="color:blue"> Multiindex</span>

# <span style="color:green">====================</span>

> create multiindex

```
scoring.set_index(['playerID','year'])
```

> create multiindex from array

```
midx = pd.MultiIndex.from_arrays([months, metrics])
team_splits.columns = midx
```

> multiindex basic operations

```
scoring.groupby(level=1)['goals'].max()
scoring.groupby(level='year')['goals'].max()
```

> multiindex object, multiindex slicing, multiindex sorting

```
idx = pd.IndexSlice
scoring.sort_index() #sort before slicing
scoring.loc[idx['aaltoan01', 1997:2000], :]
scoring.loc[idx[:, 1997:2000], :]

# another sorting example
mi = mi.sort_index(level='year')
```

> is multiindex sorted

```
mi.index.is_lexsorted()
```

> swap index level

```
swapped = mi.swaplevel()

```

> multiindex number of level

```
len(mi.index.levels)
or
mi.index.nlevels
```

> find index of max value in each group, groupby multiindex

```
# this is returning max index of each group by year (remember this is grouping on multiindex)
mi.groupby(level="year")['G'].idxmax().head()

# how to find the whole row from dataframe that is with max value per some kind of groupping?
# retrieving the whole record by idx returned from idxmax
mi.loc[mi.groupby(level="year")['G'].idxmax()].head()
```

> get locations from index slicing

```
# this is getting an list of index locations per a given multiindx slicing
loc = mi.index.get_loc((idx['aaltoan01':'adamscr01'], 1007:2000))
sliced = mi.iloc[locs, :]
```

> get many locs from multiindex; slicing multiindex and use it to retrive rows from original dataframe

```
import numpy as np
def get_many_locs(df, slices):
    arr = np.empty(0, dtype="int")
    for s in slices:
        locs = df.index.get_locs((s))
        arr = np.concatenate((arr, locs))
    return arr


locs = get_many_locs(mi, (idx['aaltoan01':'adamscr01', 1997:2000],
                          idx['aaltoan01':'adamscr01', 2004:206]))

sliced = mi.iloc[locs, :]
```

> stack/undstack multiindex

```
# transpose one level of multiIndex from columns to row (from wide to long dataframe)
team_splits = team_splits.stack(level=0)

# swaplevel, reorder level
team_splits = team_splits.swaplevel(1, 2)

team_splits = team_splits.reorder_level([2,0,1])

# transpose a row index to column
team_splits.unstack(level=['year', 'month'])
```

> change multiIndex name

```
team_splits.index.levels[2].name="month"
```
