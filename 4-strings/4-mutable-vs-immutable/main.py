# Mutable vs Immutable Strings - Python Example

text = "hello"
print("Original text:", text)

new_text = text.replace('h', 'j')
print("New text after replace:", new_text)
print("Original text remains:", text)  # unchanged (immutable)
