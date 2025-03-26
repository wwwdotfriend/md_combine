# md_combine

A simple Python script that combines multiple `.md` files into a single `.txt` file in the correct numerical order if the file names contain numbers.

I use this for my DND session logs contained in Obsidian so the filenames are `Session 1.md`, `Session 2.md,` etc.

## Prerequisites

Requires Python and the `natsort` package.

Install `natsort` with:

```sh
pip install natsort
```

## Usage

Run `md_combine.py` and input the filepath containing your markdown files. It'll output the .txt file next to the script.
