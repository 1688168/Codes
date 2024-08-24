> flatmap (merging sub-streams from original stream)
```java
long count =
cities.stream()
    .flatMap(city -> city.getPeople().,stream()) //converting from original stream and convert to a combined new stream
    .count();

cities.stream()
    .flatMap(city -> city.getPeople().,stream()) //converting from original stream and convert to a combined new stream
    .map(p -> getName())
    .forEach(name -> System.out.println(name));
```