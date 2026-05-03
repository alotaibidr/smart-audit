import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="منصة المراجع الأكاديمي الذكي", layout="wide", page_icon="🎓")

# تنسيق CSS مخصص للجمالية الأكاديمية
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #ffffff;
        border: 1px solid #dee2e6;
        border-radius: 5px 5px 0 0;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] { background-color: #007bff !important; color: white !important; }
    .criterion-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-right: 5px solid #007bff;
        margin-bottom: 15px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .essential { color: #d9534f; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.title("🎓 منصة المراجع الأكاديمي الذكي")
st.subheader("دليل الشواهد والأدلة لمعايير الاعتماد البرامجي (NCAAA)")
st.info("مبادرة د. علي بن محمد العتيبي - أتمتة خرائط الشواهد لضمان الجودة المؤسسية")

# تعريف البيانات والمعايير
data = {
    "المعيار 1: الإدارة والجودة": {
        "icon": "🏛️",
        "sub": "إدارة البرنامج وضمان جودته",
        "items": [
            {"id": "1-1-1", "text": "اتساق رسالة البرنامج وأهدافه مع رسالة المؤسسة.", "ess": False},
            {"id": "1-1-2", "text": "توفر الكوادر المؤهلة للمهام الإدارية والفنية.", "ess": True},
            {"id": "1-1-3", "text": "توفر مناخ تنظيمي وبيئة أكاديمية داعمة.", "ess": False},
            {"id": "1-1-4", "text": "متابعة تحقق الأهداف واتخاذ إجراءات التحسين.", "ess": False},
            {"id": "1-2-1", "text": "تطبيق نظام فاعل لضمان الجودة وإدارتها.", "ess": False},
            {"id": "1-2-2", "text": "تحليل مؤشرات الأداء الرئيسة وبيانات التقويم سنوياً.", "ess": True},
        ]
    },
    "المعيار 2: التعليم والتعلم": {
        "icon": "📖",
        "sub": "نواتج التعلم والمنهج الدراسي والتدريس",
        "items": [
            {"id": "2-1-1", "text": "تحديد نواتج التعلم واتساقها مع الرسالة.", "ess": False},
            {"id": "2-1-2", "text": "تطابق نواتج التعلم مع الإطار الوطني للمؤهلات وسوق العمل.", "ess": True},
            {"id": "2-2-1", "text": "مراعاة المنهج للتطورات العلمية والمهنية.", "ess": True},
            {"id": "2-3-1", "text": "التحقق من فعالية استراتيجيات التعليم والتقييم.", "ess": True},
            {"id": "2-3-7", "text": "ضبط النزاهة الأكاديمية وحماية الملكية الفكرية.", "ess": True},
        ]
    },
    "المعيار 3: الطلاب": {
        "icon": "👥",
        "sub": "القبول والخدمات والإرشاد",
        "items": [
            {"id": "3-0-1", "text": "تطبيق معايير عادلة للقبول والتسجيل والتخرج.", "ess": False},
            {"id": "3-0-3", "text": "توفر خدمات فعالة للإرشاد الأكاديمي والمهني والنفسي.", "ess": True},
            {"id": "3-0-6", "text": "تقويم كفاية وجودة الخدمات المقدمة للطلاب.", "ess": True},
        ]
    },
    "المعيار 4: هيئة التدريس": {
        "icon": "👨‍🏫",
        "sub": "العدد والكفاءة والتطوير",
        "items": [
            {"id": "4-0-1", "text": "توافر العدد الكافي من أعضاء هيئة التدريس.", "ess": True},
            {"id": "4-0-3", "text": "مشاركة هيئة التدريس في الأنشطة البحثية والإنتاج العلمي.", "ess": False},
            {"id": "4-0-5", "text": "تلقي أعضاء هيئة التدريس برامج التطوير المهني.", "ess": False},
        ]
    },
    "المعيار 5: المصادر والمرافق": {
        "icon": "🏗️",
        "sub": "مصادر التعلم والتجهيزات",
        "items": [
            {"id": "5-0-1", "text": "كفاية ومناسبة مصادر التعلم والخدمات المحدثة.", "ess": False},
            {"id": "5-0-3", "text": "تطبيق معايير السلامة والصحة المهنية في المرافق.", "ess": True},
        ]
    },
    "المعيار 6: البحث العلمي": {
        "icon": "🔬",
        "sub": "البحوث العلمية والمشاريع",
        "items": [
            {"id": "6-0-1", "text": "متابعة معدلات النشاط البحثي وتطوير الأداء.", "ess": True},
            {"id": "6-0-11", "text": "تطبيق سياسات واضحة لأخلاقيات البحث العلمي.", "ess": True},
        ]
    }
}

# إنشاء التبويبات
tabs = st.tabs([f"{data[m]['icon']} {m}" for m in data])

for i, title in enumerate(data):
    with tabs[i]:
        st.header(data[title]['sub'])
        for item in data[title]['items']:
            essential_tag = '<span class="essential"> (⭐ محك أساسي)</span>' if item['ess'] else ""
            st.markdown(f"""
                <div class="criterion-box">
                    <strong>محك {item['id']}</strong>{essential_tag}<br>
                    {item['text']}
                    <hr style="margin: 10px 0; border: 0; border-top: 1px solid #eee;">
                    <small style="color: #666;">الشواهد المقترحة: خطط العمل، التقارير السنوية، محاضر الاجتماعات.</small>
                </div>
            """, unsafe_allow_html=True)

# التذييل
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 مبادرة د. علي بن محمد العتيبي - جودة التميز الأكاديمي</p>", unsafe_allow_html=True)
