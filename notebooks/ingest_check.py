from pathlib import Path
import json

# Projekti juur (mitte cwd!)
ROOT = Path(__file__).resolve().parents[1]
RAG_DATA = ROOT / "rag_data"

def check_ingest_structure():
    print("🔍 Kontrollin ingest-struktuuri...\n")

    if not RAG_DATA.exists():
        raise FileNotFoundError(f"rag_data kausta ei leitud: {RAG_DATA}")

    for folder in RAG_DATA.iterdir():
        if not folder.is_dir() or folder.name.startswith("_"):
            continue

        print(f"📁 Kogum: {folder.name}")

        text_files = list(folder.glob("*.txt"))
        meta_path = folder / "metadata.json"

        if not text_files:
            print("  ❌ Puudub tekstifail")
        else:
            print(f"  ✅ Tekstifail(e): {[f.name for f in text_files]}")

        if not meta_path.exists():
            print("  ❌ Puudub metadata.json")
        else:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            print("  ✅ Metadata olemas:")
            for k, v in meta.items():
                print(f"     - {k}: {v}")

        print()

if __name__ == "__main__":
    check_ingest_structure()
