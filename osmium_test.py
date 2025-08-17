"""
Output an OSM file as geojson to a file.

This demonstrates how to use the GeoJSON factory.
"""
import sys
import json
import osmium

geojsonfab = osmium.geom.GeoJSONFactory()


class GeoJsonWriter(osmium.SimpleHandler):

    def __init__(self, output_file):
        super().__init__()
        self.output_file = output_file
        # write the Geojson header
        self.output_file.write('{"type": "FeatureCollection", "features": [\n')
        self.first = True

    def finish(self):
        self.output_file.write('\n]}')

    def node(self, n):
        if n.tags:
            self.write_object(geojsonfab.create_point(n), n.tags)

    def way(self, w):
        if w.tags and not w.is_closed():
            self.write_object(geojsonfab.create_linestring(w), w.tags)

    def area(self, a):
        if a.tags:
            self.write_object(geojsonfab.create_multipolygon(a), a.tags)

    def write_object(self, geojson, tags):
        geom = json.loads(geojson)
        if geom:
            feature = {'type': 'Feature', 'geometry': geom, 'properties': dict(tags)}
            if self.first:
                self.first = False
            else:
                self.output_file.write(',\n')

            self.output_file.write(json.dumps(feature))


def main(osmfile, output_filename):
    print(f"Processing {osmfile}...")
    with open(output_filename, 'w', encoding='utf-8') as f:
        handler = GeoJsonWriter(f)
        handler.apply_file(osmfile,
                         filters=[osmium.filter.EmptyTagFilter().enable_for(osmium.osm.NODE)])
        handler.finish()
    
    print(f"Successfully wrote output to {output_filename}")
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python %s <osmfile> <output.geojson>" % sys.argv[0])
        sys.exit(-1)
    
    try:
        sys.exit(main(sys.argv[1], sys.argv[2]))
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)