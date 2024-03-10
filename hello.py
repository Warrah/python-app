def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    num = int(input("Enter a positive integer: "))
    result = fibonacci(num)
    print("Fibonacci sequence for", num, "is:", result)

if __name__ == "__main__":
    main()
