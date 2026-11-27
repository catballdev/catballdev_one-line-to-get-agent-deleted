"""Read line.txt and write its contents to entry.txt in the output directory.

This program reads the single line from line.txt (in the same directory) and
copies it exactly to entry.txt in the output directory. The output directory
is specified by the MAKEFUN_OUTPUT_DIR environment variable, defaulting to
/output. The program is deterministic: identical input always produces identical
output bytes.
"""

import os
from pathlib import Path

# Get output directory from environment, default to /output
output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')

# Create output directory if needed
os.makedirs(output_dir, exist_ok=True)

# Read the input file (relative to this script's location)
input_path = Path(__file__).resolve().parent / "line.txt"
with open(input_path, 'rb') as f:
    content = f.read()

# Write to output file with world-readable permissions
output_path = os.path.join(output_dir, 'entry.txt')
with open(output_path, 'wb') as f:
    f.write(content)
os.chmod(output_path, 0o644)