def add_to0(num, target=[]):
    target.append(num)
    return target

def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(add_to(1,[1]))
print(add_to(2))
print(add_to(3))
