# page_layout.py
# Stores page layout settings


class PageLayout:
    # use floats for these values
    font_family = "Helvetica"
    margin = 0.75
    col_width = 2.25
    col_height = 8.75
    col_space = 0.25


if __name__ == "__main__":
    page_layout = PageLayout()
    attributes = [attr for attr in dir(page_layout) if not attr.startswith("__")]
    print(attributes)
