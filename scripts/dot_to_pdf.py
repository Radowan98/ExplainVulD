import os
import argparse
import subprocess

def convert_dot_to_pdf(input_path, output_path):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    try:
        subprocess.run(["dot", "-Tpdf", input_path, "-o", output_path], check=True)
        print(f"[✓] Successfully converted: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Graphviz error: {e}")
    except Exception as e:
        print(f"[!] Failed to convert {input_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a DOT file to PDF using Graphviz")
    parser.add_argument("--input", type=str, required=True, help="Path to the .dot file")
    parser.add_argument("--output", type=str, required=True, help="Path to save the output .pdf file")

    args = parser.parse_args()

    convert_dot_to_pdf(args.input, args.output)
