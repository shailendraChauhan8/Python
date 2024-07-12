def fibonacci_series(n):
    a, b = 0, 1
    count = 0
    
    while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1

# Number of terms to generate
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacci_series(num_terms)
