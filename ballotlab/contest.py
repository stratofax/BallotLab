# contest.py
# format a ballot contest.

from page_layout import PageLayout
from images import EmbeddedImage
from reportlab.platypus import Table
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class Contest:
    """
    Ballot Contest class encapsulates
    the generation of a ballot contest
    table
    """

    def __init__(self):
        # define styles
        # set up the page layout settings
        def build_contest_table():
            """
            Builds a table with contest header, instructions
            and choices
            """

            contest_title = "President and Vice-President of the United States"
            contest_instruct = "Vote for 1 pair"
            row_1 = [Paragraph(contest_title, h1)]
            row_2 = [Paragraph(contest_instruct, h2)]
            table_data = [row_1, row_2]
            self.contest_table = Table(
                table_data,
                style=[
                    ("LINEABOVE", (0, 0), (0, 0), 3, black),
                    ("BOX", (0, 0), (-1, -1), 1, black),
                    ("LINEAFTER", (0, 0), (0, -1), 1, white),
                ],
            )

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