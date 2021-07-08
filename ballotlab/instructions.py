# instructions.py
# Build the ballot instructions


from reportlab.platypus.flowables import Spacer
from page_layout import PageLayout
from images import EmbeddedImage
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


class Instructions:
    """
    Ballot Instructions class encapsulates static
    instructional text and instructional graphics
    """

    # these variables are hardcoded for now
    # may be read from a settings file later?
    def __init__(self):
        self.instruction_list = []
        # define styles
        # set up the constants
        # define CMYKColor values
        # Use floats! (0 - 1) Didn't work with values 0 - 100
        # 100% cyan
        dark = (1, 0, 0, 0)
        # light cyan
        light = (0.1, 0, 0, 0)
        white = (0, 0, 0, 0)
        black = (0, 0, 0, 1)

        # font family info
        font_normal = "Helvetica"
        font_bold = "Helvetica-Bold"
        font_size = 12
        normal_lead = 15
        head_lead = 20
        border_pad = 8

        # image dimensions
        col_width = PageLayout.col_width
        image_width = (col_width * inch) - (border_pad * 2)

        # start with the sample styles
        styles = getSampleStyleSheet()
        normal = styles["Normal"]
        warn_text = styles["BodyText"]
        h1 = styles["Heading1"]
        h2 = styles["Heading2"]

        # customize only what's different from the samples
        def define_custom_style(
            style,
            bg_color,
            border_pd=border_pad,
            font_sz=font_size,
            txt_color=black,
            font_n=font_normal,
            line_space=font_size + 1,
        ):
            style.backColor = bg_color
            style.borderColor = bg_color
            style.borderPadding = border_pd
            style.fontSize = font_sz
            style.textColor = txt_color
            style.fontName = font_n
            style.leading = line_space
            # style.leftIndent = 4

        def build_instruction_list():
            """Build a list of paragraph flowables for the ballot instructions section"""
            instruct_head = "Instructions"
            fill_head = "Making Selections"
            fill_txt = (
                "Fill in the oval to the left of "
                "the name of your choice. "
                "You must blacken the oval "
                "completely, and do not make "
                "any marks outside of the "
                "oval. You do not have to vote "
                "in every race."
            )
            fill_warn_txt = (
                "Do not cross out or "
                "erase, or your vote may "
                "not count. If you make a "
                "mistake or a stray mark, "
                "ask for a new ballot from "
                "the poll workers."
            )
            write_in_head = "Optional write-in"
            write_in_text = (
                "To add a candidate, fill in "
                "the oval to the left of “or "
                "write-in” and print the name "
                "clearly on the dotted line."
            )
            turn_in_head = "Turning in the ballot"
            turn_in_text = (
                "Insert the completed ballot "
                "into the ballot sleeve. Hand "
                "in the ballot to be counted."
            )
            turn_in_warn = "Do not fold the ballot."

            # get images
            image1 = EmbeddedImage("filled_bubble.png", image_width)
            image1_graf = image1.embed_text
            image2 = EmbeddedImage("writein.png", image_width)
            image2_graf = image2.embed_text

            fill_bubbles_img = "filled_bubble.png"
            write_in_img = "writein.png"

            self.instruction_list = [Paragraph(instruct_head, h1)]
            self.instruction_list.append(Spacer(0, border_pad * 2))
            self.instruction_list.append(Paragraph(image1_graf, normal))
            self.instruction_list.append(Paragraph(fill_head, h2))
            self.instruction_list.append(Paragraph(fill_txt, normal))
            self.instruction_list.append(Paragraph(fill_warn_txt, warn_text))
            self.instruction_list.append(Spacer(0, border_pad * 3))
            self.instruction_list.append(Paragraph(image2_graf, normal))
            self.instruction_list.append(Paragraph(write_in_head, h2))
            self.instruction_list.append(Paragraph(write_in_text, normal))

        # define our custom styles
        define_custom_style(
            h1, dark, border_pad, font_size + 2, white, font_bold, head_lead
        )
        define_custom_style(
            h2, light, border_pad, font_size, black, font_bold, normal_lead + 2
        )
        define_custom_style(
            normal, light, border_pad, font_size, black, font_normal, normal_lead
        )
        define_custom_style(
            warn_text, light, border_pad, font_size, dark, font_bold, normal_lead
        )
        # build the list, an attribute of the Instructions object
        build_instruction_list()


if __name__ == "__main__":
    instruct = Instructions()
    print(instruct.instruction_list)
