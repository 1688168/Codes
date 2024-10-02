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

> type assertion (type casting)
```
let value: any = 5;
let fixedString: string = (<number>value).toFixed(4); //cast the value to a "number" type and apply the method of number type

let fixedString: string = (value as number).toFxied(4); //same as <number>
```

> type analysis
```ts
var messagesElement: HTMLElement | string;
if(typeof messagesElement === 'string'){
    return messagesElement; //this is a string
}else{
    return messageElement; //this is a HTMLElement
}
```

> default initialized parameters
```ts
function sendGreeting(greeting: string = 'Good morning'): void {
    console.log(greting);
}
```

> static member  

> constructors  
```ts
class Developer {
    constructor(){ //constructor name is always constructor
        console.log('Stuff');
    }
}

class WebDeveloper extends Developer {
    readonly favoriteEditor: string;
    constructor(editor: string){
        super();
        this.favoriteEditor = editor;
    }
}
//parameter property
class Game {
    constructor(public player: Player, public problemCount: number, public factor: number);
}
```


> Async, try/catch/finally pattern
```ts
async function example(){
    let hero: Hero;
    try{
        hero = await getHero(email);
        hero.order = await getOrders(hero);
    } catch (error) {
        showMessage(error);
    }finally {
        showProgressbar(false);
    }

    showHero(hero);
}
```

> async/await example
```ts
async function renderHeroesAsync() {
  showFetching();
  showMessage();
  try {
    const heroes = await getHeroesViaAsyncAwait();
    showHeroes(heroes);
  } catch (error) {
    handleErrors(error);
  } finally {
    wrapUp();
  }
}
```

> typescript array
```ts
const heros = [] as Hero[];
```

> promise.all
```ts
 const [orders, accountRep] = await Promise.all([
    getOrdersAsync(hero.id),
    getAccountRepAsync(hero.id)
 ]);
```

> async using map
```ts
const getAllStatusesAsyc = orders.map(
    async (o: Order) => await getShippingStatusAsync(o.num);
);

const shippingStatuses = await Promise.all(getAllStatusesAsync);
```


> how to print message on browser
* showMessages(`the msg [${var}]`);


> some async functions
* setTimeout
* setInterval


> plugins to install
* ESLint extension
* prettier extension