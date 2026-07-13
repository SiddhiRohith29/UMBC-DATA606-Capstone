# Predicting Airline Passenger Satisfaction ✈️

**M.S. Data Science Capstone · UMBC · Spring 2024** — end-to-end machine-learning project: from raw survey data to a deployed, interactive prediction app.

📽️ [Presentation](https://docs.google.com/presentation/d/1D2ZD5IGPQSVOYRwgnUr_8oNiw0O5a9qA/edit#slide=id.p1) · 🎥 [Video walkthrough](https://youtu.be/OxhX6iiS7RU) · 📄 [Full report](docs/FinalReport.md)

## Problem

Airlines collect mountains of passenger feedback but struggle to answer one question: **which service factors actually drive satisfaction — and can we predict it for a given passenger?**

Research questions:
1. What demographic factors most influence satisfaction?
2. How do onboard services (Wi-Fi, cleanliness, food, entertainment, boarding) impact it?
3. What does a flight delay really cost in satisfaction terms?
4. How do class, travel type, and flight distance interact with satisfaction?

## Approach

| Stage | What was done |
|---|---|
| **EDA** | Demographic distributions, service-rating correlations, delay-impact analysis on 100K+ passenger records |
| **Prep** | Cleaning, encoding, feature selection; 70/30 train–test split |
| **Models** | Logistic Regression → KNN → Random Forest → Gradient Boost → **XGBoost**, compared on accuracy, classification report, and ROC-AUC |
| **Tuning** | Grid search + cross-validation on the best performer; overfit checks |
| **Deployment** | Best model pickled and served through a **Streamlit web app** where users rate services 1–5 and get a live satisfaction prediction |

## Results

- Tree-based ensembles (Random Forest / XGBoost) delivered the strongest, well-generalized performance (validated via ROC-AUC + cross-validation).
- Onboard service quality, online boarding, and in-flight Wi-Fi emerged as dominant satisfaction drivers; delays showed a measurable negative impact.
- Fully working prediction app — see `app/app.py`.

## Repo structure

```
├─ app/         # Streamlit app + pickled best model
├─ data/        # dataset + report images
├─ docs/        # proposal, final report, presentation assets
└─ notebooks/   # EDA + modeling notebooks
```

## Run the app

```bash
pip install streamlit scikit-learn numpy requests
streamlit run app/app.py
```

## Author

**Siddhidhatri Rohith Reddy Jaggari** — Data Analyst (payments / fraud / risk)
[LinkedIn](https://www.linkedin.com/in/siddhidhatri-rohith-reddy-jaggari) · [GitHub](https://github.com/SiddhiRohith29)

*Capstone prepared for the UMBC Data Science Master's program under Dr. Chaojie (Jay) Wang.*
