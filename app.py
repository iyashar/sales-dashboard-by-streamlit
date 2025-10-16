import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# تنظیمات صفحه
st.set_page_config(
    page_title="Sales Analysis Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# بارگذاری دیتا از فایل CSV
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/sales_data.csv')
        df['date'] = pd.to_datetime(df['date'])
        return df
    except FileNotFoundError:
        st.error("File 'data/sales_data.csv' not found. Please make sure the file exists.")
        return pd.DataFrame()

# بارگذاری دیتا
df = load_data()

if df.empty:
    st.stop()

# عنوان داشبورد
st.title('📊 Sales Analysis Dashboard')
st.markdown('---')

# سایدبار برای فیلترها
st.sidebar.header('Filters')

# فیلتر بازه زمانی
date_range = st.sidebar.date_input(
    "Date Range",
    value=(df['date'].min(), df['date'].max()),
    min_value=df['date'].min(),
    max_value=df['date'].max()
)

# فیلتر دسته‌بندی
categories = st.sidebar.multiselect(
    "Product Categories",
    options=df['category'].unique(),
    default=df['category'].unique()
)

# فیلتر منطقه
regions = st.sidebar.multiselect(
    "Sales Regions",
    options=df['region'].unique(),
    default=df['region'].unique()
)

# اعمال فیلترها
filtered_df = df[
    (df['date'].between(pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1]))) &
    (df['category'].isin(categories)) &
    (df['region'].isin(regions))
]

# متریک‌های کلی
st.subheader('📈 Key Performance Indicators')

col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = filtered_df['sales'].sum()
    st.metric("Total Sales", f"{total_sales:,}")

with col2:
    total_revenue = filtered_df['revenue'].sum()
    st.metric("Total Revenue", f"${total_revenue:,.0f}")

with col3:
    avg_sale_value = filtered_df['revenue'].sum() / filtered_df['sales'].sum() if filtered_df['sales'].sum() > 0 else 0
    st.metric("Average Sale Value", f"${avg_sale_value:.2f}")

with col4:
    unique_days = filtered_df['date'].nunique()
    daily_avg_sales = total_sales / unique_days if unique_days > 0 else 0
    st.metric("Daily Average Sales", f"{daily_avg_sales:.0f}")

st.markdown('---')

# ردیف اول نمودارها
col1, col2 = st.columns(2)

with col1:
    # نمودار فروش ماهانه
    monthly_sales = filtered_df.groupby('month').agg({
        'sales': 'sum',
        'revenue': 'sum'
    }).reset_index()
    
    fig_monthly = go.Figure()
    fig_monthly.add_trace(go.Scatter(
        x=monthly_sales['month'],
        y=monthly_sales['sales'],
        mode='lines+markers',
        name='Sales Count',
        line=dict(color='#1f77b4')
    ))
    
    fig_monthly.update_layout(
        title='Monthly Sales Trend',
        xaxis_title='Month',
        yaxis_title='Sales Count',
        template='plotly_white'
    )
    st.plotly_chart(fig_monthly, use_container_width=True)

with col2:
    # نمودار درآمد بر اساس دسته‌بندی
    category_revenue = filtered_df.groupby('category')['revenue'].sum().sort_values(ascending=True)
    
    fig_category = px.bar(
        x=category_revenue.values,
        y=category_revenue.index,
        orientation='h',
        title='Revenue by Category',
        labels={'x': 'Revenue', 'y': 'Category'}
    )
    fig_category.update_layout(template='plotly_white')
    st.plotly_chart(fig_category, use_container_width=True)

# ردیف دوم نمودارها - Heatmap و Regional Analysis
st.subheader('🗺️ Regional and Temporal Analysis')

col3, col4 = st.columns(2)

with col3:
    # Heatmap: فروش بر اساس روزهای هفته و ماه‌ها
    st.markdown("#### 📅 Sales Heatmap: Days vs Months")
    
    # آماده‌سازی دیتا برای heatmap
    heatmap_data = filtered_df.copy()
    heatmap_data['day_name'] = heatmap_data['date'].dt.day_name()
    heatmap_data['month_name'] = heatmap_data['date'].dt.month_name()
    
    # ترتیب روزهای هفته
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data['day_name'] = pd.Categorical(heatmap_data['day_name'], categories=days_order, ordered=True)
    
    # ترتیب ماه‌ها
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    heatmap_data['month_name'] = pd.Categorical(heatmap_data['month_name'], categories=months_order, ordered=True)
    
    # ایجاد pivot table برای heatmap
    heatmap_pivot = heatmap_data.pivot_table(
        values='sales',
        index='day_name',
        columns='month_name',
        aggfunc='sum',
        fill_value=0
    )
    
    # رسم heatmap
    fig_heatmap = px.imshow(
        heatmap_pivot,
        title='Sales Distribution: Days of Week vs Months',
        labels=dict(x="Month", y="Day of Week", color="Sales"),
        aspect="auto",
        color_continuous_scale='Blues'
    )
    fig_heatmap.update_layout(
        xaxis_title='Month',
        yaxis_title='Day of Week'
    )
    st.plotly_chart(fig_heatmap, use_container_width=True)

