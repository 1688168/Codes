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

> Java Streams:  
* A tream is a way of supporting functional-style operations on Collections.  In other words, aggregate operations that work on sequences of values.

```java
//on any collection obj
product.stream().filter(Product product -> product.getWeight() < 30)
.sorted(comparingInt(Product::getWeight))
.map(Product::getName)
.forEach(name -> System.out.println(name) 

* method reference
.forEach(System.out::println)
```

> Min/max of array  
```java
import java.util.Arrays;

public class Test {
    public static void main(String[] args){
        int[] tab = {12, 1, 21, 8};
        int min = Arrays.stream(tab).min().getAsInt();
        int max = Arrays.stream(tab).max().getAsInt();
        System.out.println("Min = " + min);
        System.out.println("Max = " + max)
    }
}
```