import requests
import mapbox_vector_tile

# Define tile coordinates (z, x, y) and profile
z, x, y = 12, 2213, 1609  # Example tile covering central Malta

# Fetch tile
url = f"http://127.0.0.1:5000/tile/v1/car/tile({x},{y},{z}).mvt"

response = requests.get(url)

if response.status_code == 200:
    # Decode MVT data
    tile_data = mapbox_vector_tile.decode(response.content)
    print(f"Layers in tile: {list(tile_data.keys())}")
    
    # Extract road data (layer name varies by OSRM version)
    roads = tile_data.get("road", [])
    print(f"Found {len(roads)} road features in tile.")
else:
    print(f"Error fetching tile: HTTP {response.status_code}")



    import math
def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 1 << zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
  return xtile, ytile

deg2num(35.8989, 14.5144, 12)