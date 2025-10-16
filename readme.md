# Sales Analysis Dashboard / داشبورد تحلیل فروش

---

## 🇺🇸 English Version

### 📊 Overview
A comprehensive, interactive sales analysis dashboard built with Streamlit. This platform provides advanced sales analytics, temporal pattern identification, and regional performance comparison capabilities.

### ✨ Key Features

#### 📈 Core Analytics
- **Performance Metrics**: Display key sales and revenue indicators
- **Time Trends**: Monthly and seasonal sales analysis
- **Category Analysis**: Product performance comparison

#### 🗺️ Advanced Regional Analysis
- **Sales Heatmap**: Sales patterns by days of week and months
- **Regional Performance**: Cross-region comparison over time
- **Regional Champions**: Top-performing regions by month
- **Regional Heatmap**: Visual performance analysis across regions

#### 🔍 Interactive Capabilities
- **Dynamic Filters**: Filter by time, category, and region
- **Responsive Charts**: Full chart interactivity
- **Data Download**: Export filtered data
- **Multi-language**: Persian and English support

### 🚀 Quick Start

#### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

#### Method 1: Quick Setup
```bash
# Clone repository
git clone https://github.com/your-username/sales-dashboard.git
cd sales-dashboard

# Install dependencies
pip install -r requirements.txt

# Generate sample data
python generate_sample_data.py

# Launch dashboard
streamlit run app.py
```

#### Method 2: Using Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Generate data
python generate_sample_data.py

# Run application
streamlit run app.py
```

### 📁 Project Structure
```
sales-dashboard/
├── app.py                    # Main dashboard application
├── generate_sample_data.py   # Sample data generator
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── setup.sh                 # Setup script (optional)
├── .gitignore               # Git ignore file
└── data/
    └── sales_data.csv       # Sales data (auto-generated)
```

### 🛠️ Technology Stack
| Technology | Version | Purpose |
|------------|---------|---------|
| **Streamlit** | 1.28+ | Web application framework |
| **Pandas** | 2.0+ | Data processing & analysis |
| **Plotly** | 5.15+ | Interactive visualizations |
| **NumPy** | 1.24+ | Numerical computations |

### 📊 Sample Data
Automatically generated sample data includes:

#### Data Structure
```python
{
    'date': '2023-01-01',        # Sales date
    'category': 'Electronics',   # Product category
    'region': 'North',          # Sales region
    'sales': 142,               # Sales quantity
    'revenue': 35682.15,        # Revenue (USD)
    'month': '2023-01',         # Month (for grouping)
    'quarter': 'Q1-2023'        # Quarter (seasonal analysis)
}
```

#### Data Patterns
- **One-year data**: January to December 2023
- **5 product categories**: Electronics, Clothing, Books, Home & Kitchen, Sports
- **5 sales regions**: North, South, East, West, Central
- **Seasonal patterns**: Regional and seasonal variations

### 🎯 Usage Guide

#### Main Dashboard Sections
1. **Filters (Sidebar)**
   - Date range selection
   - Product categories
   - Sales regions

2. **Key Metrics**
   - Total sales count
   - Total revenue
   - Average sale value
   - Daily average sales

3. **Analytical Charts**
   - Monthly sales trends
   - Revenue by category
   - Regional sales distribution

4. **Advanced Analysis**
   - Sales heatmap (Days vs Months)
   - Regional performance
   - Monthly regional champions

#### Usage Tips
- Use filters to focus on specific data subsets
- Hover over charts for detailed information
- Use download button to export filtered data
- Charts update in real-time with filter changes

### 🔧 Customization & Development

#### Adding New Data Source
```python
# Modify load_data function in app.py
def load_data():
    # For real data:
    df = pd.read_csv('path/to/your/data.csv')
    # Or for database connection:
    # df = pd.read_sql('SELECT * FROM sales', connection)
    return df
```

#### Adding New Visualizations
```python
# Add in relevant section of app.py
new_chart = px.bar(
    data_frame=filtered_df,
    x='category',
    y='sales',
    title='New Chart'
)
st.plotly_chart(new_chart)
```

### 🤝 Contributing
We welcome contributions! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Create a Pull Request

#### Git Commands for Contributors
```bash
# Fork and clone repository
git clone https://github.com/iyashar/sales-dashboard-by-streamlit.git
cd sales-dashboard

# Create new branch
git checkout -b feature/new-analysis

# Add changes
git add .
git commit -m "Add new analysis feature"

# Push changes
git push origin feature/new-analysis
```

### 📝 Troubleshooting

#### Common Issues
1. **Package Errors**
   ```bash
   # Update pip
   pip install --upgrade pip
   
   # Reinstall packages
   pip install -r requirements.txt
   ```

2. **Data Not Loading**
   - Ensure `sales_data.csv` exists in `data` folder
   - Run `python generate_sample_data.py`

3. **Port Already in Use**
   ```bash
   # Use different port
   streamlit run app.py --server.port 8502
   ```

#### Debugging
```python
# For debugging, add to app.py
import logging
logging.basicConfig(level=logging.DEBUG)