with col4:
    # Regional Performance by Month
    st.markdown("#### 🌍 Regional Performance by Month")
    
    regional_monthly = filtered_df.groupby(['month', 'region']).agg({
        'sales': 'sum',
        'revenue': 'sum'
    }).reset_index()
    
    # پیدا کردن برترین منطقه در هر ماه
    top_regions = regional_monthly.loc[regional_monthly.groupby('month')['sales'].idxmax()]
    
    fig_regional = px.bar(
        regional_monthly,
        x='month',
        y='sales',
        color='region',
        title='Sales by Region and Month',
        labels={'sales': 'Total Sales', 'month': 'Month', 'region': 'Region'},
        barmode='group'
    )
    
    # اضافه کردن annotation برای برترین منطقه‌ها
    for idx, row in top_regions.iterrows():
        fig_regional.add_annotation(
            x=row['month'],
            y=row['sales'],
            text="🏆",
            showarrow=False,
            font=dict(size=16),
            yshift=10
        )
    
    fig_regional.update_layout(template='plotly_white')
    st.plotly_chart(fig_regional, use_container_width=True)

# ردیف سوم نمودارها - تحلیل پیشرفته منطقه‌ای
col5, col6 = st.columns(2)

with col5:
    # Regional Champions - بهترین منطقه در هر ماه
    st.markdown("#### 🏆 Regional Champions by Month")
    
    # محاسبه سهم بازار هر منطقه در هر ماه
    monthly_totals = filtered_df.groupby('month')['sales'].sum().reset_index()
    monthly_totals.rename(columns={'sales': 'total_sales'}, inplace=True)
    
    regional_share = filtered_df.groupby(['month', 'region'])['sales'].sum().reset_index()
    regional_share = regional_share.merge(monthly_totals, on='month')
    regional_share['market_share'] = (regional_share['sales'] / regional_share['total_sales']) * 100
    
    # پیدا کردن برترین منطقه در هر ماه
    monthly_winners = regional_share.loc[regional_share.groupby('month')['sales'].idxmax()]
    
    fig_winners = px.scatter(
        monthly_winners,
        x='month',
        y='market_share',
        size='sales',
        color='region',
        title='Winning Regions by Month (Size = Sales Volume)',
        labels={'market_share': 'Market Share (%)', 'month': 'Month', 'region': 'Winning Region'},
        size_max=40
    )
    
    fig_winners.update_traces(
        marker=dict(line=dict(width=2, color='DarkSlateGrey'))
    )
    
    fig_winners.update_layout(template='plotly_white')
    st.plotly_chart(fig_winners, use_container_width=True)

with col6:
    # Regional Performance Heatmap
    st.markdown("#### 🔥 Regional Performance Heatmap")
    
    # آماده‌سازی دیتا برای heatmap منطقه‌ای
    regional_heatmap_data = filtered_df.pivot_table(
        values='sales',
        index='region',
        columns='month',
        aggfunc='sum',
        fill_value=0
    )
    
    fig_regional_heatmap = px.imshow(
        regional_heatmap_data,
        title='Regional Performance Heatmap by Month',
        labels=dict(x="Month", y="Region", color="Sales"),
        aspect="auto",
        color_continuous_scale='Viridis'
    )
    
    fig_regional_heatmap.update_layout(
        xaxis_title='Month',
        yaxis_title='Region'
    )
    st.plotly_chart(fig_regional_heatmap, use_container_width=True)

# ردیف چهارم - تحلیل جزئیات منطقه‌ای
st.subheader('📋 Regional Performance Details')

# جدول خلاصه عملکرد مناطق
regional_summary = filtered_df.groupby('region').agg({
    'sales': ['sum', 'mean'],
    'revenue': ['sum', 'mean'],
    'date': 'nunique'
}).round(2)

regional_summary.columns = ['Total Sales', 'Avg Daily Sales', 'Total Revenue', 'Avg Daily Revenue', 'Days Active']
regional_summary = regional_summary.sort_values('Total Sales', ascending=False)

st.dataframe(regional_summary, use_container_width=True)

# تحلیل جزئیات
st.subheader('🔍 Detailed Analysis')

# نمایش داده‌ها
st.dataframe(
    filtered_df.sort_values('date', ascending=False).head(100),
    use_container_width=True
)

# اطلاعات اضافی در سایدبار
st.sidebar.markdown('---')
st.sidebar.subheader('About Dashboard')
st.sidebar.info(
    """
    This dashboard is designed for comprehensive sales data analysis.
    
    **New Features:**
    - Sales heatmap (Days vs Months)
    - Regional performance analysis
    - Monthly regional champions
    - Regional performance heatmap
    """
)

# دانلود دیتا
st.sidebar.markdown('---')
st.sidebar.subheader('Download Data')
csv = filtered_df.to_csv(index=False)
st.sidebar.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

# پاورقی
st.markdown('---')
st.markdown(
    '<div style="text-align: center; color: gray;">'
    'Built with Streamlit | BY @IYASHAR'
    '</div>',
    unsafe_allow_html=True
)