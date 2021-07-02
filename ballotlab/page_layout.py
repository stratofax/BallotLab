# page_layout.py
# Stores page layout settings
from dataclasses import dataclass


@dataclass
class PageLayout:
    # use floats for these values
    font_family: str = "Helvetica"
    margin: float = 0.75
    col_width: float = 2.25
    col_height: float = 8.75
    col_space: float = 0.25


if __name__ == "__main__":
    page_layout = PageLayout()
    attributes = [attr for attr in dir(page_layout) if not attr.startswith("__")]
    print(attributes)
