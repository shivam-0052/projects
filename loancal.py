import streamlit as st

# Function to calculate the monthly payment
def calculate_monthly_payment(principal, annual_rate, years):
    # Convert annual rate percentage to a decimal and then to a monthly rate
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12
    if monthly_rate == 0:  # Handle zero interest rate
        return principal / num_payments
    else:
        # Formula to calculate monthly payment
        return principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

# Streamlit UI components
st.title("Simple Loan Calculator")

# Input fields
principal = st.number_input("Principal Amount ($)", min_value=0.0, format="%.2f")
annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, format="%.2f")
years = st.number_input("Number of Years", min_value=1, max_value=100)

# Calculate button
if st.button("Calculate Payment"):
    if principal > 0 and annual_rate > 0 and years > 0:
        monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
        st.write(f"Monthly Payment: ${monthly_payment:.2f}")
    else:
        st.write("Please enter valid values for all fields.")