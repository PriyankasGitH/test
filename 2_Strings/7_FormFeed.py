"""

In Python, the form feed character \f is used to represent a page break.
It is often used in text processing to denote a point where the content should move to a new page.

"""
print("======== Using escape sequence for form feed ========")
# Example of using form feed character in Python

text1 = "This is the first page."
text2 = "This is the second page."

# Using the form feed character to separate the pages
document = text1 + "\f" + text2

# Printing the document
print(document)

# Splitting the document based on the form feed character
pages = document.split("\f")

# Displaying each page separately
for i, page in enumerate(pages, start=1):
    print(f"Page {i}:")
    print(page)
    print()