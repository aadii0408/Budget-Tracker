import streamlit as st
import openai
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set your OpenAI API key
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# App title
st.title("SmartBudgeter: Budget Planner & Expense Tracker")

# User Inputs
st.header("Enter Your Financial Details")
income = st.number_input("Monthly Income ($):", min_value=0, step=100)
rent = st.number_input("Monthly Rent ($):", min_value=0, step=50)
groceries = st.number_input("Monthly Groceries ($):", min_value=0, step=50)
utilities = st.number_input(
    "Monthly Utilities (e.g., electricity, water) ($):", min_value=0, step=50
)
transportation = st.number_input("Monthly Transportation ($):", min_value=0, step=50)
entertainment = st.number_input("Monthly Entertainment ($):", min_value=0, step=50)
miscellaneous = st.number_input("Miscellaneous Expenses ($):", min_value=0, step=50)

# Goal Tracking
st.header("Set Your Savings Goal")
savings_goal = st.number_input("Monthly Savings Goal ($):", min_value=0, step=50)

# Generate Budget Plan
if st.button("Generate Budget Plan"):
    # Calculate total expenses
    total_expenses = (
        rent + groceries + utilities + transportation + entertainment + miscellaneous
    )
    remaining_income = income - total_expenses

    # Display Budget Summary
    st.subheader("Your Budget Summary")
    budget_summary = {
        "Total Income": income,
        "Total Expenses": total_expenses,
        "Remaining Income": remaining_income,
    }
    df_summary = pd.DataFrame(
        budget_summary.items(), columns=["Category", "Amount ($)"]
    )
    st.table(df_summary)

    # Show Expense Breakdown
    st.subheader("Expense Breakdown")
    expense_details = {
        "Rent": rent,
        "Groceries": groceries,
        "Utilities": utilities,
        "Transportation": transportation,
        "Entertainment": entertainment,
        "Miscellaneous": miscellaneous,
    }
    df_expenses = pd.DataFrame(
        expense_details.items(), columns=["Expense Category", "Amount ($)"]
    )
    st.table(df_expenses)

    # Graphs
    st.subheader("Visualize Your Budget")

    # Pie Chart
    st.write("**Expense Breakdown**")
    fig, ax = plt.subplots()
    ax.pie(
        expense_details.values(),
        labels=expense_details.keys(),
        autopct="%1.1f%%",
        startangle=90,
    )
    ax.axis("equal")
    st.pyplot(fig)

    # Bar Chart
    st.write("**Income vs Expenses**")
    fig, ax = plt.subplots()
    categories = ["Income", "Expenses"]
    values = [income, total_expenses]
    ax.bar(categories, values, color=["green", "red"])
    plt.ylabel("Amount ($)")
    st.pyplot(fig)

    # Goal Tracking
    st.subheader("Savings Goal Tracking")
    if savings_goal > 0:
        if remaining_income >= savings_goal:
            st.success(
                f"Great! You can meet your savings goal of ${savings_goal} this month!"
            )
        else:
            st.warning(
                f"You are ${savings_goal - remaining_income} short of your savings goal. Consider cutting back on non-essential expenses."
            )
    else:
        st.info("Set a savings goal to track your progress!")

    # Budget Fun Meter
    st.subheader("Your Budget Fun Meter")
    fun_score = entertainment / (total_expenses if total_expenses > 0 else 1) * 100
    if fun_score > 20:
        st.success(
            f"Your budget is fun-focused! 🎉 You're spending {fun_score:.1f}% on entertainment!"
        )
    elif fun_score > 10:
        st.warning(
            f"Your budget is balanced. A reasonable {fun_score:.1f}% of your expenses go to fun activities."
        )
    else:
        st.error(
            f"Your budget is too serious! 😬 Only {fun_score:.1f}% of your expenses go to fun activities. Treat yourself a little!"
        )

    # AI Tips for Savings
    st.subheader("Motivational AI Tips for Savings")
    prompt = (
        f"My monthly income is ${income}, and my expenses are:"
        f"\n- Rent: ${rent}"
        f"\n- Groceries: ${groceries}"
        f"\n- Utilities: ${utilities}"
        f"\n- Transportation: ${transportation}"
        f"\n- Entertainment: ${entertainment}"
        f"\n- Miscellaneous: ${miscellaneous}."
        f"\nHow can I save money while keeping my life balanced and fun?"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a financial assistant who gives motivational and fun advice.",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
        )
        ai_tips = response["choices"][0]["message"]["content"].strip()

        st.write(ai_tips)

    except Exception as e:
        st.error(f"Error generating AI suggestions: {str(e)}")
