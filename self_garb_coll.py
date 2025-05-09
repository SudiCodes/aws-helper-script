import gc

class Node():
    def __init__(self,name):
        self.name = name
        self.partner = None
        
    def __repr__(self):
        return f"<Node {self.name}>"
    

gc.enable()
gc.set_debug(gc.DEBUG_UNCOLLECTABLE | gc.DEBUG_STATS )

def make_cycle():
    a = Node("A")
    b = Node("B")
    
    a.partner = b
    b.partner = a
    
    return None

make_cycle()


print("Collecting ...")
n = gc.collect()
print(f"Unreachable objects found and collected: {n}")