def stance_accuracy(y_true, y_pred):
    return sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true)


def confidence_weighted_score(predictions):
    return sum(p["confidence"] for p in predictions) / len(predictions)
