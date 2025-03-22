import os
import glob
from natsort import natsorted

md_directory = input("Enter the full path to the folder containing the markdown files: ").strip()

if not os.path.isdir(md_directory):
    print("Error: The specified directory does not exist. Please check the path and try again.")
    exit()

output_file = "combined_logs.txt"

def combine_markdown_files(md_directory, output_file):
    md_files = glob.glob(os.path.join(md_directory, "*.md"))

    md_files = natsorted(md_files)

    if not md_files:
        print("No .md files found in the directory.")
        return

    with open(output_file, "w", encoding="utf-8") as outfile:
        for md_file in md_files:
            with open(md_file, "r", encoding="utf-8") as infile:
                outfile.write(f"--- {os.path.basename(md_file)} ---\n") 
                outfile.write(infile.read() + "\n\n") 

    print(f"Combined {len(md_files)} files into {output_file}")

combine_markdown_files(md_directory, output_file)
