import os
from pathlib import Path

ENTRY = (
    "A zipper is a row of tiny hands holding tight: pull the tab and each hand grabs the next one, closing the gap tooth by tooth.\n"
    "The holding-hands part is right — the teeth really do lock together in order — but real hands can let go and grab anyone, while each zipper tooth only ever meets the same partner, in the same line."
)

def main():
    if not ENTRY or len(ENTRY) > 400:
        raise SystemExit(f"ENTRY failed 1-400 char gate: {len(ENTRY)} chars")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = ENTRY.encode("utf-8")
    (out_dir / "entry.txt").write_bytes(data)
    print(f"chars={len(ENTRY)} bytes={len(data)} lines={ENTRY.count(chr(10)) + 1}")

if __name__ == "__main__":
    main()
