# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_order_status(df):
    fig, ax = plt.subplots()
    counts = df['order_status'].value_counts()
    ax.bar(counts.index, counts.values, color=['green', 'red', 'orange'])
    ax.set_title("Order Status Distribution")
    ax.set_xlabel("Status")
    ax.set_ylabel("Count")
    return fig

def plot_food_categories(df):
    fig, ax = plt.subplots()
    counts = df['food_category'].value_counts()
    ax.bar(counts.index, counts.values, color='skyblue')
    ax.set_title("Top Food Categories")
    ax.set_xlabel("Food Category")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

def plot_feature_importance(model, feature_names):
    importances = model.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    top_indices = indices[:5]
    top_features = [feature_names[i] for i in top_indices]
    top_importances = importances[top_indices]
    
    fig, ax = plt.subplots()
    ax.barh(top_features[::-1], top_importances[::-1], color='purple')
    ax.set_title("Top 5 Feature Importances")
    ax.set_xlabel("Importance")
    plt.tight_layout()
    return fig
