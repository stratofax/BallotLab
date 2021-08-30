# data.py
# read and write structured data

# from posixpath import relpath
from files import FileTools
import xmltodict
import json

# import pprint


# supported_ext_types = [".xml", ".XML"]
# supported_ext_types = [".json", ".JSON", ".xml", ".XML"]
supported_ext_types = [".json", ".JSON"]
# create a string of supported extensions from list
ext_types_str = " ".join(str(item) for item in supported_ext_types)


class ElectionData:
    """
    Open the specified Election Data File (EDF)
    Read data into Python objects.
    Read well-formatted json and xml only
    Raises RuntimeError for bad data
    """

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

        # read data file into Python objects, use that API
        # Read XML data into lxml object hierarchy
        if self.ext in [".xml", ".XML"]:
            self.election_rpt = self.parse_xml(self.abs_path_to_data)
        elif self.ext in [".json", ".JSON"]:
            self.election_rpt = self.parse_json(self.abs_path_to_data)
            # Read Election data from JSON dict, which is
            self.elect_name = self.election_rpt["Election"][0]["Name"]
            self.start_date = self.election_rpt["Election"][0]["StartDate"]
            self.end_date = self.election_rpt["Election"][0]["EndDate"]
            self.elect_type = self.election_rpt["Election"][0]["Type"]

        # self.text_rpt = self.print_line("- ", 40)
        # Election contains BallotStyle, Candidate and Contest.
        self.text_rpt = "EDF name: {}\n".format(self.data_file)
        self.text_rpt += "Location: {}\n".format(self.abs_path_to_data)
        # rpt_title = "Election Report\n"
        # self.text_rpt += rpt_title
        # self.text_rpt(self.print_line("=", len(rpt_title)))
        # self.text_rpt += "File: {}\n".format(self.data_file)
        # self.text_rpt += "Object election_rpt is {}.\n".format(type(self.election_rpt))
        # pprint.pprint(self.election_rpt)
        self.text_rpt += "Election name: {}\n".format(self.elect_name)
        self.text_rpt += "Election type: {}\n".format(self.elect_type)
        self.text_rpt += "Start date: {}\n".format(self.start_date)
        self.text_rpt += "End date: {}\n".format(self.end_date)
        # print("Geopolitical Units:")
        print(self.text_rpt)
        # print(self.election_rpt["GpUnit"])

    def parse_xml(self, xml_file):
        """
        parse xml file into JSON-style dict
        """
        with open(xml_file) as xmlf:
            xml = xmlf.read()
        return xmltodict.parse(xml, dict_constructor=dict)

    def parse_json(self, json_file):
        """
        parse json file into dictionary
        """
        # read file
        with open(json_file, "r") as jsf:
            json_data = json.load(jsf)
        return json_data

    def print_line(self, string="-", count=10):
        print(string * count)


if __name__ == "__main__":
    # xml_election = ElectionData("nist_sample_election_report.xml", "assets/data")
    # print(xml_election.data_file)
    # print(xml_election.abs_path_to_data)
    # this doesn't print out anything
    # print(xml_election.election_rpt)

    json_election = ElectionData("NIST_sample.json", "assets/data/")
    # print(json_election.data_file)
    # print(json_election.abs_path_to_data)
    # print JSON dict
    # print(json_election.election_rpt)

    json_election = ElectionData("BallotStudio_16_Edits.JSON", "assets/data/")
    # print(json_election.data_file)
    # print(json_election.abs_path_to_data)
