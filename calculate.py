
from geopy.geocoders import Nominatim
import geopy.distance

geolocator = Nominatim(user_agent="DistanceCalculator")


def get_lat_long(city):
    country = "United States"
    loc = geolocator.geocode(city + ", " + country)

    return [loc.latitude, loc.longitude]


def calculateDistance(lat1, lon1, lat2, lon2):
    coord1 = (lat1, lon1)
    coord2 = (lat2, lon2)

    return geopy.distance.geodesic(coord1, coord2).miles


def main():
    place1 = "Dallas"
    place2 = "Houston"

    position1 = get_lat_long(place1)
    position2 = get_lat_long(place2)

    distance = calculateDistance(
        position1[0], position1[1], position2[0], position2[1])

    print(distance)


if __name__ == '__main__':
    main()
