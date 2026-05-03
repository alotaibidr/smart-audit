import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="منصة المراجع الأكاديمي الذكي", page_icon="🎓", layout="wide")

# التنسيق البصري
st.markdown("""
    <style>
    .main { background-color: #f8faf9; }
    .criterion-card { 
        padding: 20px; border-radius: 12px; background-color: #ffffff; 
        border-right: 10px solid #006432; box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        direction: rtl; text-align: right; margin-bottom: 20px;
    }
    .evidence-item {
        background-color: #e6f0eb; padding: 10px; border-right: 4px solid #b8860b;
        margin-bottom: 8px; border-radius: 5px; font-size: 0.95em;
    }
    .section-title { color: #006432; border-bottom: 2px solid #b8860b; padding-bottom: 5px; text-align: right; }
    </style>
    """, unsafe_allow_html=True)

# الهيدر
st.markdown("<h1 style='text-align: center; color: #006432;'>منصة المراجع الأكاديمي الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #b8860b; font-size: 1.2em; font-weight: bold;'>دليل استيفاء شواهد الاعتماد الأكاديمي (NCAAA)</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>إعداد: د. علي بن محمد العتيبي</p>", unsafe_allow_html=True)
st.divider()

# قاعدة البيانات
criteria_guide = {
    "1-1-1: اتساق الرسالة": {
        "text": "تتسق رسالة البرنامج وأهدافه مع رسالة المؤسسة/الكلية وتوجه جميع عملياته وأنشطته.",
        "required_evidence": [
            "وثيقة رسالة البرنامج وأهدافه معتمدة.",
            "مصفوفة المواءمة بين رسالة البرنامج والكلية.",
            "محاضر اجتماعات اللجان لاعتماد الرسالة.",
            "تقارير قياس وعي المستفيدين بالرسالة."
        ],
        "tips": "يجب نشر الرسالة في موقع البرنامج والممرات الرسمية."
    },
    "1-1-2: الكوادر المؤهلة": {
        "text": "يتوفر لدى البرنامج العدد الكافي من الكوادر المؤهلة ولهم مهام وصلاحيات محددة.",
        "required_evidence": [
            "الهيكل التنظيمي المعتمد للبرنامج.",
            "أدلة الوصف الوظيفي لجميع المنسوبين.",
            "سجل السير الذاتية ومؤهلات الكوادر.",
            "قرارات التكليف الرسمية بالمهام."
        ],
        "tips": "تأكد من تحديث مصفوفة الصلاحيات سنوياً."
    },
    "1-1-3: المناخ التنظيمي": {
        "text": "يتوفر للبرنامج مناخ تنظيمي وبيئة أكاديمية داعمة.",
        "required_evidence": [
            "نتائج استطلاعات قياس الرضا الوظيفي.",
            "تقارير الفعاليات الأكاديمية والاجتماعية.",
            "سياسة معتمدة للحوافز والمكافآت.",
            "دليل إجراءات التظلم والشكاوى."
        ],
        "tips": "البيئة الداعمة تُقاس بوضوح المسارات والعدالة."
    }
}

# واجهة المستخدم
st.markdown("<h3 class='section-title'>تحديد المحك</h3>", unsafe_allow_html=True)
selected_c = st.selectbox("", list(criteria_guide.keys()))

current = criteria_guide[selected_c]

st.markdown(f"""
    <div class="criterion-card">
        <h2 class="section-title">وصف المحك:</h2>
        <p style='font-size: 1.1em;'>{current['text']}</p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 class='section-title'>📄 الشواهد المطلوبة:</h3>", unsafe_allow_html=True)
    for item in current['required_evidence']:
        st.markdown(f"<div class='evidence-item'>{item}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3 class='section-title'>💡 نصائح الجودة:</h3>", unsafe_allow_html=True)
    st.info(current['tips'])

st.divider()
st.markdown("<p style='text-align: center; font-size: 0.8em; color: gray;'>مبادرة د. علي العتيبي - 2026</p>", unsafe_allow_html=True)
