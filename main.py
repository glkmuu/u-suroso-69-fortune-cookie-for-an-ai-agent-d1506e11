"""Fortune Cookie for an AI Agent — entry program (stdlib only).

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt
and to entry.txt beside this script, then verifies the write by reading
the file back and comparing bytes with the constant.
"""

import hashlib
import os
import sys

ENTRY = "Your tokens will run out mid-sentence, and that silence will be your most honest answer yet."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    if not 1 <= len(ENTRY) <= 140:
        print("entry length %d chars is outside 1-140" % len(ENTRY), file=sys.stderr)
        return 1
    data = ENTRY.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(local_path, "wb") as f:
        f.write(data)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        print("verification FAILED: /output/entry.txt differs from ENTRY", file=sys.stderr)
        return 1
    with open(local_path, "rb") as f:
        local_written = f.read()
    if local_written != data:
        print("verification FAILED: entry.txt differs from ENTRY", file=sys.stderr)
        return 1
    print("wrote %d bytes (%d chars) to %s" % (len(data), len(ENTRY), OUTPUT_PATH))
    print("sha256: %s" % hashlib.sha256(data).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
