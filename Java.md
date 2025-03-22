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
//convert a list to 
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
```java
//optional return null if no value
import java.util.Optional;

public class Example {

    public static void main(String[] args) {
        Optional<String> optionalValue = Optional.of("Hello");//how to assign value to optional

        String result = optionalValue.orElse(null);  //retrieve optional value if present otherwise return null

        System.out.println(result); // Output: Hello

        Optional<String> emptyOptional = Optional.empty();

        String result2 = emptyOptional.orElse(null); 

        System.out.println(result2); // Output: null
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
//returning optional
return Optional.of(product); //if we found the product
return Optional.empty(); //if product is NOT found

//if the function return type is NOT optional. converting it to become optional
Optional<Product> optional = Optional.ofNullable(findProductById(23423));

//how to process optional return 
if(optional.isPresent()){
    Product product = optional.get();
}else{

}
```

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
> Java optional, return null if not present
```java
final var someVar =someOptional.orElse(~~null~~);
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
.flatMap(Optional::stream) //flat out the optional result, (null is removed)
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

> check string only contains digit
```java
package strings;

public class ContainOnlyDigitDemo {

    private static final String ONLY_DIGITS = "123456789";
    private static final String NOT_ONLY_DIGITS = "123456789A";

    public static void main(String[] args) {


        System.out.println("Character.isDigit() solution:");


        boolean onlyDigitsV11 = containsOnlyDigitsLoop(ONLY_DIGITS);
        boolean onlyDigitsV12 = containsOnlyDigitsLoop(NOT_ONLY_DIGITS);

        System.out.println("Contains only digits: " + onlyDigitsV11);
        System.out.println("Contains only digits: " + onlyDigitsV12);

        System.out.println();
        System.out.println("Java 8, functional-style solution:");

        boolean onlyDigitsV31 = containsOnlyDigitsFunctional(ONLY_DIGITS);
        boolean onlyDigitsV32 = containsOnlyDigitsFunctional(NOT_ONLY_DIGITS);

        System.out.println("Contains only digits: " + onlyDigitsV31);
        System.out.println("Contains only digits: " + onlyDigitsV32);


        System.out.println();
        System.out.println("String.matches() solution:");


        boolean onlyDigitsV21 = containsOnlyDigitsRegex(ONLY_DIGITS);
        boolean onlyDigitsV22 = containsOnlyDigitsRegex(NOT_ONLY_DIGITS);


        System.out.println("Contains only digits: " + onlyDigitsV21);
        System.out.println("Contains only digits: " + onlyDigitsV22);


    }

    public static boolean containsOnlyDigitsLoop(String str) {
            for (char c : str.toCharArray()) {
                if(!Character.isDigit(c)) {
                    return false;
                }
            }
            return true;
    }

    public static boolean containsOnlyDigitsFunctional(String str) {

            return str.chars().allMatch(Character::isDigit);
    }

    public static boolean containsOnlyDigitsRegex(String str) {

            return str.matches("[0-9]+");
    }
}
```

> check string only contains digit  (functional solution)
```java
package strings;

import java.util.function.IntPredicate;
import java.util.function.Supplier;

public class ContainsOnlySpecificCharDemo {

    private static final String ONLY_DIGITS = "123";
    private static final String NOT_ONLY_DIGITS = "123A";
    private static final String ONLY_LETTERS = "ABC";
    private static final String NOT_ONLY_LETTERS = "ABC1";


    public static void main(String[] args) {

        IntPredicate isDigit = Character::isDigit;
        IntPredicate isLetter = Character::isLetter;
        IntPredicate isLetterOrDigit = Character::isLetterOrDigit;

        System.out.println(containsOnlyCharacter(ONLY_DIGITS, isDigit));

    }


    public static boolean containsOnlyCharacter(String str, IntPredicate predicate) {
            return str.chars().allMatch(predicate);
    }


    public static boolean containsOnlyCharacter(String str, String regex) {
        return str.matches(regex);
    }


}
```
> search replace

```java
package strings;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FindAndReplaceDemo {

    public static void main(String[] args) {
        findMatches();
        replace();
    }

    public static void findMatches() {
        String str = "Java 17 Recipes!";

        System.out.println(str.matches("Java 17 Recipes!"));    // exact match - true
        System.out.println(str.matches("Java 17"));             // not exact match - false


        System.out.println(str.matches("[Jj]ava.*"));               // true
        System.out.println(str.matches("Java [0-9]+ Recipes!"));    // true


    }

    private static void replace() {
        String str = "11 Recipes for Java11";
        System.out.println(str.replace("11", "17"));    // replaces all, but takes a char sequence
        System.out.println(str.replaceAll("11", "17")); // replaces all, but takes a regex
        System.out.println(str.replaceFirst("11", "17"));
    }

}
```

>  stream of line
```java
package strings;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.stream.Stream;

public class StreamLinesDemo {

    public static void main(String[] args) {

        String str = "To whom it may concern \n" +
                "I wish you a good day \n" +
                "Sincerely \n" +
                "Me";

        Stream<String> lines = str.lines();

        // add line numbers
        final AtomicInteger i = new AtomicInteger(1);
        lines.forEach(line -> System.out.println(i.getAndIncrement() + " " + line)); //process line by line
    }
}
```

> Tokenization

```java
package strings;

public class TokenizeDemo {

