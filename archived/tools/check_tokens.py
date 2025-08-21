import argparse
from pathlib import Path
import tiktoken

ENCODING = "cl100k_base"  # GPT-4 and GPT-3.5 use this

def count_tokens(text: str) -> int:
    enc = tiktoken.get_encoding(ENCODING)
    return len(enc.encode(text))

def scan_files(directory: Path):
    print(f"📂 Scanning: {directory}\n")
    total_tokens = 0
    oversized_files = []

    for file_path in sorted(directory.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")
        tokens = count_tokens(content)
        total_tokens += tokens

        mark = "⚠️" if tokens > 1000 else "✅"
        print(f"{mark} {file_path.name:<60} : {tokens:>5} tokens")

        if tokens > 1000:
            oversized_files.append((file_path.name, tokens))

    print("\n------------------------------------------------------------")
    print(f"🧮 Total tokens across files: {total_tokens}")

    if oversized_files:
        print("\n⚠️  Files exceeding 1000 tokens:")
        for name, tokens in oversized_files:
            print(f"   - {name} ({tokens} tokens)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count approximate tokens in Markdown files.")
    parser.add_argument("--path", type=str, required=True, help="Path to folder containing .md files")
    args = parser.parse_args()

    scan_files(Path(args.path))
