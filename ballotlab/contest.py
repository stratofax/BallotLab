# contest.py
# format a ballot contest.

from page_layout import PageLayout
from images import EmbeddedImage
from reportlab.platypus import Table
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.graphics.shapes import Ellipse
from reportlab.lib.colors import white, black

oval_width = 16
oval_height = 8


class SelectionOval(_DrawingEditorMixin, Drawing):
    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self, width, height, *args, **kw)

        self.width = oval_width + PageLayout.border_pad
        self.height = oval_height + PageLayout.border_pad
        oval_cx = self.width / 2
        oval_cy = self.height / 2
        self._add(
            self,
            Ellipse(oval_cx, oval_cy, oval_width, oval_height),
            name="oval",
            validate=None,
            desc=None,
        )
        self.oval.fillColor = white
        self.oval.strokeColor = black
        self.oval.strokeWidth = 1


class Contest:
    """
    Ballot Contest class encapsulates
    the generation of a ballot contest
    table
    """

    def __init__(self):
        # set up the page layout settings
        self.contest_list = []
        self.contestants = []
        self.contest_title = "President and Vice-President of the United States"
        self.contest_instruct = "Vote for 1 pair"

        def get_contest():
            self.contestants = [
                ("Joseph Barchi and Joseph Hallaren", "Blue"),
                ("Adam Cramer and Greg Vuocolo", "Yellow"),
                ("Daniel Court and Amy Blumhard", "Purple"),
                ("Alvin Boone and James Lian", "Orange"),
                # ("Austin Hildebrand and James Garritty", "Pink"),
                # ("Martin Patterson and Clay Lariviere", "Gold"),
                # ("Elizabeth Harp and Antoine Jefferson", "Gray"),
                # ("Marzena Pazgier and Welton Phelps", "Brown"),
            ]
            # self.contestants = [
            #     ("Joseph Barchi and Joseph Hallaren", "Blue"),
            #     ("Adam Cramer and Greg Vuocolo", "Yellow"),
            #     ("Daniel Court and Amy Blumhard", "Purple"),
            #     ("Alvin Boone and James Lian", "Orange"),
            #     ("Austin Hildebrand and James Garritty", "Pink"),
            #     ("Martin Patterson and Clay Lariviere", "Gold"),
            #     ("Elizabeth Harp and Antoine Jefferson", "Gray"),
            #     ("Marzena Pazgier and Welton Phelps", "Brown"),
            # ]

        def build_contest_list(contestants, contestant_party_list):
            oval = SelectionOval()
            for contestant, party in contestants:
                # add newlines around " and "
                if contestant.find(" and "):
                    contestant = contestant.replace(" and ", "<br />and<br />")
                contest_line = "<b>{}</b><br />{}".format(contestant, party)
                contest_row = [oval, Paragraph(contest_line, normal)]
                contestant_party_list.append(contest_row)

        def build_contest_table():
            """
            Builds a table with contest header, instructions
            and choices
            """

            get_contest()
            row_1 = [Paragraph(self.contest_title, h1)]
            row_2 = [Paragraph(self.contest_instruct, h2)]
            self.header_list = (row_1, row_2)

            self.contest_header = Table(
                self.header_list,
                style=[
                    ("LINEABOVE", (0, 0), (0, 0), 3, black),
                    ("LINEBEFORE", (0, 0), (0, -1), 1, black),
                    ("LINEAFTER", (0, 0), (0, -1), 1, white),
                ],
            )
            self.contest_table = []
            build_contest_list(self.contestants, self.contest_list)
            self.contest_table = Table(
                self.contest_list,
                style=[
                    # ("BOX", (0, 0), (-1, -1), 1, black),
                    ("LINEBEFORE", (0, 0), (0, -1), 1, black),
                    ("LINEAFTER", (0, 0), (0, -1), 1, white),
                    ("LINEBELOW", (0, -1), (-1, -1), 1, black),
                ],
            )

        # define styles
        # fill colors
        dark = PageLayout.dark
        light = PageLayout.light
        white = PageLayout.white
        black = PageLayout.black
        grey = PageLayout.grey

        # font family info
        font_normal = PageLayout.font_normal
        font_bold = PageLayout.font_bold
        font_size = PageLayout.font_size
        normal_lead = PageLayout.normal_lead
        head_lead = PageLayout.head_lead
        border_pad = PageLayout.border_pad / 2

        # image dimensions
        col_width = PageLayout.col_width

        # start with the sample styles
        styles = getSampleStyleSheet()
        normal = styles["Normal"]
        warn_text = styles["BodyText"]
        h1 = styles["Heading1"]
        h2 = styles["Heading2"]

        # define custom styles for contest tables
        PageLayout.define_custom_style(
            h1,
            grey,
            border_pad,
            font_size + 2,
            black,
            font_bold,
            normal_lead,
            sp_before=12,
            sp_after=48,
        )
        PageLayout.define_custom_style(
            h2, light, border_pad, font_size, black, font_bold, normal_lead
        )
        # build the contest table, an attribute of the Contest object
        build_contest_table()
