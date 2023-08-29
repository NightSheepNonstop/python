def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(ingredient)


make_sandwich('bread')
make_sandwich('bread', 'hotdog')
make_sandwich('bread', 'bacon')
