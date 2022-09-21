def solution(cacheSize, cities):
    cache = []
    time = 0
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        name = city.lower()
        if name not in cache:
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(name)
        else:
            temp = cache.pop(cache.index(name))
            cache.append(temp)
            time += 1

    return time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork",
      "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju",
      "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
