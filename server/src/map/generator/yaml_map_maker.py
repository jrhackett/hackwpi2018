import logging
import os
import random
import yaml

from server.src.map.map import Map
from server.src.map.resources import ResourceType
from server.src.map.tiles.tile_factory import TileFactory

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
LOG = logging.getLogger(__name__)


class YamlMapMaker:

    def __init__(self, yaml_path: str = None):
        yaml_path = yaml_path or os.path.join(__location__, 'sample_cfg.yaml')
        with open(yaml_path, 'r') as yaml_file:
            self.yaml_data = yaml.load(yaml_file)

    def generate_map(self) -> Map:
        map = Map(self.yaml_data['map']['width'], self.yaml_data['map']['height'])
        total_tiles = self.yaml_data['map']['width'] * self.yaml_data['map']['width']
        total_resource_tiles = total_tiles * self.yaml_data['map']['density']

        total_resource_availability = 0
        LOG.debug("Calculating total resource availability...")
        for resource in self.yaml_data['resources']:
            total_resource_availability += resource['availability']
        LOG.debug("Total resource availability is %s", total_resource_availability)

        for resource in self.yaml_data['resources']:
            resource['expected_resource_tiles'] = round(
                resource['availability'] * total_resource_tiles / total_resource_availability)
            LOG.debug('Expected tile count for %s: %s', resource['name'], resource['expected_resource_tiles'])

        LOG.debug("Shuffling resource generation order...")
        random.shuffle(self.yaml_data['resources'])
        LOG.debug("Resources will be generated in the following order: %s",
                  ', '.join([resource['name'] for resource in self.yaml_data['resources']]))

        for resource in self.yaml_data['resources']:
            LOG.debug("Generating resource: %s...", resource['name'])
            tiles_generated = 0

            while tiles_generated < resource['expected_resource_tiles']:
                x = random.randint(0, map.width - 1)
                y = random.randint(0, map.height - 1)
                if map.is_valid_position(x, y):
                    tiles_generated += self.generate_resource_cluster(x, y, map, resource)

        return map

    def generate_resource_cluster(self, x: int, y: int, map: Map, resource: dict) -> int:
        """
        Generates a new resource cluster centered at the given coordinates
        :param x: x coord to start the cluster at
        :param y: y coord to start the cluster at
        :param map: the map to generate the cluster on
        :param resource: dictionary of resource information
        :return: the number of tiles generated
        """
        resource_type = ResourceType[resource['name']]
        resource_cluser_radius = resource['average_cluster_radius']
        resource_average_yield = resource['average_yield']
        resource_average_yield_variation = resource['average_yield_variation']
        resources_generated = 0

        for i in range(x - resource_cluser_radius, x + resource_cluser_radius):
            for j in range(y - resource_cluser_radius, y + resource_cluser_radius):
                if map.is_valid_position(i, j):
                    tile = TileFactory.make_tile(resource_type)
                    tile.quantity = self.get_resource_quantity(resource_average_yield, resource_average_yield_variation)
                    map.set_tile(i, j, tile)
                    resources_generated += 1

        return resources_generated

    @staticmethod
    def get_resource_quantity(average_yield: int, variation: float) -> int:
        """

        :param average_yield: average resource value
        :param variation: variation as a percent
        :return: the actual resource value that will be generated
        """
        # get a random between -1 and 1:
        rand = random.random() * 2 - 1
        variable_resource = rand * (variation * average_yield)
        return average_yield + variable_resource
