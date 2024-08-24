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

> create stream from array
```java
Person[] people = {p01, p02, p03};
Stream<Person> peopleStream = Arrays.stream(people);
Stream<Person> peopleStream = Stream.of(people);
```