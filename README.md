# Algorithms-and-Data-Structures

A set of data structures and algorithms, written in Python and Java

## Uses
### Sorts:
```python
from Sorts import Sorting
print(Sorting.radix_sort([4, 3, 2, 1]))
# [1, 2, 3, 4]
```

### Shunting Yard:
```python
from shuntingYard import PostFix
print(PostFix.convert('x+y'))
# 'xy+'
print(PostFix.evaluate('1 2 +'))
# 3
```

### List implemented with a Triple Ended Queue:
```java
// Improves Efficiency for operations on the front, middle, and end
List<Integer> l = new TripleEndedQueue<>(Integer.class);
// Add 1,000,000 elements quickly in the middle of the list
// METHODS: add(i, x), add(x), get(i), set(i, x), remove(i), size()
for (int i = 0; i < 1000000; i++)
    l.add(Math.floorDiv(l.size(), 2), i);
System.out.println(l.get(0));
// 1
```

### List Implemented with a Rootish Array Deque:
```java
List<Integer> rad = new RootishArrayDeque<Integer>(Integer.class);
int K = 1000000;

System.out.print("Appending " + K + " items...");
System.out.flush();

for (int i = 0; i < K; i++) {
    rad.add(i);
}

System.out.print("Prepending " + K + " items...");
System.out.flush();

for (int i = 0; i < K; i++) {
    rad.add(0, i);
}

System.out.print("Removing " + K + " items from the back...");
System.out.flush();

for (int i = 0; i < K; i++) {
    rad.remove(rad.size()-1);
}

System.out.print("Removing " + K + " items from the front...");
 System.out.flush();

for (int i = 0; i < K; i++) {
    rad.remove(0);
}
```

### Table:
```java
Table<Integer> v = new Table<>();
for (int i = 0; i < 5; i++)
     v.addCol(v.cols());
for (int i = 0; i < 5; i++)
    v.addRow(v.rows());
v.set(0,0,1);
v.set(1,1,1);
v.set(2,2,1);
v.set(3,3,1);
v.set(4,4,1);
System.out.println(v.toString());
/**
    1 null null null null 
    null 1 null null null 
    null null 1 null null 
    null null null 1 null 
    null null null null 1
*/
```

## Author

* **Jonathan Scala** - *December 8, 2017*
