def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# positional arguments
greet_with("Hana", "Japan")
# greet_with("Nowhere", "Hana") -> here positional arguments show its affection.

# keyword arguments -> keyword arguments solve positional arguments' problems.
greet_with(location="Japan", name="Hana")