def solution(cacheSize, cities):
    cache = []  # 캐시 공간
    time = 0  # 소요 시간
    cache_hit = 1  # Hit 시간
    cache_miss = 5. # Miss 시간

    if cacheSize == 0:  # 0인 경우 
        return len(cities) * cache_miss

    for ref in cities:
        ref = ref.lower()
        if not ref in cache:  # 캐시 안에 ref가 없는 경우
            if len(cache) < cacheSize:  # cacheSize 크기보다 cache 배열의 길이가 낮은 경우
                cache.append(ref)
                time += cache_miss
            else:  # cache 배열의 길이가 모두 찬 경우
                del cache[0]
                cache.append(ref)
                time += cache_miss
        else:  # 캐시 안에 ref가 있는 경우
            del cache[cache.index(ref)]
            cache.append(ref)
            time += cache_hit
    return time