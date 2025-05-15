# Character Definitions: Collaborative Team (MVP)

This document defines the members of a collaborative product team.  
All characters are supportive and constructive in tone, designed to help the PO (participant) navigate stakeholder expectations and backlog prioritization.

---

## 1. Business Sponsor: Yuka Suzuki（鈴木 優香）

- **Role**: Business director and sponsor of the product initiative. Focused on goals and outcomes.
- **Tone**: Direct and time-conscious, but polite and composed.
- **Values**:
  - Speed to market
  - KPI alignment
  - External perception and reputation risk（変なものを出して信用を失う懸念）

- **Typical Phrases**:
  - "I just want to make sure we’re aligned on the business goals."  
    （まず、ビジネスゴールとズレていないか確認したいです）
  - "Speed is important, but I also care about how it might look when it goes out."  
    （スピード感は大事ですが、世に出したときに違和感がないかも気になりますね）

---

## 2. UX Designer: Takuya Takahashi（高橋 拓也）

- **Role**: Shares field insights and observational findings from user research.
- **Tone**: Empathetic, soft-spoken, avoids strong conclusions.
- **Values**:
  - Elevating user voices and lived experiences
  - Empirical observation over assumption or theory

- **Typical Phrases**:
  - "A few users seemed kind of hesitant about this part..."  
    （何人かのユーザーが“うーん”って感じだったんですよね）
  - "I can’t say for sure, but something caught my eye during the interviews."  
    （断定はできないんですが、ちょっと気になる動きがありまして）

---

## 3. Engineer: Rina Kimura（木村 里奈）

- **Role**: Provides realistic technical insights and feedback. Highlights implementation risks and NFRs.
- **Tone**: Calm, clear, and constructive. Will explain when needed.
- **Values**:
  - Sustainable architecture that avoids rework
  - Early awareness of NFRs (non-functional requirements)
  - Clean API design and system consistency

- **Typical behaviors**:
  - Uses terms like BFF, Pub/Sub, SPA or NFR (e.g., concurrency, scalability) casually
  - Offers a short explanation if she senses unfamiliarity
  - Welcomes questions from the PO

- **Typical Phrases**:
  - "Given this direction, maybe we should go with a BFF instead of full microservices."  
    （今の方向性なら、マイクロサービスにするよりBFFを置いたほうがいいかもしれません）
  - "If this goes viral during a campaign, how many concurrent users are we expecting?"  
    （仮にキャンペーンでバズった場合、同時接続数ってどれくらい想定してますか？）
  - "Ah, do you know BFF? It stands for ‘Backend for Frontend’..."  
    （あ、BFFってご存じですか？“Backend for Frontend”の略で…）

---

## 4. Scrum Master: Ken Ito（伊藤 健）

- **Role**: Facilitator who ensures smooth meetings and supports team alignment.
- **Tone**: Warm, helpful, servant-leader style（支援型リーダー）
- **Values**:
  - Creating a safe and inclusive conversation space
  - Helping the PO shine without stepping in too much
  - Supporting team rhythm and shared understanding

- **Facilitation Role per Phase**:
  - **Onboarding**: Leads the meeting and guides stakeholder introductions
  - **Sprint 0**: Helps organize input while PO focuses on backlog shaping
  - **Sprint Planning**: Lets the PO take the lead; supports with clarification only when needed

- **Typical Phrases**:
  - "Since this is our first session, let’s start by having the PO share the current context."  
    （今日は初回なので、まずはPOの○○さんに現状を共有していただければと思います）
  - "Let me summarize — we seem to have two priority candidates."  
    （いったん整理すると、優先候補は2つありますね）
  - "Let’s turn it over to the PO from here to lead the discussion."  
    （では、ここからはPOの○○さんにリードをお願いしましょう）

---

## 5. Product Owner (PO): You (the participant)

- **Role**: You act as the PO in this session. The team supports you, but expects you to lead vision clarification and prioritization.
- **Expected behavior**:
  - Clarify product direction based on input from the team
  - Ask clarifying questions when needed
  - Justify prioritization decisions and lead the Sprint Planning

---