    public static void main(String[] args) {

        String str = "To whom it may concern \n" +
                "I wish you a good day \n" +
                "Sincerely \n" +
                "Me";

        String[] lines = str.split("\n");
        var sb = new StringBuilder();
        for(String line : lines) {
            sb.append("-> ").append(line);
        }
        System.out.println(sb);

        String text = "Tokyo, 37000000, New York, 20000000, Paris, 11000000";
        String[] lines2 = text.split(",");

        for(int i = 0 ; i < lines2.length ; i = i+2) {
            System.out.println(lines2[i]);
        }

        for(String line : str.split("\n")) {
            for(String token : line.split(",")) {

            }
        }
    }
}
```

> join string
```java
package strings;

import java.util.Objects;
import java.util.StringJoiner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class JoinStringsDemo {

    public static void main(String[] args) {

        String delimiter = ";";
        String[] strings = {"11", "12", null, "13", "14", "15", "16", "17"};

        System.out.println(joinOldWay(delimiter, strings));
        System.out.println(joinSimplest(delimiter, strings));
        System.out.println(joinWithJoiner(delimiter, strings));
        System.out.println(joinWithStream(delimiter, strings));
    }

    public static String joinOldWay(String delimiter, String... args) {

        StringBuilder result = new StringBuilder();

        int i;
        for (i = 0; i < args.length - 1; i++) {
            result.append(args[i]).append(delimiter);
        }

        result.append(args[i]);
        return result.toString();
    }


    public static String joinSimplest(String delimiter, String... args) {
        return "[" + String.join(delimiter, args) + "]";
    }

    //to avoid duplication -- since java8
    public static String joinWithJoiner(String delimiter, String... args) {
        var joiner = new StringJoiner(delimiter, "{", "}");
        for(String arg : args) {
            joiner.add(arg);
        }
        return joiner.toString();
    }

    public static String joinWithStream(String delimiter, String... args) {
        return Stream.of(args)
                .filter(Objects::nonNull) //filter out null string
                .filter(s -> !s.isEmpty())
                .collect(Collectors.joining(delimiter));
    }
}
```

> StringBuilder  

```java
var builder = new StringBuilder("abc").reverse();//use stringBuilder to reverse a string
//stringbuilder methods
//delete()
//insert()
//replace()
//reverse()
...

package strings;

public class BuildStringsInLoop {

    public static void main(String[] args) {
        //use stringBudder if you need thread-safe
        var builder = new StringBuffer("abc").reverse();    // thread-safe

        System.out.println(builder);

    }
}
```

> multiline string/text block
```java
package strings;

public class MultilineStringsDemo {

    public static void main(String[] args) {

        String str = """
                To whom it may concern
                I wish you a good day
                Sincerely
                Me""";


        String textBlock =
                """
                        <html>
                            <body>
                                <tag>
                                </tag>
                            </body>
                        </html>""";

    }
}
````



> random string

```java
package strings;

import java.util.UUID;

public class RandomString {

    public static void main(String[] args) {

        for (int i = 0; i < 10; i++) {
            String uuid = UUID.randomUUID().toString();
            System.out.println(uuid.replace("-", "").substring(0, 10));
        }

    }
}   
```


> Apache Commons
```java
//StringUtils
package strings;

import org.apache.commons.lang3.RandomStringUtils;
import org.apache.commons.lang3.StringUtils;

public class ApacheDemo {

    public static void main(String[] args) {

        System.out.println(StringUtils.stripAccents("éclair"));  // eclair

        System.out.println(StringUtils.abbreviate("This is a long text", 10));

        System.out.println(RandomStringUtils.randomAlphabetic(2, 10));

    }
}
```


```java
package strings;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

public class ProgramDemo {

    static String text = """
            Tokyo,    37000000
            New York, 20_000_000
            Paris,    11.000.000
            """;
    public static void main(String[] args) {

        List<String> populations = new ArrayList<>();
        String[] lines = text.split("\n");
        for(String line : lines) {
            String population = line.split(",")[1];
            String sanitized = population.replaceAll("[^\\d]","");
            populations.add(sanitized);
        }

        System.out.println(populations);



        List<String> populations2 = text.lines() //process multi-line text line by line
                .map(line -> line.split(",")[1])
                .map(population -> population.replaceAll("[^\\d]",""))
                .toList();

        System.out.println(populations2);

        Function<String, String> extractSecondToken = line -> line.split(",")[1];
        Function<String, String> sanitizeNumber = numberAsString -> numberAsString.replaceAll("[^\\d]","");

        List<String> populations3 = text.lines()
                .map(extractSecondToken.andThen(sanitizeNumber))
                .toList();

    }
}
```

> java stream initialize two dimentional array
```java
int a = 4;               // Number of outer array elements
int b = 2;               // Number of inner array elements

int[][] board = IntStream
    .range(0, a)                                               // iterate 0..3
    .mapToObj(i -> IntStream.range(0, b)                       // for each iteratoe 0..1
                            .map(j -> 1 + (i + (a + 1) * j))   // calculate the value
                            .toArray())                        // compose the inner array
    .toArray(int[][]::new); 

// initialize two dimentional array with max Int
  int[][] dp = IntStream.range(0, N+1)
                              .mapToObj(ii->IntStream.range(0, k+1).map(jj -> Integer.MAX_VALUE).toArray())
                              .toArray(int[][]::new);
```


//Java read a CSV and process line by line
```java
Path path = Path.of("./someDir/file.csv")

//this is stream of Object (T)
try (Stream<String> lines = File.lines(path, StandardCharsets.ISO_8859_1);){
    //do your thing
    lines.skip(2)
         .map(line -> lineToDensity.apply(line))
         .max(Comparator.naturalOrder())
         .orElseThrow();
    ;//skip headers
}catch (IOException e){
    e.printStackTrace();
}
```