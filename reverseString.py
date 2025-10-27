# Python program to reverse a string using backward traversal

def reverseString(s):
    res = []
  
    # Traverse on s in backward direction
    # and add each character to the list
    for i in range(len(s) - 1, -1, -1):
        res.append(s[i])

    # Convert list back to string
    return ''.join(res)

if __name__ == "__main__":
    s = "abdcfe"
    print(reverseString(s))
