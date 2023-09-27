# $${\color{orange} Python Notes}$$

> How to print python dictionary

```
print(json.dumps(data, indent=4))
```

> How to return PANDAS dataframe as JSON for HTTP response

```
json_data=json.loads(df_data.to_json(orient='records'))
```

> How to convert NAN to None from dataframe

```
df_new = df_old.astype(object).where(df_old.notna(), None)
df_data.replace('N/A', np.nan, inplace=True) # replace 'N/A' with np.nan
df = df.replace({np.nan: None}) # replace non with python  None
```
