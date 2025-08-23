"""
main.py

Python examples demonstrating programming essentials like comments, input/output, and error handling.
"""

def greet(name):
    # This function greets the user by name
    print("Hello, " + name)

def main():
    try:
        name = input("Enter your name: ")
        if not name:
            raise ValueError("Name cannot be empty!")
        greet(name)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
