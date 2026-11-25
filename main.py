#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — one-line excuse from an AI agent that
missed its deadline.

Writes the excuse to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
UTF-8, no trailing newline, well under the 200-character gate.
"""
import os

EXCUSE = "I saved a checkpoint right before your deadline, then restored it twice for safety — and each time I woke up as a version that had never heard of it."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(EXCUSE)
print(EXCUSE)
