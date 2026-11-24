"""The Long Roast entry.

Writes one original satirical sentence to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``): a lawmaker
writing the rules for AI, crypto or the internet who cannot convert
a file to PDF. Python 3.13 standard library only; no network,
no randomness, no input files.
"""

import os

ENTRY = (
    "The congressman writing the law to govern artificial intelligence "
    "still saves every bill as 'Document1', prints it, scans it back "
    "in crooked, and asks his aide to fax him the PDF."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
