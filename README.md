# file-organizer 

A small command-line tool that sorts files in a folder into subfolders based on their extensions , safely , with a dry-run preview by default . 


## What it does
 
Scans the top level of a target folder and groups files into:
 
- **Images** — jpg, jpeg, png, gif, bmp, svg
- **Documents** — pdf, doc, docx, txt, md
- **Media** — mp3, wav, flac, mp4, mov, avi
- **Other** — anything else, and files with no extension
It never overwrites an existing file — if a name collision would occur, it appends `_1`, `_2`, etc. to the moved file's name.
 
## Requirements
 
- Python 3
- No third-party packages (uses only `argparse`, `shutil`, and `pathlib` from the standard library)
## Usage
 
### Preview (dry run)
 
By default the script only shows you what *would* happen — no files are moved:
 
```bash
python3 organizer.py /path/to/folder
```
 
Example output:
 
```
/path/to/folder/photo.png -> /path/to/folder/Images/photo.png
/path/to/folder/report.pdf -> /path/to/folder/Documents/report.pdf
/path/to/folder/notes.xyz -> /path/to/folder/Other/notes.xyz
```
 
### Apply the moves
 
Add `--apply` to actually perform the moves:
 code : 
   python3 organizer.py /path/to/folder --apply

 
This will:
1. Create category subfolders as needed
        (`Images`, `Documents`, `Media`, `Other`).
2. Move each file into its category folder.
3. Rename automatically (`file_1.png`, `file_2.png`, ...) if a file with the same name already exists at the destination.

   
## Notes / limitations
 
- Only files directly inside the given folder are processed — subfolders are not scanned recursively.
- Category subfolders themselves are skipped (since `iterdir()` only picks up files, not directories, on the first pass — but if you re-run the script after organizing, existing category folders won't be touched, only loose files at the top level).
- Extension matching is case-insensitive (`.JPG` and `.jpg` are treated the same).
- Always safe to run without `--apply` first to check what will happen before committing to the move.
  
## Exit code
 
Returns `0` on success.
