

# ADR-0002: 出力フォーマットの標準（Markdown 本文 + 末尾 JSON）

- **Status**: Accepted  
- **Date**: 2025-08-21  
- **Deciders**: Team (Skill Assessment / Cursor PoC)  
- **Scope**: このリポで運用する **スキルアセスメント用テンプレート**（`docs/templates/*.md`）と、その出力。ChatGPT/Gemini などモデル横断で適用する。

---

## 背景 / Context

- 本リポは **学習の初速と再現性** を重視する。レビューは人間にやさしく、**検証は機械で厳格**にしたい。  
- そこで、人間が読む **Markdown 本文** と、CI 等で機械が検証できる **厳格な JSON** を **1つの出力に同居**させる方針を検討した。  
- JSON であれば `jq` などで **Yes/No 判定や集計**が容易。Markdown のみ／自由形式のみだと、**再確認・比較・KPI 化**が難しい。

---

## 決定 / Decision

1. **共通ルール**（全モデル共通）
   - 出力は **「本文（要約/表など）＋ 末尾に *厳格な JSON*」** とする。  
   - JSON は **コードフェンス ```json** を用い、**1ブロックのみ**。**コメント・末尾カンマ禁止**。  
   - JSON **キーは英語**で固定（機械処理との互換性のため）。  
   - JSON の後ろに **余分な文字列を置かない**（抽出を単純化するため）。

2. **ChatGPT 向け**  
   - スタイルは **Markdown 本文 + JSON in Markdown（末尾）**。  
   - 例：Summary / Findings / Next Steps の本文の後に、**検証可能な JSON** を 1 つだけ置く。

3. **Gemini 向け**  
   - 本文冒頭に **Markdown 表**（人が読みやすい）を置き、**末尾に JSON** を付ける（**Table + JSON tail**）。

4. **自動化モード（任意）**  
   - CI やスクリプトでの完全自動処理が必要な場合、**JSON のみ**を返すモードをテンプレで指示可能にする。

---

## 意思決定のドライバ / Decision Drivers

- **可読性×検証性**：本文は速く読める／JSON は確実に検証・比較できる。  
- **道具の豊富さ**：`jq` での検証・抽出が容易、差分比較も `jq -S` で安定。  
- **テンプレの持続可能性**：本文の表現は変えても、**JSON スキーマは不変**で継続運用できる。

---

## 影響 / Consequences

**メリット**
- レビューは本文中心で流れよく、**CI では JSON を機械検証**できる。  
- 学習ログや結果を **自動集計** しやすい（CSV/NDJSON へ変換も容易）。  
- ChatGPT/Gemini 間で **共通の最小スキーマ** を維持できる。

**デメリット（リスク）と緩和策**
- 本文と JSON の **二重記述の手間**：テンプレ側で骨組みを提供し、**Cursor で自動生成**する。  
- モデルが JSON に **装飾を混入**する可能性：テンプレで「**```json 内は JSON のみ**」と明記し、CI で `jq -e` を通す。

---

## 適用方法 / How this is applied

- **core.md（Output/Evidence/Quality）** で本 ADR を参照する。  
- **テンプレ構成**  
  - ChatGPT: 「Summary / Findings / Next Steps …」→ **```json …```（1ブロック）**  
  - Gemini: 「Assessment（Markdown 表）」→ **```json …```（1ブロック）**  
- **CI/ローカル検証**（例）  
  - JSON 抽出:  
    ```bash
    awk '/```json/{f=1;next}/```/{f=0}f' docs/templates/skill-assessment.chatgpt.md | jq -e .
    ```  
  - 正規化比較:  
    ```bash
    jq -S . a.json > a.norm.json && jq -S . b.json > b.norm.json && diff -u a.norm.json b.norm.json
    ```

---

## 最小スキーマ例 / Minimal Schema Example

> 実際のキーはテンプレに準拠（英語）。ここでは最小例を示す。

```json
{
  "score": { "design": 0, "code": 0, "tests": 0 },
  "risks": ["..."],
  "deltas": ["..."],
  "next_steps": ["..."],
  "evidence": ["docs/adr/adr-0001-prompt-language.md"]
}
```

---

## 代替案 / Considered Options

1) **Markdown のみ**  
   - Pros: 人は読みやすい  
   - Cons: 機械検証が困難、再集計・比較が面倒

2) **JSON のみ**  
   - Pros: 自動処理が容易  
   - Cons: レビューの体験が悪く、学習ログの読み物として不向き

3) **YAML**  
   - Pros: 人が読みやすい  
   - Cons: 厳格性が JSON より弱く、検証ツールの標準性もやや劣る

→ 本目的（**学習効率×機械検証**）に最適なのは **Markdown 本文 + 末尾 JSON**。

---

## フォローアップ / Follow-ups

- [ ] `/.cursor/rules/core.md` の **Output/Evidence/Quality** を本 ADR に合わせて追記  
- [ ] `docs/templates/skill-assessment.chatgpt.md` / `.gemini.md` を本形式で作成  
- [ ] `.github/workflows/policy.yml` と `scripts/verify.sh`（または `scripts/check_core.py`）で **`jq -e` 検証**を組み込む  
- [ ] `docs/learning-log/` で結果 JSON の抜粋と所見を残し、再利用可能なサンプルとして蓄積

---

## 参照 / References

- ADR-0001: プロンプト言語は日本語（Cursor 指定時のみ例外）  
- `/.cursor/rules/core.md`（Language / Output / Evidence / Quality）  
- README: Purpose と運用（Ask → Composer → Agent）