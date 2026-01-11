import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src" / "main"))

libs_path = project_root.parent / "libs"
sys.path.insert(0, str(libs_path / "grepx-orm" / "src"))
sys.path.insert(0, str(libs_path / "grepx-connection-registry" / "src"))
