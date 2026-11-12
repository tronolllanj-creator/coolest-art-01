import os
import shutil
from pathlib import Path

def main():
    script_dir = Path(__file__).resolve().parent
    source_file = script_dir / "entry.png"
    
    if not source_file.is_file():
        raise FileNotFoundError(f"Source file not found: {source_file}")
        
    env_output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    output_dir = Path(env_output_dir) if env_output_dir else Path("/output")
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    destination_file = output_dir / "entry.png"
    shutil.copy2(source_file, destination_file)

if __name__ == "__main__":
    main()
