import argparse
import yaml
from pathlib import Path
from datetime import datetime
import re

# --- Constants ---
SAFETY_PATH = Path("shared/roleplay_safety.md")
TEMPLATE_DIR = Path("shared/templates/prompts")
DEFAULT_TEMPLATES = [
    ("01_intro", TEMPLATE_DIR / "01_initialize_template.md"),
    ("03_roleplay", Path("roles/po/prompts") / "03_roleplay_template.md"),
    ("04_reflection", TEMPLATE_DIR / "04_reflection_template.md"),
]

# --- Functions ---
def load_fill_map(config_path: Path) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["fill_map"]

def resolve_source(source_key: str, fill_map: dict) -> Path:
    if source_key == "roleplay_safety":
        return SAFETY_PATH
    if source_key not in fill_map:
        raise ValueError(f"Unknown source_key in template: {source_key}")
    mapping = fill_map[source_key]
    return Path(mapping["dir"]) / mapping["file"]

def substitute_placeholders(template: str, fill_map: dict) -> str:
    pattern = r"<!-- TO_BE_FILLED_FROM: (.+?) -->"
    matches = re.findall(pattern, template)
    for key in matches:
        source_path = resolve_source(key, fill_map)
        if not source_path.exists():
            raise FileNotFoundError(f"Missing file for '{key}': {source_path}")
        content = source_path.read_text(encoding="utf-8").strip()
        template = template.replace(f"<!-- TO_BE_FILLED_FROM: {key} -->", content)
    return template

def main():
    parser = argparse.ArgumentParser(description="Build assessment prompt files.")
    parser.add_argument("--role", default="po")
    parser.add_argument("--variant", default="default")
    parser.add_argument("--config", default="config/po.yaml")
    args = parser.parse_args()

    # Prepare output directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    output_dir = Path("build") / args.role / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load fill_map
    fill_map = load_fill_map(Path(args.config))

    # Extract names for output filenames
    character_name = Path(fill_map["character"]["file"]).stem
    product_name = Path(fill_map["product"]["file"]).stem

    # Process each template
    for label, template_path in DEFAULT_TEMPLATES:
        with open(template_path, "r", encoding="utf-8") as f:
            template = f.read()

        filled = substitute_placeholders(template, fill_map)

        filename = f"{label}-{args.role}-{character_name}-{product_name}.md"
        output_path = output_dir / filename
        output_path.write_text(filled, encoding="utf-8")
        print(f"✅ Built: {output_path}")

    # Copy evaluation_criteria file as 02_evaluation_criteria-...md
    eval_path = resolve_source("evaluation_criteria", fill_map)
    eval_filename = f"02_evaluation_criteria-{args.role}-{character_name}-{product_name}.md"
    eval_output_path = output_dir / eval_filename
    eval_content = eval_path.read_text(encoding="utf-8").strip()
    eval_output_path.write_text(eval_content, encoding="utf-8")
    print(f"✅ Built: {eval_output_path}")

if __name__ == "__main__":
    main()
