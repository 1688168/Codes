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

> remove white spaces
```java
package strings;

public class RemoveSpacesDemo {

    public static void main(String[] args) {

        System.out.println("hello   ".trim() + "     there".trim());

        char space = '\u2002';
        System.out.println("\\u2002 is whitespace: " + Character.isWhitespace(space));

        System.out.println("hello\u2002".trim() + "\u2002there".trim());
        //strip is unicode-aware evolution of trim()
        //we should use strip whenever possible
        //strip is added after java11
        System.out.println("hello\u2002".strip() + "\u2002there".strip());

    }
}
```

> how to check empty string

```java
        System.out.println("isEmpty()");
        System.out.println("".isEmpty());           // True

        System.out.println("\r".isEmpty());         // False
        System.out.println("\u2002".isEmpty());     // False
        System.out.println(" ".isEmpty());          // False

        System.out.println("isBlank()");
        System.out.println("".isBlank());           // True
        System.out.println("\r".isBlank());         // True
        System.out.println("\u2002".isBlank());     // True
        System.out.println(" ".isBlank());          // True

        System.out.println("Careful!");
        String evilString = "\u2002";
        System.out.println(evilString.trim().isEmpty());        // False! But you might have expected true

        System.out.println(evilString.strip().isBlank());       // redundant
        System.out.println(evilString.isBlank());               // true
```

> [transforming string](https://github.com/andrejs-ps/Java17-Playbook/blob/main/m2strings/src/main/java/strings/TransformStringDemo.java)

```java
package strings;

public class TransformStringDemo {

    public static void main(String[] args) {

        String lotteryWin = " 100 usd ";
        String result  = lotteryWin
                .replaceAll("[a-z]", "")
                .strip();

        String formattedResult = formatNumber(result);
        System.out.println(formattedResult.toUpperCase());

        String finalResult = lotteryWin
                .replaceAll("[a-z]", "")
                .strip()
                .transform(TransformStringDemo::formatNumber)
                .toUpperCase();

        System.out.println(finalResult);


        String finalResult2 = lotteryWin //only use transform for string
                .transform(s -> s.replaceAll("[a-z]", ""))
                .transform(String::strip)
                .transform(TransformStringDemo::formatNumber)
                .transform(String::toUpperCase);

        System.out.println(finalResult2);

    }

    private static String formatNumber(String num) {
        if(Integer.parseInt(num) < 100) {
            return "Nice! You've won: " + num;
        } else {
            return "Great news! You've won: " + num;
        }
    }
}
```

```java
package strings;

public class IterateOverCharactersDemo {

    public static void main(String[] args) {

        String str = "some string";

        for(int i = 0, n = str.length() ; i < n ; i++) {
            char c = str.charAt(i);
            // do things with the char
        }

        for(char c : str.toCharArray()) {//converting string to char array
            System.out.println(c);
        }

        System.out.println("Specific char to uppercase: ");
        System.out.println(charToUpperCase(str, 's'));
        System.out.println(charToUpperCase(str, 'g'));
    }


    // uppercase -> uPPercase
    private static String charToUpperCase(String str, char charToUpper) {
        var sb = new StringBuilder();
        for(char c : str.toCharArray()) {
            char charToAppend = c == charToUpper ? Character.toUpperCase(c) : c;
            sb.append(charToAppend);
        }
        return sb.toString();
    }

}
```