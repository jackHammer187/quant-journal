def mean_std(xs):
    n = len(xs)
    mean = sum(xs) / n
    total_sq = 0
    for x in xs:
        total_sq += (x - mean) ** 2  
    std = (total_sq / n) ** 0.5 
    return mean, std

print(mean_std([2, 4, 4, 4, 5, 5, 7, 9]))
