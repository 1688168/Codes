### Regular Expression

[1517]

- raw string
  ```
    def valid*emails(users: pd.DataFrame) -> pd.DataFrame:
        # Note how we use a raw string (putting an `r` in front) to avoid having to escape the backslash
        # Also note that we escaped the `@` character, as it has a special meaning in some regex flavors
        return users[users["mail"].str.match(r"^[a-zA-Z]a-zA-Z0-9*.-]\*\@leetcode\.com$")]
  ```
