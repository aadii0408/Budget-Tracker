# **SmartBudgeter: Budget Planner & Expense Tracker**

SmartBudgeter is a lightweight, user-friendly app that helps users manage their monthly finances effectively. With features like income and expense tracking, savings goal monitoring, and AI-generated financial tips, SmartBudgeter is the perfect tool to take control of your budget.

---

## **Features**

1. **Track Monthly Finances**:
   - Input monthly income and expenses across categories like rent, groceries, utilities, transportation, and entertainment.
   
2. **Savings Goal Setting**:
   - Set a monthly savings goal and track your progress.

3. **Expense Visualization**:
   - View detailed summaries of your expenses with interactive charts.

4. **AI-Generated Financial Tips**:
   - Get motivational savings tips and actionable advice to optimize your budget.

5. **Budget Fun Meter**:
   - Analyze your spending to determine whether your budget is fun-focused, balanced, or serious.

---

## **Technologies Used**

- **Python**: Core language for building the application.
- **Streamlit**: Web framework for creating an interactive app.
- **OpenAI API**: For generating financial tips and recommendations.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Visualizing expense data through charts.

---

## **Installation**

### **Requirements**
- Python 3.7 or higher
- Pip (Python package manager)

### **Setup Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/smartbudgeter.git
   cd smartbudgeter
   ```

2. **Install Dependencies**:
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your OpenAI API Key**:
   - Create a `.env` file in the project directory.
   - Add your OpenAI API key to the `.env` file:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key
     ```

4. **Run the Application**:
   Start the Streamlit app:
   ```bash
   streamlit run your_app.py
   ```

5. **Access the App**:
   Open the URL provided by Streamlit (default is `http://localhost:8501`).

---

## **How to Use**

1. **Enter Your Financial Details**:
   - Input your monthly income and expenses in the respective fields.
   - Categories include:
     - Rent
     - Groceries
     - Utilities
     - Transportation
     - Entertainment
     - Miscellaneous

2. **Set Your Savings Goal**:
   - Specify your desired monthly savings goal.
   - SmartBudgeter will calculate how close you are to achieving it.

3. **View Expense Summary**:
   - Check detailed tables showing your income, expenses, and remaining budget.
   - Use visual charts to analyze your spending.

4. **Get Financial Tips**:
   - Click the **Generate Financial Tips** button to receive AI-driven advice on optimizing your budget.

5. **Check Your Budget Fun Meter**:
   - See if your budget leans towards fun, balance, or seriousness based on your entertainment spending.

---

## **Screenshots**

### **1. Input Financial Details**
![Input Financial Details](https://via.placeholder.com/600x300?text=Input+Details+Screenshot)

### **2. View Budget Summary**
![Budget Summary](https://via.placeholder.com/600x300?text=Budget+Summary+Screenshot)

### **3. Expense Visualization**
![Expense Visualization](https://via.placeholder.com/600x300?text=Expense+Visualization+Screenshot)

---

## **Future Enhancements**
1. Add real-time notifications for budget updates.
2. Integrate with banking APIs for live transaction tracking.
3. Introduce community tips and forums for shared financial advice.
4. Expand charts with more advanced visualizations.

---

## **Contributing**

Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature/bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request on GitHub.

---