# Or use st.write for debugging
st.write("Debug info:", filtered_df.shape)
```

### 📄 License
This project is licensed under the MIT License. See LICENSE file for details.

### 📞 Support
- **Issues**: For bug reports or feature requests
- **Discussions**: For questions and discussions
- **Email**: yashara@outlook.com

### 🔄 Changelog

#### Version 1.1 (Current)
- Added sales heatmaps
- Advanced regional analysis
- Multi-language support
- Data download capability

#### Future Roadmap
- [ ] Real database integration
- [ ] ML-based sales forecasting
- [ ] Administrative dashboard
- [ ] Automated reporting

---

## 🇮🇷 نسخه فارسی

### 📊 نمای کلی
یک داشبورد تحلیل فروش تعاملی و جامع ساخته شده با Streamlit. این پلتفرم امکان تحلیل پیشرفته فروش، شناسایی الگوهای زمانی و مقایسه عملکرد مناطق مختلف را فراهم می‌کند.

### ✨ ویژگی‌های اصلی

#### 📈 تحلیل‌های کلیدی
- **شاخص‌های عملکرد**: نمایش متریک‌های کلیدی فروش و درآمد
- **روندهای زمانی**: تحلیل فروش ماهانه و فصلی
- **تحلیل دسته‌بندی**: مقایسه عملکرد محصولات مختلف

#### 🗺️ تحلیل منطقه‌ای پیشرفته
- **هیت‌مپ فروش**: نمایش الگوهای فروش بر اساس روزهای هفته و ماه‌ها
- **عملکرد مناطق**: مقایسه مناطق مختلف در بازه‌های زمانی
- **برترین مناطق**: شناسایی منطقه برتر در هر ماه
- **هیت‌مپ منطقه‌ای**: تحلیل بصری عملکرد مناطق

#### 🔍 قابلیت‌های تعاملی
- **فیلترهای پویا**: فیلتر بر اساس زمان، دسته‌بندی و منطقه
- **نمودارهای واکنش‌گرا**: تعامل کامل با نمودارها
- **دانلود داده**: امکان دریافت داده‌های فیلتر شده
- **چندزبانه**: پشتیبانی از زبان فارسی و انگلیسی

### 🚀 راه‌اندازی سریع

#### پیش‌نیازها
- Python 3.8 یا بالاتر
- pip (مدیریت پکیج پایتون)

#### روش اول: نصب سریع
```bash
# کلون کردن ریپازیتوری
git clone https://github.com/iyashar/sales-dashboard-by-streamlit.git
cd sales-dashboard

# نصب وابستگی‌ها
pip install -r requirements.txt

# تولید داده‌های نمونه
python generate_sample_data.py

# اجرای داشبورد
streamlit run app.py
```

#### روش دوم: استفاده از محیط مجازی
```bash
# ایجاد محیط مجازی
python -m venv venv

# فعال‌سازی محیط مجازی
# در ویندوز:
venv\Scripts\activate
# در مک/لینوکس:
source venv/bin/activate

# نصب پکیج‌ها
pip install -r requirements.txt

# تولید داده‌ها
python generate_sample_data.py

# اجرای برنامه
streamlit run app.py
```

### 📁 ساختار پروژه
```
sales-dashboard/
├── app.py                    # کد اصلی داشبورد
├── generate_sample_data.py   # تولید داده‌های نمونه
├── requirements.txt          # لیست پکیج‌های مورد نیاز
├── README.md                # مستندات پروژه
├── setup.sh                 # اسکریپت راه‌اندازی (اختیاری)
├── .gitignore               # فایل‌های نادیده گرفته شده توسط Git
└── data/
    └── sales_data.csv       # داده‌های فروش (تولید خودکار)
