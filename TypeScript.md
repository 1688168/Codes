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

> dev console
```yaml
* setting: Log XMLHttpRequests (turn on to show http request in console)

* console.groupCollapsed('a Tag')
* console.dir(data);
* console.table(data);
* console.groupEnd();
* console.assert(data.length === 15, {pieCount: data.length, reason: 'some msg'});
* console.trace();
```

> how to change json to string
* let string = JSON.stringify(data);

> how to create table
```js
data.forEach(element => {
    <tr>
        <td>${element.name}</td>
        <td>${element.description}</td>
        <td>${element.price}</td>
        <td>View Details</td>
    </tr>
})
```

> $0  
* the selected element
* $1 (previous selected)

> add listener to DOM
```js
$0.addEventListener('click', logEvent);
$1.addEventListener('mouseenter', logEvent)
logo.addEventListener('click', (e) => console.log('clicked'));
```

> how to refer to html inner text.
```js
$1.innerText = 'Menu'

document.body.appendChild(document.createElement('h3'));
document.querySelector('h3').innerText="some text in the html h3 tag"
```

> monitor a function, this prints when function is called with inputs
```js
    monitor(aJSFunction);
```

> debug a javascript function, debugging mode
```js
debug(functionName);//this opens debugger when the function is called
```

> export 
```ts
export {a, b, c as aliasName}
export default doSomething;

//we can rename default export to anything
import do from "./module"
```

> import
```ts
import {StaffMember as CoWorker} './person';
import * as HR from './person'
```
* node, document, DOM hierarchy
![react](./rcs/react001.png)
* How to walk the nodes
![react](./rcs/react002.png)
![react](./rcs/react003.png)
![react](./rcs/react004.png)
![react](./rcs/react005.png)

> what is react
* react component -> return JSX -> Babel -> javascript -> webpack

> next commands
```sh
create-next-app globomantics
```

> react avoid recreating function
```
//if we do not use useCallBack, each time the function called, we will recreate the function reference and that might trigger re-rendering to degrade the performance
const setHouseWrapper = 
    useCallback((house) => {setSelectedHouse(house)}, []);
```

> arrays  
```ts
//declare array
let arr: Array<object> = [];
int arr: object[] = [];
let arr: Array<string> = new Array();
let arr: Array<string> = Array();
let arr: Array<Array<string>> = [];

let arr: number[] = [];
```