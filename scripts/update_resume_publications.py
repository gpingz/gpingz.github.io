#!/usr/bin/env python3
"""Rebuild page 2 of the website CV with the current publication list."""

from pathlib import Path
from tempfile import TemporaryDirectory

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
RESUME = ROOT / "static" / "uploads" / "resume.pdf"
PAGE_WIDTH, PAGE_HEIGHT = letter
LEFT = 74
RIGHT = 74
BODY_SIZE = 10.7
BODY_LEADING = 13.7


def wrap_text(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_wrapped(
    pdf: canvas.Canvas,
    text: str,
    y: float,
    *,
    x: float = LEFT,
    width: float = PAGE_WIDTH - LEFT - RIGHT,
    font: str = "Times-Roman",
    size: float = BODY_SIZE,
    leading: float = BODY_LEADING,
    link: str | None = None,
) -> float:
    lines = wrap_text(text, font, size, width)
    pdf.setFont(font, size)
    for line in lines:
        pdf.drawString(x, y, line)
        y -= leading
    if link:
        top = y + leading + 2
        bottom = y - 1
        pdf.linkURL(link, (x, bottom, x + width, top), relative=0)
    return y


def draw_page_two(output: Path) -> None:
    pdf = canvas.Canvas(str(output), pagesize=letter)
    pdf.setTitle("Guangping Zeng CV")
    pdf.setAuthor("Guangping Zeng")

    y = 720
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(LEFT, y, "Lab Skills")
    y -= 23
    y = draw_wrapped(
        pdf,
        "Geochemistry & Microanalysis: SIMS, MC-ICP-MS, LA-ICP-MS, SEM, XRF",
        y,
        x=94,
        width=PAGE_WIDTH - 94 - RIGHT,
    )
    y = draw_wrapped(
        pdf,
        "Data Analysis: Python, MATLAB, ArcGIS",
        y,
        x=94,
        width=PAGE_WIDTH - 94 - RIGHT,
    )

    y -= 16
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(LEFT, y, "Honors and Awards")
    y -= 24
    for award in (
        "AGU Student Travel Grant $1,000 (2024)",
        "UCAS Joint Ph.D. Training Fellowship $24,000 (2024-2025)",
        "National Encouragement Scholarship (2020-2022)",
        "Outstanding Graduation Thesis Award (2019)",
        "Excellent Camper, Nanjing Institute of Paleontology, CAS (2018)",
        "University People's Scholarship Award (2017)",
        "University Student Summer Social Practice Group Award (2016)",
    ):
        y = draw_wrapped(
            pdf,
            award,
            y,
            x=97,
            width=PAGE_WIDTH - 97 - RIGHT,
        )

    y -= 15
    pdf.setFont("Times-Roman", 16)
    pdf.drawString(LEFT, y, "Publications")
    y -= 27
    pdf.setFont("Times-Roman", 11.5)
    pdf.drawString(LEFT, y, "Peer-reviewed Articles")
    y -= 22

    articles = (
        (
            "Gardezi, S.A.H., Luan, X., Li, F., Lin, J., Zeng, C., Zeng, G., Zhang, Y., "
            "Yang, X., Khan, M.J., Sun, Z., 2026. Structural evolution of mud-intrusive "
            "and mud-extrusive system in the Makran accretionary wedge: Processes and "
            "patterns. Marine Geoscience and Energy Resources 193, 207833. "
            "https://doi.org/10.1016/j.marger.2026.207833",
            "https://doi.org/10.1016/j.marger.2026.207833",
        ),
        (
            "Zeng, G., Zhang, Y., Sun, Z., Mehmood, M., Gardezi, S.A.H., Miao, X., Sun, "
            "L., Li, X., 2026. Unraveling the India-Eurasia Collision Pattern: Insights "
            "from Subduction to Collision-Related Magmatism in the Chagai Hills. "
            "J. Earth Sci. 37, 1055-1069. "
            "https://doi.org/10.1007/s12583-025-0244-z",
            "https://doi.org/10.1007/s12583-025-0244-z",
        ),
        (
            "Zeng, G., Wang, J., Zhang, C.G., Zhao, Q., Wu, S., 2022. Paleogeographic "
            "environment characteristics of the Guanshan Member of the Leping Formation "
            "in the Erjiacun Depression, southern Poyang Basin. Fault-Block Oil & Gas "
            "Field 29(2), 199-206 (in Chinese).",
            None,
        ),
    )
    for article, doi in articles:
        y = draw_wrapped(pdf, article, y, link=doi)
        y -= 8

    y -= 3
    pdf.setFont("Times-Roman", 11.5)
    pdf.drawString(LEFT, y, "Conference Abstracts")
    y -= 22
    y = draw_wrapped(
        pdf,
        "Zeng, G., Zhang, Y., Straub, S.M., et al., 2024. Sediment recycling at the "
        "Makran arc: Insights from whole-rock elemental and Sr-Nd-Pb isotope systematics. "
        "Abstract, AGU Fall Meeting 2024.",
        y,
    )

    y -= 12
    pdf.setFont("Times-Roman", 11.5)
    pdf.drawString(LEFT, y, "Manuscripts under Review")
    y -= 22
    draw_wrapped(
        pdf,
        "Zeng, G., Zhang, Y., Sun, Z., et al. Efficient return of subducted organic "
        "carbon in the Makran arc volcano. Under review.",
        y,
    )

    pdf.setFont("Times-Roman", 10)
    pdf.drawCentredString(PAGE_WIDTH / 2, 31, "2")
    pdf.save()


def update_resume() -> None:
    with TemporaryDirectory(prefix="resume-update-") as temp_dir:
        page_two = Path(temp_dir) / "page-two.pdf"
        output = Path(temp_dir) / "resume.pdf"
        draw_page_two(page_two)

        current = PdfReader(str(RESUME))
        replacement = PdfReader(str(page_two))
        writer = PdfWriter()
        writer.add_page(current.pages[0])
        writer.add_page(replacement.pages[0])
        writer.add_metadata(
            {
                "/Title": "Guangping Zeng CV",
                "/Author": "Guangping Zeng",
            }
        )
        with output.open("wb") as stream:
            writer.write(stream)
        RESUME.write_bytes(output.read_bytes())


if __name__ == "__main__":
    update_resume()
