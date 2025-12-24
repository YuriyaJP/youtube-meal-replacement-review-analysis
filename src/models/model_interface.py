class ReviewModel:
    """
    Abstract interface for review analysis models.
    """

    def predict(self, text: str) -> dict:
        """
        Returns structured sentiment and stance signals.
        """
        raise NotImplementedError
