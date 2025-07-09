# routing_tutorial


## Setting up OSRM in Ubuntu using Docker

mkdir -p /data/osrm/Uruguay

cd /data/osrm/Uruguay

wget https://download.geofabrik.de/south-america/uruguay-latest.osm.pbf

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-extract -p /opt/car.lua /data/uruguay-latest.osm.pbf

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-extract -p /opt/car.lua /data/uruguay-latest.osm.pbf

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-partition /data/uruguay-latest.osrm

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-customize /data/uruguay-latest.osrm

docker run -t -i -p 5000:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/uruguay-latest.osrm


## Setting up OSM in Windows

Using PowerShell, navigate to a directory where you have permissions to read and write.

```powershell
md -Force  C:\Users\guillermo\Documents\data\osrm\malta

cd C:\Users\guillermo\Documents\data\osrm\malta

curl.exe -O https://download.geofabrik.de/europe/malta-latest.osm.pbf
```

osrm-extract
docker run -t -v "$(pwd):/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/malta-latest.osm.pbf

osrm-partition
docker run -t -v "$(pwd):/data" osrm/osrm-backend osrm-partition /data/malta-latest.osrm

osrm-customize
docker run -t -v "$(pwd):/data" osrm/osrm-backend osrm-customize /data/malta-latest.osrm

run the container
docker run -t -i -p 5000:5000 -v "$(pwd):/data" osrm/osrm-backend osrm-routed --algorithm mld /data/malta-latest.osrm


