# System Architecture Overview

This project follows a **research-grade, modular pipeline**.

## High-Level Components

1. Data Ingestion (private)
   - YouTube API / manual export
   - Transcript extraction
   - Comment batching

2. Feature Layer (public)
   - Aspect taxonomy (taste, health, price, convenience)
   - Sentiment polarity & intensity
   - Reviewer stance signals

3. Modeling Layer (public)
   - Interpretable NLP models
   - Rule + ML hybrid approach
   - Bias checks across reviewer styles

4. Evaluation Layer (public)
   - Precision-focused metrics
   - Error taxonomy
   - Qualitative failure analysis

5. Visualization (private)
   - Dashboards
   - Temporal plots
   - Narrative summaries
