from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
RAG_DATA = ROOT / "rag_data"
RULES_PATH = RAG_DATA / "_collection_rules.json"

def validate_metadata():
    print("🧪 Metadata valideerimine\n")

    if not RULES_PATH.exists():
        raise FileNotFoundError(f"_collection_rules.json puudub: {RULES_PATH}")

    rules = json.loads(RULES_PATH.read_text(encoding="utf-8"))

    for folder in RAG_DATA.iterdir():
        if not folder.is_dir() or folder.name.startswith("_"):
            continue

        print(f"📁 {folder.name}")

        meta_path = folder / "metadata.json"
        if not meta_path.exists():
            print("  ❌ metadata.json puudub\n")
            continue

        meta = json.loads(meta_path.read_text(encoding="utf-8"))

        for field in rules["required_metadata_fields"]:
            if field not in meta:
                print(f"  ❌ Puudub väli: {field}")
            else:
                print(f"  ✅ {field}: {meta[field]}")

        if "allowed_status" in rules:
            if meta.get("status") not in rules["allowed_status"]:
                print("  ❌ Staatuse väärtus ei ole lubatud")

        print()

if __name__ == "__main__":
    validate_metadata()
