* let: variable of let may not be used prior to their declaration
* use let instead of var (declare variable before using it)
* use const whenever possible

> type annotations
* let x: string: 'i will forever be a string'
        ^^^^^^^^
        annotation (but not required, type will be inferred)

> formatted string in typescript
```ts
const varName: varType = varValue;
function logPlayer(name){
    console.log(`New Game Starting for player: ${name}`)
}
```

> how to comment HTML
<!-- stuff -->

> DOM
```yaml
The document Object Model (DOM) connects web pages to JavaScript by representing the structure of a document in memory
```

> union type
* let nullableString: string | null;