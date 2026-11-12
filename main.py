import os
import shutil
from pathlib import Path


def main():
    script_dir = Path(__file__).resolve().parent
    source_file = script_dir / "entry.png"
    
    if not source_file.is_file():
        raise FileNotFoundError(f"Source file not found: {source_file}")

    output_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_dir = Path(output_dir_env) if output_dir_env else Path("/output")

    output_file = output_dir / "entry.png"

    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_file, output_file)


if __name__ == "__main__":
    main()
