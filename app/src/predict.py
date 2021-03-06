import pickle

import pandas as pd
import re


def value_preprocess(val):
    return ''.join(['0' if c.isdigit() else c.lower() for c in val])


def regex_chars_sub(x):
    return re.sub("[a-z]", "X", x)


class Model:
    def __init__(self):
        with open("model.pkl", 'rb') as handle:
            self.models_dict = pickle.load(handle)

    def predict_our_model(self, in_str):
        ngrams_to_use = self.models_dict["ngrams_to_use"]
        words_to_use = self.models_dict["words_to_use"]
        model = self.models_dict["model"]

        preprocessed = value_preprocess(in_str)

        chars_replaced = regex_chars_sub(preprocessed)

        # X_for_pred = {}

        features = []
        for ngramm in ngrams_to_use:
            feature = chars_replaced.count(ngramm)
            # X_for_pred[ngramm] = chars_replaced.count(ngramm)
            features.append(feature)

        for word, _ in words_to_use:
            feature = preprocessed.count(word)
            # X_for_pred[word] = feature
            features.append(feature)

        # features = list(pd.Series(X_for_pred))
        prediction = model.predict([features])[0]
        return prediction


def main():
    model = Model()

    in_str = "Select Epigrams from the Greek Anthology"
    # in_str = "Between Ink and Shadows"

    prediction = model.predict_our_model(in_str)

    print(in_str)
    print(prediction)


if __name__ == "__main__":
    main()
