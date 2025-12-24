# Multimodal Narrative Risk Analysis: Health Product Discourse

**Status:** Research Project (Ongoing)  
**Focus:** Multimodal ML for consumer health discourse analysis

## What This Is

A **multimodal machine learning project** analyzing how automated content systems interpret health product narratives across multiple data modalities:

- **Video transcripts** (spoken language → text modality)
- **User comments** (written text modality)  
- **Engagement signals** (numerical metadata: views, likes, timestamps)
- **Temporal patterns** (how narratives evolve over time)

**Research Question:**  
*How do narrative trajectories differ between high-engagement content (YouTube) and community discourse (comments), and what does multimodal fusion reveal about safe consumer analytics design?*

---

## Why Multimodal?

Traditional unimodal analysis (text-only sentiment) misses:
- **Temporal dynamics:** How claims escalate from hedged ("I felt bloated") to definitive ("Huel causes bloating")
- **Engagement signals:** Rare dramatic narratives get amplified algorithmically despite low prevalence
- **Cross-modal gaps:** What creators say ≠ what audiences hear ≠ what communities discuss
- **Platform effects:** YouTube (performative) vs Reddit (community-validated)

**This project demonstrates multimodal fusion** to detect these gaps.

---

# Multimodal Narrative Analysis: Creator Claims vs Audience Reality

## Research Question
**"When health product reviewers make claims in videos, do their audience's comments validate or contradict those claims—and what does this gap tell us about algorithmic amplification risk?"**

## Modalities
1. **Video Transcripts** (creator narrative)
2. **Video Comments** (audience experiences)
3. **Engagement Signals** (views, likes, comment velocity)
4. **Temporal Patterns** (narrative evolution, comment timing)

## Key Insight
High-engagement videos with dramatic health claims often have comment sections full of:
- "This didn't happen to me"
- "My experience was different"
- "Clickbait"

But automated systems trained on *video content alone* would miss this validation gap.

## This Is Multimodal Because:
You're **aligning two text modalities in same context**:
- What the creator **claims** (video)
- What the audience **experiences** (comments)
- Weighted by **engagement signals** (algorithmic amplification)
- Tracked across **time** (narrative trajectory)


---

## Data Architecture
```
[YouTube Videos] ────────┐
                         ├──> [Multimodal Fusion]
[Video Transcripts] ─────┤         |
[User Comments] ─────────┤         v
[Engagement Metrics] ────┤    [Trajectory Modeling]
[Timestamps] ────────────┘         |
                                   v
                [Comments] ──> [Validation]
                                   |
                                   v
                            [Safety Analysis]
                                   |
                                   v
                            [Interpretable Outputs]
---
```

## Tech Stack

**Multimodal ML:**
- `sentence-transformers` (text embeddings)
- `openai` (LLM-assisted claim extraction)
- `hmmlearn` (temporal sequence modeling)
- `scikit-learn` (fusion & classification)

**Data Collection:**
- `youtube-transcript-api` (transcript modality)
- YouTube Data API (engagement modality)

**Visualization:**
- `plotly` (interactive multimodal visualizations)
- `matplotlib` (trajectory plots)

---

## Ethical Considerations

1. **Public data only** (no login-required content)
2. **No personal identification** (anonymized examples)
3. **Explicit uncertainty** (no definitive health claims)
4. **Platform-as-case-study** (not product judgment)
5. **Open methodology** (reproducible, documented)

---

## Author

**Yulia Chekhovska**  
Background: Psycholinguistics → Data Science  
Focus: Multimodal ML for consumer health & AI safety

[LinkedIn](linkedin.com/in/yuliia-che) | [Portfolio](yuriyajp.github.io)

---

*This project applies multimodal ML principles to health discourse, demonstrating fusion techniques and safety-aware analytics for consumer-facing AI systems.*