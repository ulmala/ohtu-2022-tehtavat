import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        content = toml.loads(content)
        
        name = content['tool']['poetry']['name']
        description = content['tool']['poetry']['description']
        dependencies = list(content['tool']['poetry']['dependencies'].keys())
        dev_dependencies = list(content['tool']['poetry']['dev-dependencies'].keys())

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
