"""
AI Sales Lead Prediction & Analytics System
-------------------------------------------
Professional Streamlit application for:

1. Individual lead conversion prediction
2. Lead prioritization
3. Sales analytics dashboard
4. Batch lead prediction
5. Model performance information

Author: Hadi Inamdar
Project: JZD Technologies Assignment
"""

import os
import logging
from datetime import datetime

import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Sales Lead Predictor",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOGGING CONFIGURATION
# ============================================================

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ============================================================
# PATH CONFIGURATION
# ============================================================

DATA_PATH = os.getenv(
    "DATA_PATH",
    "04_jzd_sales_data.csv"
)

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "models/lead_conversion_model.joblib"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .sub-title {
        font-size: 18px;
        color: #6c757d;
        margin-bottom: 30px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        background-color: #f8f9fa;
        border: 1px solid #e9ecef;
    }

    .high-priority {
        padding: 15px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: #d1fae5;
        color: #065f46;
    }

    .medium-priority {
        padding: 15px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: #fef3c7;
        color: #92400e;
    }

    .low-priority {
        padding: 15px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background-color: #fee2e2;
        color: #991b1b;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# DATA LOADING FUNCTIONS
# ============================================================

@st.cache_data
def load_data(path):
    """
    Load sales lead dataset.

    Parameters
    ----------
    path : str
        Path to the CSV dataset.

    Returns
    -------
    pandas.DataFrame
    """

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Dataset not found: {path}"
        )

    data = pd.read_csv(path)

    logger.info(
        "Dataset loaded successfully. Shape=%s",
        data.shape
    )

    return data


@st.cache_resource
def load_model(path):
    """
    Load trained machine learning model.

    Returns
    -------
    dict
        Saved model artifact.
    """

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model not found: {path}. "
            "Run the training notebook first."
        )

    artifact = joblib.load(path)

    logger.info("ML model loaded successfully.")

    return artifact


# ============================================================
# BUSINESS LOGIC
# ============================================================

def get_priority(probability):
    """
    Convert conversion probability into lead priority.
    """

    if probability >= 0.80:
        return "HIGH", "🔥 High Priority"

    elif probability >= 0.50:
        return "MEDIUM", "⚡ Medium Priority"

    return "LOW", "🔵 Low Priority"


def get_recommendation(probability, priority):
    """
    Generate sales recommendation based on AI prediction.
    """

    if priority == "HIGH":
        return (
            "This lead has a strong probability of conversion. "
            "The sales team should contact the lead immediately "
            "and prioritize personalized follow-up."
        )

    elif priority == "MEDIUM":
        return (
            "This lead shows moderate conversion potential. "
            "Schedule structured follow-ups and provide relevant "
            "service information to improve conversion chances."
        )

    return (
        "This lead currently has a lower conversion probability. "
        "Use automated nurturing campaigns and avoid allocating "
        "high-cost sales resources until stronger engagement signals appear."
    )


# ============================================================
# APPLICATION INITIALIZATION
# ============================================================

try:

    df = load_data(DATA_PATH)
    model_artifact = load_model(MODEL_PATH)

    model = model_artifact["model"]

    FEATURES = model_artifact.get(
        "features",
        [
            "industry",
            "service",
            "lead_source",
            "budget_inr",
            "first_response_hours",
            "followup_count"
        ]
    )

