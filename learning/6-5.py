rivers={'nile':'egypt','Yellow River':'China','Yangtze River':'China'}
for key,value in rivers.items():
    print(f"The {key} runs through {value}.")
for key in rivers.keys():
    print(key.title())
for value in rivers.values():
    print(value.title())
