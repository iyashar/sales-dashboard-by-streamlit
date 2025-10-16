import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_full_sample_data():
    np.random.seed(42)
    
    # ایجاد تاریخ‌های نمونه برای یک سال کامل
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')
    
    # ایجاد دیتای فروش
    data = []
    categories = ['Electronics', 'Clothing', 'Books', 'Home & Kitchen', 'Sports']
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    # ایجاد الگوهای فصلی برای مناطق مختلف
    regional_patterns = {
        'North': {'peak': 12, 'amplitude': 0.4},  # اوج در دسامبر
        'South': {'peak': 6, 'amplitude': 0.3},   # اوج در ژوئن
        'East': {'peak': 3, 'amplitude': 0.35},   # اوج در مارس
        'West': {'peak': 9, 'amplitude': 0.5},    # اوج در سپتامبر
        'Central': {'peak': 0, 'amplitude': 0.25} # الگوی یکنواخت‌تر
    }
    
    for date in dates:
        for category in categories:
            for region in regions:
                # فروش پایه با توجه به دسته‌بندی
                base_sales = {
                    'Electronics': np.random.randint(80, 250),
                    'Clothing': np.random.randint(60, 180),
                    'Books': np.random.randint(40, 120),
                    'Home & Kitchen': np.random.randint(70, 200),
                    'Sports': np.random.randint(90, 220)
                }[category]
                
                # الگوی فصلی کلی
                seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * date.dayofyear / 365)
                
                # الگوی منطقه‌ای
                regional_pattern = regional_patterns[region]
                regional_factor = 1 + regional_pattern['amplitude'] * np.sin(
                    2 * np.pi * (date.month - regional_pattern['peak']) / 12
                )
                
                # اثر آخر هفته
                weekend_factor = 1.5 if date.weekday() >= 4 else 1
                
                # اثر تعطیلات (تقریبی)
                holiday_factor = 1.8 if date.month == 12 and date.day in range(20, 27) else 1
                
                sales = int(base_sales * seasonal_factor * regional_factor * weekend_factor * holiday_factor)
                revenue = sales * np.random.uniform(50, 500)
                
                data.append({
                    'date': date,
                    'category': category,
                    'region': region,
                    'sales': sales,
                    'revenue': revenue,
                    'month': date.strftime('%Y-%m'),
                    'quarter': f'Q{((date.month-1)//3)+1}-{date.year}'
                })
    
    df = pd.DataFrame(data)
    return df

# ایجاد و ذخیره دیتا
if __name__ == "__main__":
    print("Generating enhanced sample sales data with regional patterns...")
    df = generate_full_sample_data()
    
    # ذخیره در فایل CSV
    df.to_csv('data/sales_data.csv', index=False)
    print(f"Data saved to 'data/sales_data.csv'")
    print(f"Total records: {len(df):,}")
    print(f"Date range: {df['date'].min()} to {df['date'].max()}")
    print(f"Categories: {', '.join(df['category'].unique())}")
    print(f"Regions: {', '.join(df['region'].unique())}")
    
    # نمایش الگوهای منطقه‌ای
    monthly_regional = df.groupby(['month', 'region'])['sales'].sum().unstack()
    print("\nRegional sales patterns (top months for each region):")
    for region in monthly_regional.columns:
        top_month = monthly_regional[region].idxmax()
        print(f"{region}: Peak in {top_month} with {monthly_regional[region][top_month]:,} sales")