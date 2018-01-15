from server.src.map.generator.yaml_map_maker import YamlMapMaker


class TestYamlMapMaker:

    def test_default_map_maker_creation_raises_no_errors(self):
        map_maker = YamlMapMaker()
        map = map_maker.generate_map()
        assert map

    def test_generate_map_with_no_resources(self):
        blank_map_data = {
            'map':
                {
                    'width': 10,
                    'height': 10,
                    'density': 0.0
                }
        }
        map_maker = YamlMapMaker(yaml_data=blank_map_data)
        map_maker.generate_map()
