__author__ = 'donal'
__project__ = 'rendezview'

from math import radians, cos, sin, asin, sqrt

def haversine((lat1, lon1), (lat2, lon2)):
    """
    Calculate the great circle distance between two points (km)
    on the earth (specified in decimal degrees).

    The 2nd, 3rd, and 4th digits (after the decimal) adds -
    Latitude (1km, 100m, 10m)
    Longitude (150m, 15m, 1m)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers.
    return round(c * r, 2)


if __name__ == '__main__':
    targ = (51.53, -0.14)  # home
    lalos = [
        (51.5006, -0.1228),  # big ben
        # lat adds
        (51.5106, -0.1228),  # big ben + 0.01
        (51.5016, -0.1228),  # big ben + 0.001
        (51.5007, -0.1228),  # big ben + 0.0001
        # long adds
        (51.5006, -0.1328),  # big ben + 0.01
        (51.5006, -0.1238),  # big ben + 0.001
        (51.5006, -0.1229),  # big ben + 0.0001

        (51.541, -0.088),  # office
        (54.5870, -5.3945),  # belfast
        (37.4029937, -122.1811814)  # mountain view
    ]
    dists = [haversine(targ, lalo) for lalo in lalos]
    print dists

    # 51.5412621, -0.08813879999999999