from utils.files import FileTools
from page_layout import PageLayout
from reportlab.lib import utils
from reportlab.platypus import Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import PCMYKColor
from reportlab.lib.units import inch
import os

# these variables are private, hardcoded for now
# may be read from a settings file later?

col_width = PageLayout.col_width
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
    "<bold>Do not cross out or "
    "erase, or your vote may "
    "not count. If you make a "
    "mistake or a stray mark, "
    "ask for a new ballot from "
    "the poll workers.</bold>"
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


styles = getSampleStyleSheet()
normal = styles["Normal"]
warning_style = styles["BodyText"]
h1 = styles["Heading1"]
h2 = styles["Heading2"]


# modify default styles to fit spec
cyan = PCMYKColor(100, 0, 0, 0)
white = PCMYKColor(0, 0, 0, 0)
fsize = 12
border_pad = 6
# h1 (Heading 1)
# 100% process cyan

h1.backColor = cyan
h1.borderColor = cyan
h1.textColor = white
h1.borderPadding = border_pad
h1.fontSize = fsize + 2
# h2 (Heading 2)
light_cyan = PCMYKColor(10, 0, 0, 0)
h2.backColor = light_cyan
h2.borderColor = light_cyan
h2.borderPadding = border_pad
h2.fontSize = fsize
# Normal
normal.backColor = light_cyan
normal.borderColor = light_cyan
normal.borderColor = light_cyan
normal.borderPadding = border_pad
normal.leading = 15
normal.fontSize = fsize
# Warning style inherits normal styles
warning_style.backColor = light_cyan
warning_style.borderColor = light_cyan
warning_style.borderColor = light_cyan
warning_style.borderPadding = border_pad
warning_style.leading = 15
warning_style.fontName = "Helvetica-Bold"
warning_style.fontSize = fsize
warning_style.textColor = cyan

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

    instruction_list = [Paragraph(instruct_head, h1)]
    instruction_list.append(Paragraph(graf_text, h2))
    # instruction_list.append(fill_img, h2)
    instruction_list.append(Paragraph(fill_txt, normal))
    instruction_list.append(Paragraph(fill_warn_txt, warning_style))
    instruction_list.append(Paragraph(write_in_head, h2))
    instruction_list.append(write_img)
    instruction_list.append(Paragraph(write_in_text, normal))


if __name__ == "__main__":
    instruct = Instructions()
    print(instruct.instruction_list)
