"""
main.py

Python examples demonstrating control flow statements.
"""

def check_number(num):
    if num > 0:
        print(f"{num} is Positive")
    elif num == 0:
        print(f"{num} is Zero")
    else:
        print(f"{num} is Negative")

def main():
    for i in range(-1, 2):
        check_number(i)

if __name__ == "__main__":
    main()
