```java
package files;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Date;

public class FileToPathConversion {

    static String filePath = "m6io/src/main/resources/modules.txt";

    public static void main(String[] args) {

        File file = new File(filePath);//[java][file]
        System.out.println(file.exists());//[java][file][exist]

        Path path = Path.of(filePath);//[java][path] -- java will figure out the correct separator
        System.out.println(Files.exists(path));

        Path path2 = file.toPath();//[java][from file to path]
        System.out.println(Files.exists(path2));
    }
}

```