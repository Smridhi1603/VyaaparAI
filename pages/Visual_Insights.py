import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Define the send_email function before calling it
def send_email(subject, body, to_email):
    from_email = st.secrets["general"]["email_user"]
    from_password = st.secrets["general"]["email_password"]

    # Set up the MIME structure for the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the email body to the email message
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use 'smtp.gmail.com' for Gmail
        server.starttls()  # Enable security
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()

        return True  # Indicate that the email was sent successfully
    except Exception as e:
        print(f"Error: {e}")
        return False  # Indicate that there was an error

# Load the data
data = pd.read_excel('pages/cosmetic_bodycare_haircare_dataset.xlsx')

# Convert the 'Month' column to datetime
data['Month'] = pd.to_datetime(data['Month'])

# Define the months list
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Streamlit selectors for month and product
selected_month = st.selectbox("Select Month", months_list)
selected_product = st.selectbox("Select Product", data['Product Name'].unique())

# Filter the data for the selected product
monthly_data = data[data['Product Name'] == selected_product]

# Filter data for the selected month
monthly_data['Month_str'] = monthly_data['Month'].dt.strftime('%B')
monthly_data = monthly_data[monthly_data['Month_str'] == selected_month]

# Check if data is available for the selected product and month
if not monthly_data.empty:
    # Calculate total sales and stock for the selected month and product
    total_month_stock = monthly_data['Monthly_Stock'].sum()
    total_sales = monthly_data['Monthly_Sales'].sum()

    # Prepare data for Prophet model
    df = monthly_data[['Month', 'Monthly_Sales']].rename(columns={'Month': 'ds', 'Monthly_Sales': 'y'})

    # Fit the Prophet model
    model = Prophet()
    model.fit(df)

    # Make future predictions
    future = model.make_future_dataframe(periods=1, freq='M')
    forecast = model.predict(future)

    # Get the predicted value for the next month
    predicted_value = forecast['yhat'].iloc[-1]

    # Check if forecasted demand exceeds current stock
    if predicted_value > total_month_stock:
        st.warning(f"Warning: Forecasted demand ({predicted_value:.2f}) exceeds current stock ({total_month_stock}). Please reorder stock!")
        
        # Send email and check if it's sent successfully
        if send_email("Stock Reorder Alert", 
                      f"Your forecasted demand for {selected_product} in {selected_month} exceeds your current stock. Forecasted demand: {predicted_value:.2f}, Current stock: {total_month_stock}. Please reorder stock.", 
                      "smridhi3943.beai23@chitkara.edu.in"):  # Replace with the recipient's email
            st.success("Reorder alert email has been sent successfully.")
        else:
            st.error("Failed to send reorder alert email.")

    else:
        st.success("Stock levels are adequate for forecasted demand.")
        
        # Send email and check if it's sent successfully
        if send_email("Stock Adequacy Alert", 
                      f"Your stock levels are adequate for {selected_product} in {selected_month}. Forecasted demand: {predicted_value:.2f}, Current stock: {total_month_stock}.", 
                      "smridhi1603@gmail.com"):  # Replace with the recipient's email
            st.success("Stock adequacy email has been sent successfully.")
        else:
            st.error("Failed to send stock adequacy email.")

    # Pie Chart to show sales vs stock distribution
    st.subheader(f"Sales vs. Stock for {selected_product} in {selected_month}")
    fig_pie = go.Figure()
    fig_pie.add_trace(go.Pie(labels=['Total Sales', 'Total Stock'], 
                             values=[total_sales, total_month_stock], 
                             name='Sales and Stock', 
                             marker=dict(colors=['orange', 'brown'])))
    fig_pie.update_layout(title='Sales and Stock Distribution')
    st.plotly_chart(fig_pie)

    # Bar Plot for Sales vs Stock
    fig_bar = go.Figure()
    fig_bar.add_trace(go.Bar(x=['Sales', 'Stock'], 
                             y=[total_sales, total_month_stock], 
                             marker_color=['orange', 'brown']))
    fig_bar.update_layout(title='Sales vs Stock', xaxis_title='Category', yaxis_title='Amount')
    st.plotly_chart(fig_bar)

    # Line Plot for Sales vs Stock Trend
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=['Sales', 'Stock'], 
                                  y=[total_sales, total_month_stock], 
                                  mode='lines+markers', 
                                  name='Sales & Stock', 
                                  line=dict(shape='linear', color='brown')))
    fig_line.update_layout(title='Sales vs Stock Trend', xaxis_title='Category', yaxis_title='Amount')
    st.plotly_chart(fig_line)

else:
    st.error(f"No data available for {selected_product} in {selected_month}.")
