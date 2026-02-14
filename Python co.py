from collections import OrderedDict

def solve():
    # Read the number of items
    n = int(input())
    
    # Initialize the ordered dictionary
    item_inventory = OrderedDict()
    
    for _ in range(n):
        # Read the line and split into parts
        # Example: "BANANA FRIES 12" -> ['BANANA', 'FRIES', '12']
        data = input().split()
        
        # Join all elements except the last one to get the full item name
        item_name = " ".join(data[:-1])
        
        # The last element is the price
        price = int(data[-1])
        
        # If item exists, add to net_price, else initialize it
        if item_name in item_inventory:
            item_inventory[item_name] += price
        else:
            item_inventory[item_name] = price
            
    # Print the results in order of first occurrence
    for item, net_price in item_inventory.items():
        print(f"{item} {net_price}")

if __name__ == "__main__":
    solve()
