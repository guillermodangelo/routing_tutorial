# routing_tutorial


## Setting up OSRM in Ubuntu using Docker

```bash
mkdir -p /data/osrm/Uruguay

cd /data/osrm/Uruguay

wget https://download.geofabrik.de/south-america/uruguay-latest.osm.pbf

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-extract -p /opt/car.lua /data/uruguay-latest.osm.pbf

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-extract -p /opt/car.lua /data/uruguay-latest.osm.pbf

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-partition /data/uruguay-latest.osrm

docker run -t -v $(pwd):/data osrm/osrm-backend osrm-customize /data/uruguay-latest.osrm

docker run -t -i -p 5000:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/uruguay-latest.osrm
```

## Setting up OSRM in Windows

Using PowerShell, navigate to a directory where you have permissions to read and write.

We'll be using OSM data for the country of Malta, provided by Geofabrik as a PBF file. Download the file and place it in the directory you're working in.

```powershell
md -Force  C:\Users\guillermo\Documents\data\osrm\malta

cd C:\Users\guillermo\Documents\data\osrm\malta

curl.exe -O https://download.geofabrik.de/europe/malta-latest.osm.pbf
```

Now, we'll run the `osrm-extract` and several other commands to extract the data from the PBF file, generate the data for OSRM and partition it for faster routing. The graph will be generated using the car routing profile, there are other profiles available, but we'll stick with the default for now.

```powershell
# osrm-extract
docker run -t -v "$(pwd):/data" osrm/osrm-backend osrm-extract -p /opt/car.lua /data/malta-latest.osm.pbf

# osrm-partition
docker run -t -v "$(pwd):/data" osrm/osrm-backend osrm-partition /data/malta-latest.osrm

# osrm-customize
docker run -t -v "$(pwd):/data" osrm/osrm-backend osrm-customize /data/malta-latest.osrm

```
We're now ready to run the `docker run` command to start the OSRM server. We'll use the `-p` flag to expose port 5000 on the host machine, and the `-v` flag to mount the current directory as `/data` inside the container.

```powershell
# run the container
docker run -t -i -p 5000:5000 -v "$(pwd):/data" osrm/osrm-backend osrm-routed --algorithm mld /data/malta-latest.osrm
```
