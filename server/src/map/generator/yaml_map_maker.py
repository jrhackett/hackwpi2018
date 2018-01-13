import os
import yaml

from server.src.map.map import Map

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class YamlMapMaker:

    def __init__(self, yaml_path: str = None):
        yaml_path = yaml_path or os.path.join(__location__, 'sample_cfg.yaml')
        with open(yaml_path, 'r') as yaml_file:
            self.yaml_data = yaml.load(yaml_file)

    def generate_map(self) -> Map:
        map = Map(self.yaml_data['map']['width'], self.yaml_data['map']['height'])
        total_resource_count = len(self.yaml_data['resources'])
        total_resource_availability = 0
        for resource in self.yaml_data['resources']:
            total_resource_availability += resource['availability']



