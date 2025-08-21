# Core Rules

- **Language**: プロンプト/READMEは日本語。Cursorや外部ツールが特定言語を明示要求した場合のみ例外。外部公開例は英訳可。  
  *(Ref: docs/adr/adr-0001-prompt-language.md)*

- **Output**: ChatGPT＝**Markdown本文 + 末尾に```json 1ブロック**（コメント/末尾カンマ禁止、`jq -e` で検証可）。Gemini＝**Markdown表 + JSON tail**（表→末尾に```json 1ブロック）。  
  *(Ref: docs/adr/adr-0002-prompt-format.md)*

- **Evidence**: 各 **score / recommendation** に **根拠1行** を必須（対象ファイル/行または ADR ID を示す）。**欠落はNG**。

- **Quality**: テンプレは **Self-check** 節を保持。出力の JSON は **必須キー**（`score`,`risks`,`deltas`,`next_steps`,`evidence`）を含み、**構文エラーは再生成**。
