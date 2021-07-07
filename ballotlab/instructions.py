# instructions.py
# Build the ballot instructions

from utils.files import FileTools
from page_layout import PageLayout
from reportlab.lib import utils
from reportlab.platypus import Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import PCMYKColor
from reportlab.lib.units import inch
import os

# these variables are hardcoded for now
# may be read from a settings file later?

col_width = PageLayout.col_width


def build_instruction_list(i_list):
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

    i_list = [Paragraph(instruct_head, h1)]
    i_list.append(Paragraph(graf_text, h2))
    i_list.append(Paragraph(fill_txt, normal))
    i_list.append(Paragraph(fill_warn_txt, warn_text))
    i_list.append(Paragraph(write_in_head, h2))
    i_list.append(write_img)
    i_list.append(Paragraph(write_in_text, normal))


# define styles
# # set up the constants
# 100% process cyan
dark_bg = PCMYKColor(100, 0, 0, 0)
# light cyan
light_bg = PCMYKColor(10, 0, 0, 0)
white = PCMYKColor(0, 0, 0, 0)
black = PCMYKColor(0, 0, 0, 100)
font_size = 12
border_pad = 6


def define_custom_style(
    style,
    bg_color,
    border_pd=border_pad,
    font_sz=font_size,
    txt_color=black,
    font_n="Helvetica",
    line_space=font_size + 1,
):
    style.backColor = bg_color
    style.borderColor = bg_color
    style.borderPadding = border_pd
    style.fontSize = font_sz
    style.textColor = txt_color
    style.fontName = font_n
    style.leading = line_space


def get_styles():
    """customize styles for the instructions section"""
    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    warn_text = styles["BodyText"]
    h1 = styles["Heading1"]
    h2 = styles["Heading2"]

    # modify default styles to fit spec
    # h1 (Heading 1)

    define_custom_style(h1, dark_bg, border_pad, font_size + 2, white)
    define_custom_style(h2, light_bg)
    define_custom_style(normal, light_bg)
    define_custom_style(
        warn_text, light_bg, border_pad, font_size, dark_bg, "Helvetica-Bold", 15
    )

    # h1.backColor = cyan
    # h1.borderColor = cyan
    # h1.borderPadding = border_pad
    # h1.fontSize = font_size + 2
    # h1.textColor = white
    # h2 (Heading 2)
    # h2.backColor = light_cyan
    # h2.borderColor = light_cyan
    # h2.borderPadding = border_pad
    # h2.fontSize = font_size
    # Normal
    # normal.backColor = light_cyan
    # normal.borderColor = light_cyan
    # normal.borderPadding = border_pad
    # normal.leading = 15
    # normal.fontSize = font_size
    # Warning style inherits normal styles
    # warn_text.backColor = light_cyan
    # warn_text.borderColor = light_cyan
    # warn_text.borderColor = light_cyan
    # warn_text.borderPadding = border_pad
    # warn_text.leading = 15
    # warn_text.fontName = "Helvetica-Bold"
    # warn_text.fontSize = font_size
    # warn_text.textColor = cyan


# get image files
rel_img_path = "assets/img"
ftools = FileTools()
package_root = ftools.package_root
img_folder = os.path.join(package_root, rel_img_path)
fill_bubbles_img = "filled_bubble.png"
write_in_img = "writein.png"

fill_bubbles = os.path.join(img_folder, fill_bubbles_img)
img = utils.ImageReader(fill_bubbles)
img_width, img_height = img.getSize()
aspect = img_height / float(img_width)

i_width = (col_width * inch) - (border_pad * 2)
i_height = i_width * aspect

# <img src="snakehead.jpg" width="50" height="50"/> in the
#     middle of our text'''

graf_text = '<p>{}</p><br /><br /><br /><br /><br /><p><img src="{}" width="{}" height="{}" valign="text-bottom"/></p>'.format(
    fill_head, fill_bubbles, i_width, i_height
)
# fill_img = Image(fill_bubbles, width=target_width, height=(target_width * aspect))
# fill_img.hAlign = "CENTER"
fill_img = Paragraph(graf_text)


write_in = os.path.join(img_folder, write_in_img)
img = utils.ImageReader(write_in)
img_width, img_height = img.getSize()
aspect = img_height / float(img_width)

write_img = Image(write_in, width=i_width, height=(i_width * aspect))
write_img.hAlign = "CENTER"


class Instructions:
    """
    Ballot Instructions class encapsulates static
    instructional text and instructional graphics
    """


if __name__ == "__main__":
    instruct = Instructions()
    print(instruct.instruction_list)
