# --- Day 1: Trebuchet?! ---

def get_first(str):
    for c in str:
        if c.isnumeric():
            return c
        
def get_last(str):
    for c in reversed(str):
        if c.isnumeric():
            return c 
arr = []

with open("data.txt", 'r') as handle:
    for row in handle:
        word = row.rstrip()
        
        first = get_first(word)
        last = get_last(word)
        
        num = int(first + last)
        arr.append(num)


result = sum(arr)

        
        
    

    