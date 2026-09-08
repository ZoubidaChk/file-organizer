#!/usr/bin/env python3
"""Plan and apply safe file moves by extension."""
import argparse, shutil
from pathlib import Path

def plan(folder):
    folder=Path(folder); moves=[]
    for src in folder.iterdir():
        if src.is_file():
            ext=src.suffix.lower().lstrip("."); category=ext.upper() if ext else "Other"
            if category in {"JPG","JPEG","PNG","GIF","BMP","SVG"}: category="Images"
            elif category in {"PDF","DOC","DOCX","TXT","MD"}: category="Documents"
            elif category in {"MP3","WAV","FLAC","MP4","MOV","AVI"}: category="Media"
            elif category not in {"Images","Documents","Media"}: category="Other"
            moves.append((src, folder/category/src.name))
    return moves

def apply(moves):
    done=[]
    for src,dst in moves:
        dst=Path(dst); dst.parent.mkdir(exist_ok=True)
        candidate=dst; n=1
        while candidate.exists(): candidate=dst.with_name(f"{dst.stem}_{n}{dst.suffix}"); n+=1
        shutil.move(str(src), str(candidate)); done.append((src,candidate))
    return done

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("folder"); p.add_argument("--apply", action="store_true"); a=p.parse_args()
    moves=plan(a.folder)
    for src,dst in moves: print(f"{src} -> {dst}")
    if a.apply: apply(moves)
    return 0
if __name__ == "__main__": raise SystemExit(main())
