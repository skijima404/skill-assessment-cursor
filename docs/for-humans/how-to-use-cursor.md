# 初めてCursor使う人がHello Worldを作れるようになるための進め方

Cursor = VSCode (にすごく似たEditor) にGenAIがくっついて、積極的にリポジトリの中身を見に行ってくれていろいろやってくれるGenAI

## 初期設定

macOSアプリ版  
Cursor > Settings > Cursor Settings > Chat > Include Full-Folder Context を入れておくと、フォルダを指定したときにフォルダ以下全部読んでくれるのでおすすめ。

---

## .cursor/rules/core.md 作成
このファイルはCursorがコーディング時の必須条件を探しに行くファイルなので、必須条件はここに書く。

- Measurableなものをおくこと。
- あまり内容を増やしすぎないこと。Measurableではないもの、方針などは別に書く。
    - このリポジトリの場合は、docs/for-models あたりに格納している
    - コーディング規約もdocs/for-modelsとかの方が適切

---

## Cursorには要件の「ふわふわ段階」から相談可能

チャットにはAskモードとAgentモードがある
まだ考えが固まってないとか、モヤモヤしているならAskモードで相談すると良い

### **Askモード**
**用途**: 質問・相談・情報収集・理解確認
- ファイル読み込み、検索、分析
- 既存コードの理解
- 設計方針の相談
- デバッグやエラー解析

**特徴**:
- ファイルを**読む**ことに特化
- 複数のツール（search、grep、read_file等）を並列実行
- 情報を集めて提案・アドバイスする
- **実際にファイルを変更しない**

### **Agentモード**
**用途**: 実際の作業・ファイル作成・編集
- 新規ファイル作成
- コード編集・修正
- ファイルの移動・削除
- 設定ファイルの変更

**特徴**:
- **write**ツールが使える
- 実際にプロジェクトを変更する
- より「実行」に特化
- 慎重な確認が必要

### 注意
1ユーザーあたりの利用制限 (Quota) があるので、何でもかんでもCursorでやっていると一瞬で使い潰す可能性あり。  
Askモード便利だけど、可能であればある程度Gemini等他のGenAIで固めた資材を持ってきて、実装の相談あたりからCursorでやると良い。
(Askモードの裏側GPTとかClaudeなんで、要件定義とかも「結構できる子」。)

Quota確認方法:
- macOSアプリ > Cursor > Settings > Cursor Settings > Manage Accountで現在の利用量を確認できる

---

## 合意事項はMarkdownにしておく

Askモードで相談してある程度固まったら、固まった内容は合意事項としてMarkdownとして吐き出し、都度Cursorが参照できるようにしておくと良い。  
GenAIはなんだかんだ忘れるので、Remindする仕掛けにする。

このリポジトリでは、
- docs/ 直下
    - 人もGenAIも読むもの
- docs/for-models
    - 主にGenAIが読むもの
- docs/adr
    - Architectural Decision Records。アーキテクチャ的な意思決定と方針、その理由が書いてある

ファイルやフォルダを明示的にCursorに参照させる場合は、左ペインのフォルダ一覧からチャットウインドウに Drag & Drop。
