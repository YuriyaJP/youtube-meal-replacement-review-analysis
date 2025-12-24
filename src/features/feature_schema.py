"""
Defines the core analytical features extracted from review text.
"""

ASPECTS = [
    "taste",
    "satiety",
    "health_perception",
    "digestibility",
    "price_value",
    "convenience",
]

STANCE_LABELS = [
    "positive",
    "neutral",
    "skeptical",
    "negative",
]

FEATURE_SCHEMA = {
    "aspect": str,
    "sentiment_score": float,
    "stance": str,
    "confidence": float,
}
