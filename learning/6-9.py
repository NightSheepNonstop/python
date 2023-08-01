favorite_places = {
  'Chen': ['Beijing', 'Shanghai'],
  'Wang': ['Wuhan', 'Changsha'],
  'Li': ['Xiamen', 'Dalian']
}
for name,places in favorite_places.items():
    print(f"{name}'s favorite places are ")
    for place in places:
        print(place)
