

# skill-assessment-cursor

> **目的**  
> このリポジトリは、**Cursor を前提**に、プロダクト方針や ADR を読み込ませて  
> **スキルアセスメント用のプロンプトテンプレート（ChatGPT / Gemini）** を生成・運用するための土台です。
> CursorのArtifactや学習記録は一式ここに格納します。

---

## 範囲 / 非対象

- **範囲（Scope）**
  - Cursor の運用型（**Ask → Composer → Agent**）のテンプレ化
  - 方針/ADR/アーキ図などの文脈を **@files / @folders** で添付する前提のワークフロー
  - 生成物（テンプレ）の保管・差分管理（PR ベース）

- **非対象（Non-goals）**
  - 本格 UI / 認証 / DB 実装
  - 大規模 E2E（PoC では smoke のみ）

---

## リポジトリ構成

```
/cursor/
  └─ rules/core.md        # 生成・改変時に“常に守る原則”（薄く 5–7 行を推奨）
/docs/
  /for-models/            # モデルに渡す背景（1 ページ×複数）
    ├─ product-brief.md
    └─ prompt-principles.md
  /templates/             # 生成されたテンプレの格納先（ChatGPT/Gemini）
  ├─ PromptLog.md         # 失敗→再指示→改善の軽い記録（2–3 例で十分）
  └─ CompletionMatrix.md  # 要件 ↔ 実装 ↔ 証拠（URL/スクショ）のトレース表
/reference/               # 参照用の旧資料 (読む、リンクする) ※ 編集可
/archived/                # 凍結済みの過去資材（編集しない）
README.md
```

> 旧ファイルは一括で `archive/` に退避済み。参照継続が必要なものは `reference/` に戻します。  
> 実働に使う短文は **`/docs/for-models` と `/.cursor/rules` に新規作成**します。

---

## クイックスタート（5 分）

### 0) 前提
- Cursor が使えること（Ask / Composer / Agent）。
- `/.cursor/rules/core.md` と `/docs/for-models/*` を用意（無ければ本 README のサンプルを参考に作成）。

### 1) Notepad の登録（推奨）
Cursor の Notepad に **「SkillAssessment」** を作成し、以下を保存します（1 ページ）。

```md
# Cursor-Guide (SkillAssessment)
- 使い分け: Ask=読解/章立て合意 → Composer=骨組み → Agent=横断改変(MR前提)
- 毎回付ける: @files .cursor/rules/core.md, @files docs/for-models/product-brief.md, @files docs/for-models/prompt-principles.md
- 失敗時: Askで影響要約→A/B案→Agentで適用（差分は最小）
```

### 2) 合意（Ask）
以下を Cursor に貼り付け、章立てを合意します（ChatGPT / Gemini の差分も 3 行で）。

```text
@files .cursor/rules/core.md
@files docs/for-models/product-brief.md
@files docs/for-models/prompt-principles.md
目的：スキルアセスメント・プロンプトテンプレ（ChatGPT/Gemini）を設計。
成果：共通章立てとモデル差分の提案（理由を3行）。
```

### 3) 骨組み（Composer）
Ask の合意に沿って、テンプレの骨組みを生成します。

```
docs/templates/skill-assessment.chatgpt.md
docs/templates/skill-assessment.gemini.md
```

**必須内容（例）**
- System / (Developer 任意) / User scaffold  
- Guardrails（差分最小・根拠の一行・ブロック時の質問）  
- Context の添付指示（@files/@folders、**自動参照はしない**旨を明記）  
- Output schema（ChatGPT=JSON in Markdown、Gemini=表+JSON尻）  
- Few-shot スロット / Self-check（自己テスト）

### 4) 横断改変（Agent）
2 つのテンプレに対して、変数とガードレールを統一します（MR 前提）。

```text
@files docs/templates/skill-assessment.chatgpt.md
@files docs/templates/skill-assessment.gemini.md
@files .cursor/rules/core.md
次を反映：
1) 変数: {{product_goals}}, {{target_users}}, {{non_goals}}, {{nfr}}, {{scoring_rubric}}, {{output_format}}
2) 各テンプレ冒頭に「@files で ADR/図を添付すること」を明記
3) 変更理由を3点で出力し、MRを作成
```

### 5) スモーク（10 分デモ想定）
- ChatGPT/Gemini にテンプレを投げ、**出力形式**と**根拠の明示**を確認。  
- `docs/PromptLog.md` に **成功/失敗を 2 件だけ**追記（厚くしない）。

---

## Cursor 運用の型（覚えやすい版）

| 目的 | 使うもの | コツ |
|---|---|---|
| 仕様の確認・方針の比較 | **Ask** | `@Notepad + @files` を毎回付ける |
| 新規ファイルの骨組み | **Composer** | 先に Ask で章立てを合意 |
| 既存コードの横断修正 | **Agent** | 差分最小・MR前提・必要なら `@git@Commit` |

- **Rules は薄く先に**（`.cursor/rules/core.md` は 5–7 行）  
- **背景は Notepad / `/docs/for-models`** に置く（厚い原稿は `reference/`）  
- **@context を厳密に**（`@files`, `@folders`, 必要に応じて `@git@Commit`）

---

## ブランチ / PR

- **命名例**  
  - 整理: `chore/repo-tidy` / `chore/archive-sweep`  
  - 初期敷設: `chore/init-cursor-scaffold`  
- **コミット例**  
  - `chore(repo): move legacy materials to archive/`  
  - `docs(templates): add skill-assessment scaffolds`  
- CI が重い場合は初回整理 PR に限り **`[skip ci]`** を使用可。

---

## Upstream 同期（任意）

このリポが元リポの複製で、同期したい場合は `upstream` を追加して定期的に取り込みます。

```bash
git remote add upstream https://github.com/<owner>/<original-repo>.git
git fetch upstream
git merge upstream/main   # or: git rebase upstream/main
```

---

## FAQ

- **Notepad と rules の違いは？**  
  Notepad は「毎回読む背景の束」。rules は「常に守る最小原則」。両方を同時に使うと安定します。

- **Markdown に `@files` と書けば自動参照される？**  
  されません。**チャット側で @ を付けて添付**してください（明示が前提）。

- **旧資料はどう扱う？**  
  `archive/` は凍結、`reference/` は参照用。必要時にだけ `reference/` へ戻します。

---

## License

必要に応じて追記してください。