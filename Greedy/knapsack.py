#Greedy fractional knapsack

def knapsack(w,array):

    array.sort(key=lambda x: (x.value/x.weight),reverse=True)

    total =0.0

    for item in array:
        if item.weight <= w:
            w -= item.weight
            total += item.value
        else:
            total += item.value * (w/item.weight)
            print("getting a fraction")
            break
    return total

class Item:
    def __init__(self,weight,value):
        self.weight = weight
        self.value = value

if __name__ == '__main__':
    w = 8
    array = [Item(1,200),Item(3,240),Item(2,140),Item(5,150)]
    print(knapsack(w,array))
