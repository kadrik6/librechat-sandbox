from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "sandbox_policy.md"

print("📜 Sandbox policy kontroll\n")

if not POLICY.exists():
    raise FileNotFoundError(f"sandbox_policy.md puudub: {POLICY}")

text = POLICY.read_text(encoding="utf-8")

required_sections = [
    "AI tohib",
    "AI ei tohi",
    "Kui infot ei ole piisavalt"
]

for section in required_sections:
    if section in text:
        print(f"✅ {section} olemas")
    else:
        print(f"❌ {section} puudub")
