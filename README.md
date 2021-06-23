# Dynamic Programming - Salary Work Schedule
You are maintaining a database which recognises criminal DNA. During the study, more criminal DNA will be collected from patients.

Note: DNA is typically represented using A, T, C and G. For the purpose of easy coding, we
will use A, B, C and D (since they have adjacent ASCII values).

## Input
The input to addSequence is a single nonempty string of uppercase letters in uppercase [A-D].

The input to query is a single (possibly empty) string of uppercase letters in uppercase [A-D].

## Output
addSequence(s) should not return anything. It should appropriately store s into the database
represented by the instance of SequenceDatabase. We define the frequency of a particular
string to be the number of times it has been added to the database in this way.
query(q) should return a string with the following properties:
- It must have q as a prefix
- It should have a higher frequency in the database than any other string with q as a
prefix
- If two or more strings with prefix q are tied for most frequent, return the lexicographically
least of them

If no such string exists, query should return None.
 
## Example
```
db = SequenceDatabase()
db.addSequence("ABCD")
db.addSequence("ABC")
db.addSequence("ABC")
db.query("A")
>>> "ABC"
db.addSequence("ABCD")
db.query("A")
>>> "ABC"
db.addSequence("ABCD")
db.query("A")
>>> "ABCD"
de.query("B")
>>> None
```

## Complexity
Remember that string comparison is not considered O(1) in this unit.
- The __init__ method of SequenceDatabase should run in O(1)
- addSequence(s) should run in O(len(s))
- query(q) should run in O(len(q)). Note that although you need to return a string longer
than len(q), since strings are pass-by-reference, returning a string of any length is O(1).

### Disclaimer
1. This case study derives from my school assignment.
2. Details of the actual case study has been sanitized and changed.

