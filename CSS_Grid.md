> Basic example

```css
html {
  height: 100%; /* take the whole page */
}

body {
  height: 100%;
  display: grid; /* this specifies compoent is displayed as grid*/
  grid-template-columns: 15em auto 15em; /* 3 columns */
  grid-template-rows: min-content auto min-content; /* 3 rows */
  max-width: 80em;
  margin: auto;
}

header,
footer {
  grid-column-start: 1; /* define beggin/ending of header/footer */
  grid-column-end: 4;
}
```
