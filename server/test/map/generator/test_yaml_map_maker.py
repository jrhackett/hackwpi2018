from server.src.map.generator.yaml_map_maker import YamlMapMaker


class TestYamlMapMaker:

    def test_default_map_maker_creation_raises_no_errors(self):
        map_maker = YamlMapMaker()
        map_ = map_maker.generate_map()
        with open('c://users//dbozzuto//desktop//map.txt', 'w') as map_file:
            map_file.write(map_.format_map_as_str())

