* let: variable of let may not be used prior to their declaration
* use let instead of var (declare variable before using it)
* use const whenever possible

> type annotations
* let x: string: 'i will forever be a string'
        ^^^^^^^^
        annotation (but not required, type will be inferred)

> formatted string in typescript
```ts
function logPlayer(name){
    console.log('New Game Starting for player: $(name)')
}
```