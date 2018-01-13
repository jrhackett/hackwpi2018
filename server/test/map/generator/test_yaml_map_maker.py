from server.src.map.generator.yaml_map_maker import YamlMapMaker


class TestYamlMapMaker:

    def test_default_map_maker_creation_raises_no_errors(self):
        map_maker = YamlMapMaker()
