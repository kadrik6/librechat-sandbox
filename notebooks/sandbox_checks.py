import sys

def run_check(label, func):
    print(f"\n▶️ {label}")
    try:
        func()
        print(f"✅ {label} – OK")
    except Exception as e:
        print(f"❌ {label} – FAIL")
        print(f"   {type(e).__name__}: {e}")
        sys.exit(1)

# ---- impordime olemasolevad checkid ----
from ingest_check import check_ingest_structure
from metadata_validation import validate_metadata
import policy_check  # policy_check jookseb importimisel

# ---- käivitame järjest ----
if __name__ == "__main__":
    print("🔐 Õigusloome AI Sandbox – tehniline kontroll\n")

    run_check("Ingest-struktuuri kontroll", check_ingest_structure)
    run_check("Metadata valideerimine", validate_metadata)

    print("\n▶️ AI kasutuspiirangute (policy) kontroll")
    # policy_check käivitub importimisel, seega kui siiani jõuame, on OK
    print("✅ AI kasutuspiirangud – OK")

    print("\n🎉 KÕIK KONTROLLID LÄBITUD")
