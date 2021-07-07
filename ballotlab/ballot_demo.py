# ballot_demo.py

from instructions import Instructions
from page_layout import PageLayout
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, Frame


def ballot_demo():
    # 1 = True, 0 = FALSE
    SHOW_BOUNDARY = 1

    margin = PageLayout.margin
    c_width = PageLayout.col_width
    c_height = PageLayout.col_height
    c_space = PageLayout.col_space

    ballot_canvas = Canvas("ballot_demo.pdf", pagesize=letter)
    inst = Instructions

    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    h1 = styles["Heading1"]

    left_column = inst.instruction_list

    mid_column = [Paragraph("Contest #1", h1)]
    mid_column.append(Paragraph("ipsum lorem", normal))

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
