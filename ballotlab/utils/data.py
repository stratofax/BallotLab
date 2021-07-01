# data.py
# read and write structured data

from files import FileTools
from lxml import objectify


class ElectionData:
    def __init__(self, data_file, data_dir):
        self.data_file = data_file
        self.data_dir = data_dir
        self.abs_path_to_data = self.find_data_file(self.data_file, self.data_dir)
        if self.abs_path_to_data:
            self.xml = self.parse_xml(self.abs_path_to_data)

    def find_data_file(self, find_file, search_dir):
        dataFile = FileTools(find_file, search_dir)
        if dataFile.file_found:
            return dataFile.abs_path_to_file
        else:
            return ""

    def parse_xml(self, xml_file):
        """"""
        with open(xml_file) as f:
            xml = f.read()
        return objectify.fromstring(xml)


if __name__ == "__main__":
    election = ElectionData("nist_sample_election_report.xml", "assets/data")
    print(election.data_file)
    print(election.abs_path_to_data)
    print(objectify.dump(election.xml))
