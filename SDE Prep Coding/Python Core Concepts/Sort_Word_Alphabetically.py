# Python Code Challenge #3: Sort a String

#Your goal is to implement a function, `sort_words()`, that takes a string containing one or more words separated by spaces as the input argument and returns a string containing those words sorted alphabetically.

## Example Test Output
def sort_words(String):
    Splitted_String = String.split()
    print(" ".join(sorted(Splitted_String, key=str.title)))


sort_words('banana ORANGE apple')

#Output : 'apple banana ORANGE'




