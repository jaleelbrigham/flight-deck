import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Flight Deck",
    page_icon="✈️",
    layout="wide"
)

@st.cache_data
def load_data():
    """Load the airline dataset."""
    return pd.read_csv("T_ONTIME_REPORTING.csv")


# Load flight data
flight_df = load_data()

# Airline filter
carrier_options = sorted(flight_df["OP_UNIQUE_CARRIER"].dropna().unique())

selected_carriers = st.sidebar.multiselect(
    "select airlines",
    carrier_options,
    default=carrier_options
)

st.sidebar.write("Selected airlines:", selected_carriers)

# Apply selected airline filters
filtered_df = flight_df[
    flight_df["OP_UNIQUE_CARRIER"].isin(selected_carriers)
]

# Baseline metrics
TOTAL_FLIGHTS = filtered_df.shape[0]
LATE_DEPARTURES = filtered_df[filtered_df["DEP_DELAY"] > 0].shape[0]
DELAY_RATE = (LATE_DEPARTURES / TOTAL_FLIGHTS) * 100 if TOTAL_FLIGHTS > 0 else 0

# Dashboard title
st.title("flight deck 🌴")

st.caption(
    "an interactive airline delay dashboard built from historical flight data"
)

# Metric cards
metric_col_1, metric_col_2, metric_col_3 = st.columns(3)

metric_col_1.metric("total flights", f"{TOTAL_FLIGHTS:,}")
metric_col_2.metric("late departures", f"{LATE_DEPARTURES:,}")
metric_col_3.metric("delay rate", f"{DELAY_RATE:.2f}%")

st.divider()

st.subheader("sample flight data")
st.write(
    "a quick look at the flight records powering the dashboard."
)

st.dataframe(
    filtered_df.sample(min(100, TOTAL_FLIGHTS), random_state=42),
    width="stretch"
)

