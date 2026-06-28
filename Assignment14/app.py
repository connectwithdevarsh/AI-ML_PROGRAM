import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import model
import graphs
import train_model

raw_df = pd.read_csv("Order_dataset - Sheet1.csv")

selected = option_menu(
    menu_title="Main Menu",
    options=["Home", "Dataset", "Prediction"],
    icons=["house", "database", "graph-up"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    st.title("Food Order Status Predictor")
    
    total_orders = len(raw_df)
    delivered_pct = (raw_df['order_status'] == 'Delivered').mean() * 100
    cancelled_pct = (raw_df['order_status'] == 'Cancelled').mean() * 100
    avg_order_value = raw_df['order_value'].mean()
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Orders", f"{total_orders}")
    col2.metric("Delivered %", f"{delivered_pct:.2f}%")
    col3.metric("Cancelled %", f"{cancelled_pct:.2f}%")
    col4.metric("Average Order Value", f"Rs. {avg_order_value:.2f}")
    
    st.subheader("Order Status Distribution")
    fig1 = graphs.plot_order_status(raw_df)
    st.pyplot(fig1)
    
    st.subheader("Top Food Categories")
    fig2 = graphs.plot_food_categories(raw_df)
    st.pyplot(fig2)

elif selected == "Dataset":
    st.title("Order Dataset Page")
    
    st.subheader("Dataset Shape")
    st.write(f"Rows: {raw_df.shape[0]}, Columns: {raw_df.shape[1]}")
    
    st.subheader("Dataset Summary")
    st.write(raw_df.describe())
    
    st.subheader("Complete Dataset")
    st.dataframe(raw_df)

elif selected == "Prediction":
    st.title("Prediction and Model Performance")
    
    st.subheader("Model Performance")
    st.write(f"**Accuracy Score:** {train_model.acc:.4f}")
    
    st.write("**Confusion Matrix:**")
    st.write(train_model.cm)
    
    st.subheader("Feature Importance")
    fig3 = graphs.plot_feature_importance(model.model, model.X.columns)
    st.pyplot(fig3)
    
    st.subheader("Predict Custom Order Status")
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            month = st.selectbox("Month", model.encoders['month'].classes_)
            day_of_week = st.selectbox("Day of Week", model.encoders['day_of_week'].classes_)
            food_category = st.selectbox("Food Category", model.encoders['food_category'].classes_)
            order_platform = st.selectbox("Order Platform", model.encoders['order_platform'].classes_)
            payment_method = st.selectbox("Payment Method", model.encoders['payment_method'].classes_)
            time_slot = st.selectbox("Time Slot", model.encoders['time_slot'].classes_)
            weather_condition = st.selectbox("Weather Condition", model.encoders['weather_condition'].classes_)
            kitchen_load = st.selectbox("Kitchen Load", model.encoders['kitchen_load'].classes_)
            
        with col2:
            items_ordered = st.number_input("Items Ordered", min_value=1, max_value=20, value=3)
            order_value = st.number_input("Order Value", min_value=10.0, max_value=10000.0, value=500.0)
            discount_percent = st.number_input("Discount Percent", min_value=0, max_value=100, value=10)
            prep_time_mins = st.number_input("Prep Time (Mins)", min_value=1, max_value=180, value=20)
            delivery_time_mins = st.number_input("Delivery Time (Mins)", min_value=1, max_value=180, value=30)
            is_repeat_customer = st.selectbox("Is Repeat Customer", [0, 1])
            distance_km = st.number_input("Distance (KM)", min_value=0.1, max_value=100.0, value=5.0)
            driver_rating = st.number_input("Driver Rating", min_value=1.0, max_value=5.0, value=4.0)
            customer_complaint_history = st.number_input("Customer Complaint History", min_value=0, max_value=20, value=0)
            payment_failed_attempt = st.number_input("Payment Failed Attempts", min_value=0, max_value=10, value=0)
            promo_code_used = st.selectbox("Promo Code Used", [0, 1])
            
        submitted = st.form_submit_button("Predict")
        if submitted:
            input_dict = {
                'month': month,
                'day_of_week': day_of_week,
                'food_category': food_category,
                'order_platform': order_platform,
                'payment_method': payment_method,
                'time_slot': time_slot,
                'items_ordered': items_ordered,
                'order_value': order_value,
                'discount_percent': discount_percent,
                'prep_time_mins': prep_time_mins,
                'delivery_time_mins': delivery_time_mins,
                'is_repeat_customer': is_repeat_customer,
                'distance_km': distance_km,
                'driver_rating': driver_rating,
                'weather_condition': weather_condition,
                'kitchen_load': kitchen_load,
                'customer_complaint_history': customer_complaint_history,
                'payment_failed_attempt': payment_failed_attempt,
                'promo_code_used': promo_code_used
            }
            res = model.predict_status(input_dict)
            st.success(f"Predicted Order Status: {res}")
