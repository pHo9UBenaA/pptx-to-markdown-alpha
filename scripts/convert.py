from pathlib import Path
import sys
import subprocess
import re

USAGE = """
Convert PPTX to Markdown using pptx2md.

Usage:
  uv run scripts/convert.py <pptx-file> [--disable-image]

Options:
  --disable-image      Do not extract images and do not output them to Markdown

Example:
  uv run scripts/convert.py docs/input/sample.pptx --disable-image
"""

DEFAULT_OUTPUT_DIR = Path("/app/docs/output")


def parse_args(args):
    """
    Parse command line arguments
    """
    if not args or args[0] in ('-h', '--help'):
        print(USAGE)
        sys.exit(1)

    pptx_file = Path(args[0])
    disable_image = '--disable-image' in args
    disable_underline = '--disable-underline' in args

    return pptx_file, disable_image, disable_underline


def validate_paths(pptx_file, output_dir):
    """
    Check if file and directory exist
    """
    if not pptx_file.exists():
        print(f"❌ File not found: {pptx_file}")
        sys.exit(1)
    if not output_dir.exists():
        print(f"❌ Output directory does not exist: {output_dir}")
        sys.exit(1)


def run_pptx2md(pptx_file, md_filename, disable_image):
    """
    Run pptx2md command
    """
    cmd = [
        "pptx2md",
        str(pptx_file),
        "-o", str(md_filename)
    ]
    if disable_image:
        cmd.append("--disable-image")

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Converted {pptx_file} to Markdown: {md_filename}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Conversion failed: {e}")
        sys.exit(1)


def main():
    pptx_file, disable_image, disable_underline = parse_args(sys.argv[1:])
    validate_paths(pptx_file, DEFAULT_OUTPUT_DIR)

    md_filename = DEFAULT_OUTPUT_DIR / (pptx_file.stem + ".md")
    run_pptx2md(pptx_file, md_filename, disable_image)


if __name__ == '__main__':
    main()