except Exception as error:

    logger.exception("Application initialization failed.")

    st.error(
        f"Application failed to start: {error}"
    )

    st.info(
        "Please ensure the CSV dataset and trained "
        "model file are available."
    )

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🎯 AI Sales Intelligence")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "🤖 Lead Prediction",
        "📊 Sales Analytics",
        "📁 Batch Prediction",
        "🧠 Model Information"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    **AI Sales Lead Prediction System**

    Predict conversion probability and help
    sales teams prioritize valuable leads.
    """
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎯 AI Sales Lead Prediction & Analytics System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Machine Learning Powered Sales Intelligence Platform</div>',
    unsafe_allow_html=True
)


# ============================================================
# PAGE 1: DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.header("Sales Performance Overview")

    total_leads = len(df)
    converted_leads = df["converted"].sum()
    conversion_rate = (
        converted_leads / total_leads
    ) * 100

    average_budget = df["budget_inr"].mean()

    avg_followups = df["followup_count"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Leads",
        f"{total_leads:,}"
    )

    col2.metric(
        "Converted Leads",
        f"{converted_leads:,}"
    )

    col3.metric(
        "Conversion Rate",
        f"{conversion_rate:.2f}%"
    )

    col4.metric(
        "Average Budget",
        f"₹{average_budget:,.0f}"
    )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        st.subheader("Conversion by Industry")

        industry_data = (
            df.groupby("industry")["converted"]
            .mean()
            .reset_index()
        )

        industry_data["conversion_rate"] = (
            industry_data["converted"] * 100
        )

        industry_data = industry_data.sort_values(
            "conversion_rate",
            ascending=False
        )

        fig = px.bar(
            industry_data,
            x="industry",
            y="conversion_rate",
            title="Conversion Rate by Industry",
            labels={
                "conversion_rate": "Conversion Rate (%)",
                "industry": "Industry"
            }
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        st.subheader("Lead Source Performance")

        source_data = (
            df.groupby("lead_source")["converted"]
            .mean()
            .reset_index()
        )

        source_data["conversion_rate"] = (
            source_data["converted"] * 100
        )

        fig = px.pie(
            source_data,
            names="lead_source",
            values="conversion_rate",
            title="Lead Source Conversion Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("Budget Distribution")

    fig = px.histogram(
        df,
        x="budget_inr",
        color="converted",
        nbins=30,
        title="Budget Distribution by Conversion Status",
        labels={
            "budget_inr": "Budget (INR)",
            "converted": "Converted"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Follow-up Activity")

    followup_data = (
        df.groupby("followup_count")["converted"]
        .mean()
        .reset_index()
    )

    followup_data["conversion_rate"] = (
        followup_data["converted"] * 100
    )

    fig = px.line(
        followup_data,
        x="followup_count",
        y="conversion_rate",
        markers=True,
        title="Conversion Rate vs Follow-up Count",
        labels={
            "followup_count": "Number of Follow-ups",
            "conversion_rate": "Conversion Rate (%)"
        }
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# PAGE 2: INDIVIDUAL LEAD PREDICTION
# ============================================================

elif page == "🤖 Lead Prediction":

    st.header("AI Lead Conversion Prediction")

    st.write(
        "Enter lead information below to predict the probability "
        "of conversion and determine the recommended sales priority."
    )

    col1, col2 = st.columns(2)

    with col1:

        industry = st.selectbox(
            "Industry",
            sorted(df["industry"].dropna().unique())
        )

        service = st.selectbox(
            "Service Required",
            sorted(df["service"].dropna().unique())
        )

        budget_inr = st.number_input(
            "Budget (INR)",
            min_value=0.0,
            value=100000.0,
            step=10000.0
        )

    with col2:

        lead_source = st.selectbox(
            "Lead Source",
            sorted(df["lead_source"].dropna().unique())
        )

        first_response_hours = st.number_input(
            "First Response Time (Hours)",
            min_value=0.0,
            value=2.0,
            step=0.5
        )

        followup_count = st.number_input(
            "Follow-up Count",
            min_value=0,
            value=3,
            step=1
        )

    st.markdown("---")

    if st.button(
        "🔮 Predict Lead Conversion",
        use_container_width=True
    ):

        try:

            input_data = pd.DataFrame(
                [{
                    "industry": industry,
                    "service": service,
                    "lead_source": lead_source,
                    "budget_inr": budget_inr,
                    "first_response_hours": first_response_hours,
                    "followup_count": followup_count
                }]
            )

            probability = float(
                model.predict_proba(
                    input_data[FEATURES]
                )[:, 1][0]
            )

            prediction = int(
                probability >= 0.50
            )

            priority, priority_text = get_priority(
                probability
            )

            recommendation = get_recommendation(
                probability,
                priority
            )

            logger.info(
                "Lead prediction generated. Probability=%.4f Priority=%s",
                probability,
                priority
            )

            st.success(
                "Prediction completed successfully!"
            )

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric(
                "Conversion Probability",
                f"{probability * 100:.2f}%"
            )

            metric2.metric(
                "Prediction",
                "Likely to Convert"
                if prediction == 1
                else "Unlikely to Convert"
            )

            metric3.metric(
                "Sales Priority",
                priority
            )

            st.markdown("### AI Sales Recommendation")

            if priority == "HIGH":

                st.markdown(
                    f'<div class="high-priority">{priority_text}</div>',
                    unsafe_allow_html=True
                )

            elif priority == "MEDIUM":

                st.markdown(
                    f'<div class="medium-priority">{priority_text}</div>',
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    f'<div class="low-priority">{priority_text}</div>',
                    unsafe_allow_html=True
                )

            st.info(recommendation)

            fig = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=probability * 100,
                    title={
                        "text": "Conversion Probability"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        }
                    }
                )
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        except Exception as error:

            logger.exception(
                "Prediction failed."
            )

            st.error(
                f"Prediction failed: {error}"
            )


# ============================================================
# PAGE 3: SALES ANALYTICS
# ============================================================

elif page == "📊 Sales Analytics":

    st.header("Advanced Sales Analytics")

    tab1, tab2, tab3 = st.tabs(
        [
            "Industry Analysis",
            "Lead Source Analysis",
            "Sales Behaviour"
        ]
    )

    with tab1:

        industry_analysis = (
            df.groupby("industry")
            .agg(
                total_leads=("lead_id", "count"),
                conversions=("converted", "sum"),
                conversion_rate=("converted", "mean"),
                average_budget=("budget_inr", "mean")
            )
            .reset_index()
        )

        industry_analysis[
            "conversion_rate"
        ] *= 100

        st.dataframe(
            industry_analysis,
            use_container_width=True
        )

        fig = px.scatter(
            industry_analysis,
            x="average_budget",
            y="conversion_rate",
            size="total_leads",
            hover_name="industry",
            title="Industry Budget vs Conversion Rate"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with tab2:

        source_analysis = (
            df.groupby("lead_source")
            .agg(
                total_leads=("lead_id", "count"),
                conversions=("converted", "sum"),
                conversion_rate=("converted", "mean")
            )
            .reset_index()
        )

        source_analysis[
            "conversion_rate"
        ] *= 100

        st.dataframe(
            source_analysis,
            use_container_width=True
        )

        fig = px.bar(
            source_analysis,
            x="lead_source",
            y="conversion_rate",
            title="Lead Source Conversion Performance"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with tab3:

        response_analysis = (
            df.groupby("converted")[
                "first_response_hours"
            ]
            .mean()
            .reset_index()
        )

        response_analysis["converted"] = (
            response_analysis["converted"]
            .map({
                0: "Not Converted",
                1: "Converted"
            })
        )

        fig = px.bar(
            response_analysis,
            x="converted",
            y="first_response_hours",
            title="Average First Response Time"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# ============================================================
# PAGE 4: BATCH PREDICTION
# ============================================================

elif page == "📁 Batch Prediction":

    st.header("Batch Lead Prediction")

    st.write(
        "Upload a CSV file containing multiple leads "
        "to generate conversion probabilities and sales priorities."
    )

    required_columns = FEATURES

    st.info(
        "Required columns: "
        + ", ".join(required_columns)
    )

    uploaded_file = st.file_uploader(
        "Upload Lead CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            batch_df = pd.read_csv(
                uploaded_file
            )

            missing_columns = (
                set(required_columns)
                - set(batch_df.columns)
            )

            if missing_columns:

                st.error(
                    "Missing required columns: "
                    + ", ".join(
                        sorted(missing_columns)
                    )
                )

            else:

                probabilities = (
                    model.predict_proba(
                        batch_df[FEATURES]
                    )[:, 1]
                )

                results_df = batch_df.copy()

                results_df[
                    "conversion_probability"
                ] = probabilities

                results_df[
                    "conversion_percentage"
                ] = (
                    probabilities * 100
                )

                results_df[
                    "predicted_conversion"
                ] = (
                    probabilities >= 0.50
                ).astype(int)

                results_df[
                    "lead_priority"
                ] = (
                    results_df[
                        "conversion_probability"
                    ]
                    .apply(
                        lambda x: get_priority(x)[0]
                    )
                )

                results_df = (
                    results_df.sort_values(
                        "conversion_probability",
                        ascending=False
                    )
                )

                st.success(
                    "Batch prediction completed!"
                )

                st.dataframe(
                    results_df,
                    use_container_width=True
                )

                csv_data = (
                    results_df
                    .to_csv(index=False)
                    .encode("utf-8")
                )

                st.download_button(
                    label="⬇️ Download Prediction Results",
                    data=csv_data,
                    file_name=(
                        "lead_predictions_"
                        + datetime.now().strftime(
                            "%Y%m%d_%H%M%S"
                        )
                        + ".csv"
                    ),
                    mime="text/csv",
                    use_container_width=True
                )

                logger.info(
                    "Batch prediction completed for %d leads.",
                    len(results_df)
                )

        except Exception as error:

            logger.exception(
                "Batch prediction failed."
            )

            st.error(
                f"Batch prediction failed: {error}"
            )


# ============================================================
# PAGE 5: MODEL INFORMATION
# ============================================================

elif page == "🧠 Model Information":

    st.header("Machine Learning Model Information")

    model_name = model_artifact.get(
        "model_name",
        "Unknown"
    )

    metrics = model_artifact.get(
        "metrics",
        {}
    )

    st.subheader("Selected Model")

    st.success(
        f"🏆 {model_name}"
    )

    st.subheader("Model Performance")

    if metrics:

        metric_cols = st.columns(
            len(metrics)
        )

        for index, (
            metric_name,
            metric_value
        ) in enumerate(metrics.items()):

            metric_cols[index].metric(
                metric_name.replace(
                    "_",
                    " "
                ).title(),
                f"{metric_value:.4f}"
            )

    else:

        st.warning(
            "Model metrics are not available."
        )

    st.subheader("Input Features")

    feature_df = pd.DataFrame(
        {
            "Feature": FEATURES,
            "Description": [
                "Business industry",
                "Service requested",
                "Source of the lead",
                "Available budget",
                "Time taken for first response",
                "Number of sales follow-ups"
            ]
        }
    )

    st.dataframe(
        feature_df,
        use_container_width=True
    )

    st.subheader("Data Leakage Prevention")

    st.info(
        """
        The feature `days_to_conversion` is excluded from prediction.

        This information may only be known after a successful
        conversion and including it would cause data leakage.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "AI Sales Lead Prediction & Analytics System | "
    "JZD Technologies Assignment | "
    "Machine Learning Powered Decision Support"
)
