"""Comprobaciones rápidas que no consumen la API de Gemini."""

from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def main() -> None:
    files = sorted(DATA.glob("*.pdf"))
    assert len(files) == 3, f"Se esperaban 3 PDF y se encontraron {len(files)}."

    total_pages = 0
    for path in files:
        reader = PdfReader(str(path))
        assert reader.pages, f"{path.name} no contiene páginas."
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        assert len(text.strip()) > 300, f"{path.name} parece no contener texto."
        total_pages += len(reader.pages)
        print(f"OK: {path.name} ({len(reader.pages)} páginas)")

    print(f"\nBase documental válida: {len(files)} archivos, {total_pages} páginas.")


if __name__ == "__main__":
    main()
