"""Train the insurance charges model and report its performance.

Regenerates linear_regression_model.pkl and min_max_values.json from
Health_insurance.csv so the shipped artefacts and the reported metrics
always come from the same fit.

Usage:  python train.py
"""

import json

import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_score

DATA = "Health_insurance.csv"
MODEL_OUT = "linear_regression_model.pkl"
SCALER_OUT = "min_max_values.json"

# Continuous columns are min-max scaled; children is left on its native scale.
SCALED = ["age", "bmi", "heart rate", "Creatinine", "glucose"]

FEATURES = [
    "age", "bmi", "children", "diabetes", "heart rate", "Creatinine", "glucose",
    "sex_female", "smoker_no",
    "region_northeast", "region_northwest", "region_southeast", "region_southwest",
]


def build_features(df, ranges):
    out = pd.DataFrame(index=df.index)
    for col in SCALED:
        lo, hi = ranges[col]
        out[col] = (df[col] - lo) / (hi - lo)
    out["children"] = df["children"]
    out["diabetes"] = df["diabetes"]
    out["sex_female"] = (df["sex"] == "female").astype(int)
    out["smoker_no"] = (df["smoker"] == "no").astype(int)
    for region in ["northeast", "northwest", "southeast", "southwest"]:
        out["region_" + region] = (df["region"] == region).astype(int)
    return out[FEATURES]


def main():
    raw = pd.read_csv(DATA)
    df = raw.dropna(subset=SCALED + ["sex", "smoker", "region", "children", "diabetes", "charges"])
    print("rows: %d total, %d complete cases used" % (len(raw), len(df)))

    ranges = {c: [float(df[c].min()), float(df[c].max())] for c in SCALED}
    X = build_features(df, ranges)
    y = df["charges"].values

    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    r2 = cross_val_score(LinearRegression(), X, y, cv=cv, scoring="r2")
    rmse = -cross_val_score(LinearRegression(), X, y, cv=cv, scoring="neg_root_mean_squared_error")

    model = LinearRegression().fit(X, y)
    pred = model.predict(X)

    print("\n5-fold cross-validation")
    print("  R2   %.4f   (folds %s)" % (r2.mean(), np.round(r2, 3)))
    print("  RMSE %.0f" % rmse.mean())
    print("\nIn-sample")
    print("  R2   %.4f" % r2_score(y, pred))
    print("  RMSE %.0f" % np.sqrt(mean_squared_error(y, pred)))
    print("  MAE  %.0f" % mean_absolute_error(y, pred))

    smoker = df[["smoker"]].eq("no").astype(int)
    solo = LinearRegression().fit(smoker, y)
    print("\nR2 from smoker status alone: %.4f" % r2_score(y, solo.predict(smoker)))

    print("\nCoefficients")
    for name, coef in zip(FEATURES, model.coef_):
        print("  %-18s %12.2f" % (name, coef))
    print("  %-18s %12.2f" % ("(intercept)", model.intercept_))

    joblib.dump(model, MODEL_OUT)
    with open(SCALER_OUT, "w") as fh:
        json.dump(ranges, fh)
    print("\nwrote %s and %s" % (MODEL_OUT, SCALER_OUT))


if __name__ == "__main__":
    main()
