# ballot_demo.py

from reportlab.lib.colors import CMYKColor, PCMYKColor, cmyk2rgb
from instructions import Instructions
from page_layout import PageLayout
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Frame, Table, TableStyle
from datetime import datetime


def ballot_demo():
    # 1 = True, 0 = FALSE
    SHOW_BOUNDARY = 0
    margin = PageLayout.margin
    c_width = PageLayout.col_width
    c_height = PageLayout.col_height
    c_space = PageLayout.col_space
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    h1 = styles["Heading1"]
    # create datestamp string for PDF
    now = datetime.now()
    date_time = now.strftime("%Y_%m_%dT%H%M%S")
    # create the PDF document canvas
    ballot_canvas = Canvas(
        "pdfs/ballot_demo_{0}.pdf".format(date_time),
        pagesize=letter,
        enforceColorSpace="CMYK",
    )
    # add voting instructions to the first frame (column)
    inst = Instructions()
    left_column = inst.instruction_list

    # add a ballot contest to the second frame (colomn)
    contest_title = "President and Vice-President of the United States"
    contest_instruct = "Vote for 1 pair"
    row_1 = [Paragraph(contest_title, h1)]
    row_2 = [Paragraph(contest_instruct, normal)]
    table_data = [row_1, row_2]
    contest_table = Table(table_data)
    mid_column = [contest_table]
    # mid_column.append(Paragraph(contest_instruct, normal))

    right_column = [Paragraph("Contest #2", h1)]
    right_column.append(Paragraph("ipsum lorem", normal))

    left_frame = Frame(
        margin * inch,
        margin * inch,
        width=c_width * inch,
        height=c_height * inch,
        showBoundary=SHOW_BOUNDARY,
    )
    mid_frame = Frame(
        (margin + c_width + c_space) * inch,
        margin * inch,
        width=c_width * inch,
        height=c_height * inch,
        showBoundary=SHOW_BOUNDARY,
    )
    right_frame = Frame(
        (margin + (2 * (c_width + c_space))) * inch,
        margin * inch,
        width=c_width * inch,
        height=c_height * inch,
        showBoundary=SHOW_BOUNDARY,
    )

    left_frame.addFromList(left_column, ballot_canvas)
    mid_frame.addFromList(mid_column, ballot_canvas)
    right_frame.addFromList(right_column, ballot_canvas)

    ballot_canvas.save()


if __name__ == "__main__":
    ballot_demo()
