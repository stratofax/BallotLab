# data.py
# read and write structured data

from files import FileTools
from lxml import objectify
import json

supported_ext_types = [".json", ".JSON", ".xml", ".XML"]
# create a string of supported extensions from list
ext_types_str = " ".join(str(item) for item in supported_ext_types)


class ElectionData:
    def __init__(self, data_file, data_dir):

        election_file = FileTools(data_file, data_dir)
        if not election_file.file_found:
            msg = "Election data file {} not found in directory {}"
            raise RuntimeError(msg.format(str(data_file, data_dir)))

        self.data_file = data_file
        self.data_dir = data_dir
        self.abs_path_to_data = election_file.abs_path_to_file
        self.ext = election_file.ext

        if self.ext not in supported_ext_types:
            msg = "Election data must be one of the following file types: " "{}. Got {}"
            raise RuntimeError(msg.format(ext_types_str, self.ext))

        if self.ext in [".xml", ".XML"]:
            self.election_data = self.parse_xml(self.abs_path_to_data)
        elif self.ext in [".json", ".JSON"]:
            self.election_data = self.parse_json(self.abs_path_to_data)

    def parse_xml(self, xml_file):
        """
        parse xml file into Python objects
        """
        with open(xml_file) as f:
            xml = f.read()
        return objectify.fromstring(xml)
        # was dump(xml_election.xml)

    def parse_json(self, json_file):
        """
        parse json file into Python objects
        """
        # read file
        with open(json_file, "r") as jsf:
            json_data = json.load(jsf)
        return json_data


if __name__ == "__main__":
    xml_election = ElectionData("nist_sample_election_report.xml", "assets/data")
    print(xml_election.data_file)
    print(xml_election.abs_path_to_data)
    print(xml_election.election_data)

    json_election = ElectionData("BallotStudio_16_Edits.JSON", "assets/data/")
    print(json_election.data_file)
    print(json_election.abs_path_to_data)
    print(json_election.election_data)
