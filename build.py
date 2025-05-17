# build.py

import os
from pathlib import Path

def main():
    print("🚧 Build script started!")
    # 出力先を仮で定義
    output_dir = Path("build/po/default")
    output_dir.mkdir(parents=True, exist_ok=True)

    # テンプレートファイル（例）
    template_path = Path("shared/templates/prompts/03_reflection_template.md")
    output_path = output_dir / "03_reflection.md"

    # テンプレート読み込み
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # 差し込み（今回はダミーで1箇所だけ）
    filled = template.replace("<!-- TO_BE_FILLED_FROM: evaluation_criteria.md -->", "👀 ←ここに評価基準が入ります")

    # 出力
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(filled)

    print(f"✅ Output written to: {output_path}")

if __name__ == "__main__":
    main()