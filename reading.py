def convert(val):
    """
    Converts string to correct datatype

    Agrs:
    - val (str): object to convert to correct datatype

    Returns:
    - Any: converted object
    """
    # Check integer
    if val.isdigit():
        return int(val)
    
    # Check float
    if all([deel.isdigit() for deel in val.split('.')]):
        return float(val)
    
    
    # Check string
    if '"' in val:
        return val.replace('"', '')
    
    return val

with open('data.txt', 'r') as f:
    headers = f.readline().strip().split(',')
    data = []
    for line in f.readlines():
        values = [convert(val) for val in line.strip().split(',')]
        data.append(dict(zip(headers, values)))

filtered_data = filter(lambda x: x['var2'] > 1.5, data)
for x in filtered_data:
    print(x)