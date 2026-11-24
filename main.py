#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt, the artifact the house judge reads.
"""

import os
from pathlib import Path

LINE = (
    "The baby monitor crackled at 3 a.m., and a small voice I didn't "
    "recognize said, 'Mummy, the man in your bed isn't Daddy.'"
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
