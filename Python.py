import string

def print_rangoli(size):
    # Get all lowercase letters
    alphabet = string.ascii_lowercase
    
    # List to store each line of the rangoli
    lines = []
    
    for i in range(size):
        # Pick the letters for the current row
        # For size 3, row 0 uses 'c', row 1 uses 'c-b', row 2 uses 'c-b-a'
        s = "-".join(alphabet[size-1 : size-1-i : -1] + alphabet[size-1-i : size])
        
        # Center the string with dashes based on the maximum width
        width = 4 * size - 3
        lines.append(s.center(width, "-"))
    
    # Join the top half, the middle, and the bottom (reversed top)
    # The [:-1] slice excludes the middle line from the reversed list
    rangoli = "\n".join(lines + lines[::-1][1:])
    print(rangoli)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)