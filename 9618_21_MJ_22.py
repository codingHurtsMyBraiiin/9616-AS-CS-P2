"""
6 (a) 
An algorithm will:
    • output each integer value between 100 and 200 that ends with the digit 7, for example, 107
    • output a final count of the number of values that are output.
Write pseudocode for this algorithm.
Any variables used must be declared.

"""

sevens = 0

for i in range(100, 200):
    string_num = str(i)
    if string_num[2] == "7":
        sevens += 1

print (f"final count: {sevens}")
