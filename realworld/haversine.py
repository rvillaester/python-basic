import math

def calculateDistance(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin( (lat2 - lat1) / 2 ) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2 ) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))

if __name__ == '__main__':
    lat1 = 14.599512
    lon1 = 120.98422
    lat2 = -33.86882
    lon2 = 151.209296
    d = calculateDistance(lat1, lon1, lat2, lon2)
    print(d)