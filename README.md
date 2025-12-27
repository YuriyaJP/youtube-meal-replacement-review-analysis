# Longitudinal Consumer Health Narrative Analysis (Case Study: Meal Replacement Product)

**Status:** Research Project (Ongoing)  
**Focus:** Multimodal ML for consumer health discourse analysis

## What This Is

A **multimodal machine learning project** analyzing how automated content systems interpret health product narratives across multiple data modalities:

- **Video transcripts** (spoken language → text modality)
- **User comments** (written text modality)  
- **Engagement signals** (numerical metadata: views, likes, timestamps)
- **Temporal patterns** (how narratives evolve over time)

**Research Question:**  
How do long-form self-experiment health narratives evolve over time, and how do audience communities reinforce or correct creator claims?

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

## Setup
```bash
pip install -r requirements.txt
export YOUTUBE_API_KEY="your_key_here"
python scripts/collect_data.py
```

## Data Privacy
- `data/raw/`: Contains original usernames (NOT committed)
- `data/public/`: Anonymized versions (safe to share)
- `data/sample/`: Small samples for documentation

## Ethical Considerations

1. **Public data only** (no login-required content)
2. **No personal identification** (anonymized examples)
3. **Explicit uncertainty** (no definitive health claims)
4. **Platform-as-case-study** (not product judgment)
5. **Open methodology** (reproducible, documented)

---
