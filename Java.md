# <span style="color:purple">Java</span>

> Exceptions
```java
try{

}catch (Exception ex){
    System.outprintln("Error: " + ex.getMessage());
    ex.printStackTrace();
}
```

> Array  
```java
//declare an array and initialize with value
Product[] products = {door, fllorPanel}

//copy an array and make it bigger
var newArray = Arrays.copyOf(array, length+1);
newArray[array.length] = product;


```

> User Inputs
```java
    Scanner scanner = new Scanner(System.in);
    scanner.nextLine();//read user inputs until user hit enter
```