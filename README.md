# pptx-to-markdown

## Overview

This project provides a Dockerized environment for converting PowerPoint (`.pptx`) files to Markdown using the `pptx2md` tool.

## Getting Started

### Start the Docker Container

```bash
docker compose up -d
```

### Convert PPTX to Markdown

To convert a PPTX file to Markdown, use the following command:

```bash
docker compose exec -w /app app uv run scripts/convert.py docs/input/sample.pptx 
```

- To disable image extraction, add the `--disable-image` option:
- The converted Markdown file will be saved in the `docs/output/` directory.
