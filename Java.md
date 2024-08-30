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

```java
//convert a list to map
Map<String, Long> lightProducts = products
.stream()
.filter(product -> product.getWeight() < 30)
.sorted(comparingInt(Product::getWeght))
.collect(groupingBy(Product::getName, counting()))
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

> Optional:  
* as a safe alternative to Null
* an Optional is a container that can either contain a value or be empty
* Optional is an immutable value class (Should NOT be used for synchronization)
* Optional was primarily designed to be used as a return type for methods.
* Optional can NOT be serialized.  -> cannot be used as return type that need to be seralized.

```java  
//consider an legacy function that could return null, we want to convert it to return Optional
Optional<Product> optional2 = Optional.ofNullable(getProductById(12345)); //to convert getProductById which could return null to become return Optional

//convert to another value if null
Product product = optional.orElse(new Product());
Product product1 = optional.orElse(null); //orElse takes a value
Product product2 = optional.orElseGet(() -> Product.PRODUCTS.get(RANDOM.nextInt(Product.PRODUCTS.size()))); //orElseGet takes a supplier
Product product3 = optional.orElseThrow(); //returns the value or throw NoSuchElement if empty
Product product4 = optional.orElseThrow(() -> new IllegalStateException("ErrorMsg")); //2nd form, takes supplier
```

> Optional with Stream

```java
//ex1:
return Product.PRODUCT.stream().filter(product -> product.id()==productId).findFirst(); //this returns an optional for the 1st element of the stream after filter

//ex2:
optional.ifPresent(product -> System.out.println("Found product: " + product));

//ex3: 
optional.ifPresentOrElse(
    product -> System.out.println("Found product: " + product), //argument 1
    () -> System.out.println("Product not found"));
)

```

> Optional with functional programming: map, filter
```java
// map
    String text = optional.map(Product::name).orElse("Product not found"); //transform an optinal to an String

// filter
    Set<Long> discountedProductIds = Set.of(1231L, 4343L, 23423432L);
    System.out.println(optional.filter(product -> discountedProductIds.contains(product.id()))
    .map(product -> "Discounted product: " + product.name())
    .orElse("No discounted product")
    );


Set<Long> productIds = Set.of(3132L, 23234L, 982342L);
List<Product> products = productIds.stream()
.map(OptionalExample02::findProductById) //stream of optional of product
.flatMap(Optional::stream) //flat out the optional result
.toList();//convert to list
```

* [Google Guice Tutorial](https://github.com/mvpjava/google-guice-tutorials)