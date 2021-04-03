def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("Length of the series is bigger than series or zero or -1")
    return [series[i:i+length] for i in range(len(series)) if i+length <= len(series)]


slices("49142", 3)