```

### 🛠️ تکنولوژی‌های استفاده شده
| تکنولوژی | نسخه | کاربرد |
|----------|------|---------|
| **Streamlit** | 1.28+ | فریم‌ورک اصلی وب اپلیکیشن |
| **Pandas** | 2.0+ | پردازش و تحلیل داده‌ها |
| **Plotly** | 5.15+ | نمودارهای تعاملی |
| **NumPy** | 1.24+ | محاسبات عددی |

### 📊 نمونه داده‌ها
داده‌های استفاده شده در این داشبورد به صورت خودکار تولید می‌شوند و شامل:

#### ساختار داده‌ها
```python
{
    'date': '2023-01-01',        # تاریخ فروش
    'category': 'Electronics',   # دسته‌بندی محصول
    'region': 'North',          # منطقه فروش
    'sales': 142,               # تعداد فروش
    'revenue': 35682.15,        # درآمد (دلار)
    'month': '2023-01',         # ماه (برای گروه‌بندی)
    'quarter': 'Q1-2023'        # فصل (برای تحلیل فصلی)
}
```

#### الگوهای داده‌ها
- **داده‌های یکساله**: از ژانویه تا دسامبر 2023
- **5 دسته‌بندی محصول**: الکترونیک، پوشاک، کتاب، خانه و آشپزخانه، ورزشی
- **5 منطقه فروش**: شمال، جنوب، شرق، غرب، مرکز
- **الگوهای فصلی**: تغییرات فصلی و منطقه‌ای

### 🎯 راهنمای استفاده

#### بخش‌های اصلی داشبورد
1. **فیلترها (سایدبار)**
   - بازه زمانی
   - دسته‌بندی محصولات
   - مناطق فروش

2. **متریک‌های کلیدی**
   - تعداد کل فروش
   - درآمد کل
   - میانگین ارزش فروش
   - میانگین فروش روزانه

3. **نمودارهای تحلیلی**
   - روند فروش ماهانه
   - درآمد بر اساس دسته‌بندی
   - توزیع فروش منطقه‌ای

4. **تحلیل‌های پیشرفته**
   - هیت‌مپ فروش (روز vs ماه)
   - عملکرد منطقه‌ای
   - برترین مناطق هر ماه

#### نکات استفاده
- از فیلترها برای تمرکز بر داده‌های خاص استفاده کنید
- روی نمودارها هاور کنید تا اطلاعات دقیق‌تر ببینید
- از دکمه دانلود برای دریافت داده‌های فیلتر شده استفاده کنید
- نمودارها به صورت real-time با فیلترها به‌روز می‌شوند

### 🔧 توسعه و سفارشی‌سازی

#### اضافه کردن منبع داده جدید
```python
# در app.py، تابع load_data را تغییر دهید
def load_data():
    # برای داده‌های واقعی:
    df = pd.read_csv('path/to/your/data.csv')
    # یا برای اتصال به دیتابیس:
    # df = pd.read_sql('SELECT * FROM sales', connection)
    return df
```

#### اضافه کردن نمودار جدید
```python
# در بخش مربوطه از app.py اضافه کنید
new_chart = px.bar(
    data_frame=filtered_df,
    x='category',
    y='sales',
    title='نمودار جدید'
)
st.plotly_chart(new_chart)
```

### 🤝 مشارکت در توسعه
ما از مشارکت‌های شما استقبال می‌کنیم! برای مشارکت:

1. ریپازیتوری را Fork کنید
2. Branch جدید ایجاد کنید: `git checkout -b feature/amazing-feature`
3. تغییرات را Commit کنید: `git commit -m 'Add amazing feature'`
4. به Branch اصلی Push کنید: `git push origin feature/amazing-feature`
5. Pull Request ایجاد کنید

#### دستورات Git برای مشارکت‌کنندگان
```bash
# Fork ریپازیتوری و کلون کردن
git clone https://github.com/iyashar/sales-dashboard-by-streamlit.git
cd sales-dashboard

# ایجاد برنچ جدید
git checkout -b feature/new-analysis

# اضافه کردن تغییرات
git add .
git commit -m "Add new analysis feature"

# آپلود تغییرات
git push origin feature/new-analysis
```

### 📝 راهنمای عیب‌یابی

#### مشکلات رایج
1. **خطای پکیج‌ها**
   ```bash
   # آپدیت pip
   pip install --upgrade pip
   
   # نصب مجدد پکیج‌ها
   pip install -r requirements.txt
   ```

2. **داده‌ها لود نمی‌شوند**
   - مطمئن شوید فایل `sales_data.csv` در پوشه `data` وجود دارد
   - دستور `python generate_sample_data.py` را اجرا کنید

3. **پورت در حال استفاده است**
   ```bash
   # استفاده از پورت متفاوت
   streamlit run app.py --server.port 8502
   ```

#### دیباگینگ
```python
# برای دیباگ، در app.py اضافه کنید
import logging
logging.basicConfig(level=logging.DEBUG)

# یا از st.write برای دیباگ استفاده کنید
st.write("Debug info:", filtered_df.shape)
```

### 📄 لایسنس
این پروژه تحت لایسنس MIT منتشر شده است. برای جزئیات بیشتر فایل LICENSE را مطالعه کنید.

### 📞 پشتیبانی
- **ایسوها**: برای گزارش باگ یا پیشنهاد قابلیت جدید
- **دیسکاشن‌ها**: برای سوالات و بحث‌ها
- **ایمیل**: yashara@outlook.com

### 🔄 تاریخچه تغییرات

#### نسخه 1.1 (کنونی)
- اضافه شدن هیت‌مپ فروش
- تحلیل‌های منطقه‌ای پیشرفته
- پشتیبانی از زبان فارسی
- قابلیت دانلود داده‌ها

#### برنامه آینده
- [ ] اتصال به دیتابیس واقعی
- [ ] پیش‌بینی فروش با ML
- [ ] دشبورد مدیریتی
- [ ] گزارش‌های خودکار

---

<div dir="ltr" style="text-align: center;">

**Built with ❤️ using Streamlit**

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io)

</div>
