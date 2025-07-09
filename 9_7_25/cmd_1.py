import sys
import ast
a = sys.argv[1:]
parsed = []
for item in a:
    try:
        val = ast.literal_eval(item)
    except (ValueError, SyntaxError):
        val = item
    parsed.append(val)
print("Original args:", a)
print("Parsed args:", parsed)
ints = [x for x in parsed if isinstance(x, int)]
floats = [x for x in parsed if isinstance(x, float)]
strs = [x for x in parsed if isinstance(x, str)]
lists = [x for x in parsed if isinstance(x, list)]
tuples = [x for x in parsed if isinstance(x, tuple)]
dicts = [x for x in parsed if isinstance(x, dict)]
sets = [x for x in parsed if isinstance(x, set)]
print("Ints:", ints)
print("Floats:", floats)
print("Strings:", strs)
print("Lists:", lists)
print("Tuples:", tuples)
print("Dicts:", dicts)
print("Sets:", sets)