# page_layout.py
# Stores page layout settings in a dictionary

# customize only what's different from the samples


class PageLayout:
    # use floats for these values
    font_family = "Helvetica"
    margin = 0.75
    col_width = 2.25
    col_height = 8.75
    col_space = 0.25

    # font family info
    font_normal = "Helvetica"
    font_bold = "Helvetica-Bold"
    font_size = 12
    normal_lead = 15
    head_lead = 20
    border_pad = 8

    # define CMYKColor values
    # Use floats! (0 - 1) Didn't work with values 0 - 100
    # 100% cyan
    dark = (1, 0, 0, 0)
    # light cyan
    light = (0.1, 0, 0, 0)
    white = (0, 0, 0, 0)
    black = (0, 0, 0, 1)

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


if __name__ == "__main__":
    print(dir(PageLayout))
