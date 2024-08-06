#!/usr/bin/python3
"""
Converts Markdown to HTML
"""
import os
import sys


def md2html(md_file, html_file):
    """Converts heandings to HTML tags"""
    with open(md_file, 'r') as md, open(html_file, 'w') as html:
        for line in md:
            # remove whitespaces
            line = line.strip()
            if line[0] == '#':
                # count the nmber of leading '#' chars
                level = len(line.split(' ')[0])
                if 1 <= level <= 6:
                    # extract the title
                    title = line[level:].strip()
                    html.write(f"<h{level}>{title}</h{level}>\n")


def main():
    """Handles command line arguments and related errors"""

    if len(sys.argv) < 3:
        print(
            "Usage: ./markdown2html.py README.md README.html",
            file=sys.stderr
            )
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.isfile(md_file):
        print(f"Missing {md_file}", file=sys.stderr)
        sys.exit(1)

    md2html(md_file, html_file)

    sys.exit(0)


if __name__ == "__main__":
    main()
