# -*- coding: utf-8 -*-
"""
دليل الشواهد الذكي للاعتماد البرامجي - نسخة Python / Streamlit
تشغيل التطبيق:
1) pip install streamlit pandas
2) streamlit run smart_accreditation_streamlit_app.py
"""

import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="دليل الشواهد الذكي للاعتماد البرامجي",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# مكتبة الشواهد العامة حسب المجال
# -----------------------------
EVIDENCE_LIBRARY = {
    "governance": {
        "label": "الحوكمة والإدارة",
        "evidences": [
            "توصيف البرنامج المعتمد والنسخة المعلنة للرسالة والأهداف.",
            "محاضر مجالس القسم والكلية المتضمنة الاعتماد أو المراجعة.",
            "مصفوفة مواءمة بين رسالة البرنامج وأهدافه ورسالة الكلية/الجامعة.",
            "الخطة التشغيلية للبرنامج ومؤشرات الأداء المرتبطة بالأهداف.",
            "تقارير متابعة تنفيذ الخطة وقرارات التحسين.",
        ],
        "tips": [
            "وحّد صياغة الرسالة والأهداف في جميع الوثائق؛ فاختلاف الصياغات علامة خطر أمام المراجع.",
            "اربط كل هدف بمؤشر أداء ومبادرة ومسؤول تنفيذ وزمن محدد.",
            "لا ترفع محضرًا عامًا؛ أبرز الفقرة التي تثبت الاعتماد أو المراجعة.",
        ],
    },
    "quality": {
        "label": "ضمان الجودة والتحسين",
        "evidences": [
            "دليل نظام الجودة في البرنامج وآلية ارتباطه بالنظام المؤسسي.",
            "تقرير مؤشرات الأداء السنوي مع التحليل والمقارنة المرجعية.",
            "تقارير الدراسة الذاتية أو التقويم الدوري.",
            "خطط التحسين ومتابعة إغلاق دائرة الجودة.",
            "محاضر لجنة الجودة وما نتج عنها من قرارات.",
        ],
        "tips": [
            "التحليل أهم من الرقم؛ لا تكتف بعرض المؤشر دون تفسير وقرار تحسين.",
            "أثبت أثر التحسين بسلسلة: نتيجة → قرار → إجراء → متابعة → أثر.",
            "استخدم مقارنات داخلية وخارجية موثقة حيث أمكن.",
        ],
    },
    "learning": {
        "label": "نواتج التعلم",
        "evidences": [
            "وثيقة نواتج تعلم البرنامج المعتمدة.",
            "مصفوفة مواءمة النواتج مع الإطار الوطني للمؤهلات.",
            "مصفوفة ربط نواتج البرنامج بالمقررات.",
            "خطة قياس نواتج التعلم وأدواتها المباشرة وغير المباشرة.",
            "تقارير نتائج قياس النواتج وخطط التحسين.",
        ],
        "tips": [
            "استخدم أفعالًا قابلة للقياس وتجنب العبارات الفضفاضة.",
            "يجب أن تكون آلية احتساب تحقق النواتج واضحة لا صندوقًا أسود.",
            "لا تجعل الاختبار النهائي يقيس كل شيء؛ هذه وصفة جاهزة لتعليق المراجع.",
        ],
    },
    "curriculum": {
        "label": "المنهج والخطة الدراسية",
        "evidences": [
            "الخطة الدراسية المعتمدة.",
            "توصيف البرنامج وتوصيفات المقررات.",
            "مصفوفة التتابع والتكامل بين المقررات.",
            "محاضر مراجعة الخطة وتحديثها.",
            "مقارنات مرجعية مع برامج مناظرة ومتطلبات مهنية.",
        ],
        "tips": [
            "أظهر كيف تخدم الخطة أهداف البرنامج ونواتجه لا مجرد سرد المقررات.",
            "وثّق المراجعة الدورية للخطة بمسوغات وقرارات لا بتواريخ صامتة.",
            "تحقق من الاتساق بين الشطرين أو الفروع عند وجودها.",
        ],
    },
    "teaching": {
        "label": "التدريس والتقويم",
        "evidences": [
            "استراتيجية التعليم والتعلم والتقويم المعتمدة.",
            "نماذج من خطط المقررات والاختبارات والواجبات والمشاريع.",
            "سلالم تقدير لقياس المهارات والقيم.",
            "تقارير المقررات وتغذية راجعة للطلاب.",
            "تقارير تحقق جودة التقويم والنزاهة الأكاديمية.",
        ],
        "tips": [
            "طابق بين ما في التوصيف وما يحدث فعليًا في القاعة والتقرير.",
            "نوّع استراتيجيات التدريس والتقويم بحسب طبيعة المخرج.",
            "احتفظ بعينات مقننة من أعمال الطلاب مع آلية تصحيح واضحة.",
        ],
    },
    "students": {
        "label": "الطلاب والخريجون",
        "evidences": [
            "دليل الطالب واللوائح المنشورة للقبول والتسجيل والتخرج.",
            "أدلة الإرشاد الأكاديمي والمهني والنفسي والاجتماعي.",
            "قوائم المرشدين وخطط الإرشاد وسجلات المتابعة.",
            "آليات رعاية المتفوقين والمتعثرين والموهوبين.",
            "استبانات رضا الطلاب وتقارير التحسين.",
        ],
        "tips": [
            "ميّز بين وجود الخدمة وفاعليتها؛ المراجع يريد أثرًا لا لوحة إعلانية.",
            "وثّق حالات المتابعة دون الإخلال بالخصوصية.",
            "استخدم نتائج رضا الطلاب في قرارات تحسين واضحة.",
        ],
    },
    "faculty": {
        "label": "هيئة التدريس",
        "evidences": [
            "بيان أعضاء هيئة التدريس ونصابهم وتخصصاتهم.",
            "خطة التوظيف أو سد العجز عند الحاجة.",
            "خطة التطوير المهني وتقارير حضور البرامج التدريبية.",
            "تقارير تقييم أداء هيئة التدريس والتغذية الراجعة.",
            "بيانات الإنتاج العلمي والمشاركة المجتمعية.",
        ],
        "tips": [
            "لا يكفي عدد أعضاء هيئة التدريس؛ أثبت الملاءمة للتخصص والمقررات والمواقع.",
            "اربط التدريب باحتياج فعلي وقيّم أثره بعد التنفيذ.",
            "استخدم مؤشرات واضحة للإنتاج العلمي والشراكة المجتمعية.",
        ],
    },
    "resources": {
        "label": "مصادر التعلم والمرافق",
        "evidences": [
            "قائمة مصادر التعلم المرتبطة بالمقررات.",
            "تقرير المكتبة وقواعد البيانات والخدمات الإلكترونية.",
            "تقارير جاهزية القاعات والمعامل والتجهيزات.",
            "استبانات رضا الطلاب وهيئة التدريس عن المصادر والمرافق.",
            "خطة تحديث المصادر والمرافق بناءً على نتائج التقويم.",
        ],
        "tips": [
            "اربط المصدر بالمقرر والناتج التعلمي لا ترفع قائمة كتب عائمة.",
            "أثبت كفاية المصادر بالأعداد، وحداثتها، ومدى استخدامها.",
            "اجعل نتائج الرضا مدخلًا لخطة تحسين قابلة للتتبع.",
        ],
    },
    "research": {
        "label": "البحث العلمي والمشاريع",
        "evidences": [
            "خطة البحث العلمي للبرنامج وارتباطها بخطة المؤسسة.",
            "مؤشرات النشاط البحثي والنشر والإنتاج العلمي.",
            "قائمة الأولويات البحثية المعتمدة.",
            "أدلة أخلاقيات البحث العلمي وإجراءات الموافقة.",
            "تقارير متابعة الإشراف العلمي والرسائل والمشاريع.",
        ],
        "tips": [
            "اربط البحث العلمي برسالة البرنامج والتوجهات الوطنية لا بالأمزجة الفردية.",
            "اعرض المؤشرات باتجاه زمني وتحليل، لا رقم سنة واحدة فقط.",
            "في الدراسات العليا تحديدًا: أدلة الرسائل والإشراف والعدالة في المناقشة محورية.",
        ],
    },
    "ethics": {
        "label": "النزاهة والأخلاقيات",
        "evidences": [
            "سياسات النزاهة الأكاديمية والأمانة العلمية وحقوق الملكية الفكرية.",
            "آلية فحص التشابه والانتحال وتقاريرها الدورية.",
            "دليل السلوك المهني والأخلاقي.",
            "محاضر أو تقارير التوعية والتدريب.",
            "إجراءات التعامل مع المخالفات والشكاوى والتظلمات.",
        ],
        "tips": [
            "وجود السياسة لا يكفي؛ أثبت التطبيق والمتابعة وحالات المعالجة إن وجدت.",
            "اربط النزاهة بالطلاب وأعضاء هيئة التدريس والبحث العلمي.",
            "احرص على وضوح الصلاحيات وسرية الإجراءات وعدالتها.",
        ],
    },
}


def criterion(code, text, themes, essential=False):
    return {
        "code": code,
        "text": text,
        "themes": themes,
        "essential": essential,
    }


STANDARDS = [
    {
        "id": "s1",
        "code": "المعيار الأول",
        "title": "إدارة البرنامج وضمان جودته",
        "description": "حوكمة البرنامج ورسالته وأهدافه وضمان الجودة والتحسين المستمر.",
        "substandards": [
            {
                "title": "1-1 إدارة البرنامج",
                "criteria": [
                    criterion("1-1-1", "تتسق رسالة البرنامج وأهدافه مع رسالة المؤسسة/الكلية وتوجه جميع عملياته وأنشطته.", ["governance"]),
                    criterion("1-1-2", "يتوفر لدى البرنامج العدد الكافي من الكوادر المؤهلة للقيام بالمهام الإدارية والمهنية والفنية، ولهم مهام وصلاحيات محددة.", ["governance", "faculty"], True),
                    criterion("1-1-3", "يتوفر للبرنامج مناخ تنظيمي وبيئة أكاديمية داعمة.", ["governance", "students"]),
                    criterion("1-1-4", "يتابع القائمون على البرنامج مدى تحقق أهدافه وتتخذ الإجراءات اللازمة للتحسين.", ["governance", "quality"]),
                    criterion("1-1-5", "تطبق إدارة البرنامج آليات تضمن النزاهة والعدالة والمساواة في جميع ممارساتها الأكاديمية والإدارية، وبين شطري الطلاب والطالبات والفروع إن وجدت.", ["governance", "ethics"]),
                    criterion("1-1-6", "تستفيد إدارة البرنامج من آراء المهنيين والخبراء في تخصص البرنامج في تقييم وتطوير وتحسين أدائه.", ["governance", "quality"]),
                    criterion("1-1-7", "تتيح إدارة البرنامج معلومات موثوقة ومعلنة تتضمن وصف البرنامج وأداءه وإنجازاته بما يتناسب مع احتياجات المستفيدين.", ["governance", "quality"]),
                    criterion("1-1-8", "تلتزم إدارة البرنامج بتفعيل قيم الأمانة العلمية وحقوق الملكية الفكرية وقواعد الممارسات الأخلاقية والسلوك القويم في جميع المجالات والأنشطة الأكاديمية والبحثية والإدارية والخدمية.", ["ethics"], True),
                    criterion("1-1-9", "تطبق إدارة البرنامج الأنظمة واللوائح والإجراءات المعتمدة من قبل المؤسسة/الكلية، بما في ذلك التظلم والشكاوى والقضايا التأديبية.", ["governance", "ethics"]),
                ],
            },
            {
                "title": "1-2 ضمان جودة البرنامج",
                "criteria": [
                    criterion("1-2-1", "تطبق إدارة البرنامج نظامًا فاعلًا لضمان الجودة وإدارتها، يتسق مع نظام الجودة المؤسسي.", ["quality"]),
                    criterion("1-2-2", "يقوم البرنامج بتحليل مؤشرات الأداء الرئيسة وبيانات التقويم سنويًا ويستفاد منها في عمليات التخطيط والتطوير واتخاذ القرارات.", ["quality"], True),
                    criterion("1-2-3", "يجري البرنامج تقويمًا دوريًا شاملًا ويضع خططًا للتحسين، ويتابع تنفيذها.", ["quality"]),
                ],
            },
        ],
    },
    {
        "id": "s2",
        "code": "المعيار الثاني",
        "title": "التعليم والتعلم",
        "description": "نواتج التعلم والمنهج الدراسي وجودة التدريس والتقويم.",
        "substandards": [
            {
                "title": "2-1 نواتج التعلم",
                "criteria": [
                    criterion("2-1-1", "يحدد البرنامج نواتج التعلم المستهدفة وبما يتسق مع رسالته ويتواءم مع خصائص الخريجين على المستوى المؤسسي، ويتم اعتمادها وإعلانها، وتراجع دوريًا.", ["learning"]),
                    criterion("2-1-2", "تتوافق نواتج التعلم مع متطلبات الإطار الوطني للمؤهلات، ومتطلبات سوق العمل.", ["learning"], True),
                    criterion("2-1-3", "يحدد البرنامج نواتج التعلم للمسارات المختلفة إن وجدت.", ["learning"]),
                    criterion("2-1-4", "يطبق البرنامج آليات وأدوات مناسبة لقياس نواتج التعلم والتحقق من استيفائها وفق مستويات أداء وخطط تقييم محددة.", ["learning", "teaching"], True),
                    criterion("2-1-5", "يطبق البرنامج استراتيجية واضحة ومعتمدة للتعليم والتعلم والتقييم، توضح فلسفته التعليمية وتكفل تحقيق نواتج التعلم في البرنامج.", ["learning", "teaching"]),
                ],
            },
            {
                "title": "2-2 المنهج الدراسي",
                "criteria": [
                    criterion("2-2-1", "يراعي المنهج الدراسي تحقيق أهداف البرنامج ونواتجه التعليمية والتطورات العلمية والتقنية والمهنية في مجال التخصص، ويراجع بصورة دورية.", ["curriculum"], True),
                    criterion("2-2-2", "تحقق الخطة الدراسية التوازن بين المتطلبات العامة ومتطلبات التخصص، وبين الجوانب النظرية والتطبيقية، كما تراعي التتابع والتكامل بين المقررات الدراسية.", ["curriculum"], True),
                    criterion("2-2-3", "ترتبط نواتج التعلم في المقررات مع نواتج التعلم في البرنامج في مصفوفة توزيع نواتج تعلم البرنامج على المقررات.", ["curriculum", "learning"]),
                    criterion("2-2-4", "يتأكد البرنامج من تطبيق موحد للخطة الدراسية وتوصيف البرنامج والمقررات التي تقدم في أكثر من موقع، مثل أقسام الطلاب والطالبات.", ["curriculum", "quality"], True),
                ],
            },
            {
                "title": "2-3 جودة التدريس وتقييم الطلاب",
                "criteria": [
                    criterion("2-3-1", "يتحقق البرنامج من فعالية استراتيجيات التعليم والتعلم وطرق التقييم الواردة في توصيفات البرنامج والمقررات ومدى التزام هيئة التدريس بها من خلال آليات محددة.", ["teaching", "quality"], True),
                    criterion("2-3-2", "تتنوع استراتيجيات التعليم والتعلم وطرق التقييم في البرنامج بما يتناسب مع طبيعته ومستواه، وتتوافق مع نواتج التعلم المستهدفة على مستوى البرنامج والمقررات.", ["teaching", "learning"]),
                    criterion("2-3-3", "يقدم التدريب اللازم لهيئة التدريس على استراتيجيات التعليم والتعلم وطرق التقييم المحددة في توصيف البرنامج والمقررات، والاستخدام الفعال للتقنية الحديثة والمتطورة، ويتابع استخدامهم لها.", ["teaching", "faculty"]),
                    criterion("2-3-4", "يزود الطلاب في بداية تدريس كل مقرر بمعلومات شاملة عنه، تتضمن نواتج التعلم، واستراتيجيات التعليم والتعلم وطرق التقييم ومواعيدها، وما يتوقع منهم خلال دراسة المقرر، ويقدم لهم تغذية راجعة عن أدائهم.", ["teaching", "students"]),
                    criterion("2-3-5", "يطبق البرنامج آليات لدعم وتحفيز التميز في التدريس وتشجيع الإبداع والابتكار لدى هيئة التدريس.", ["teaching", "faculty"]),
                    criterion("2-3-6", "يطبق البرنامج إجراءات واضحة ومعلنة للتحقق من جودة طرق التقييم ومصداقيتها، والتأكد من مستوى تحصيل الطلاب.", ["teaching", "quality"]),
                    criterion("2-3-7", "تستخدم إجراءات فعالة لضبط النزاهة الأكاديمية على مستوى البرنامج للتحقق من أن الأعمال والواجبات التي يقدمها الطلاب هي من إنتاجهم.", ["teaching", "ethics"], True),
                ],
            },
        ],
    },
    {
        "id": "s3",
        "code": "المعيار الثالث",
        "title": "الطلاب",
        "description": "قبول الطلاب وخدماتهم وإرشادهم ورعاية فئاتهم وقياس رضاهم.",
        "substandards": [
            {
                "title": "3-0 الطلاب",
                "criteria": [
                    criterion("3-0-1", "يطبق البرنامج معايير وشروط معتمدة ومعلنة لقبول الطلاب وتسجيلهم وتخرجهم، والانتقال إلى البرنامج ومعادلة ما تعلمه الطلاب سابقًا، بما يتناسب مع طبيعة البرنامج، وتطبق بعدالة.", ["students", "governance"]),
                    criterion("3-0-2", "يوفر البرنامج المعلومات الأساسية للطلاب، مثل متطلبات الدراسة، والخدمات، والتكاليف المالية إن وجدت، بوسائل متنوعة.", ["students"]),
                    criterion("3-0-3", "يتوفر لطلاب البرنامج خدمات فعالة للإرشاد والتوجيه الأكاديمي والمهني والنفسي والاجتماعي، من خلال كوادر مؤهلة وكافية.", ["students"], True),
                    criterion("3-0-4", "تطبق آليات ملائمة للتعرف على الطلاب الموهوبين والمبدعين والمتفوقين والمتعثرين في البرنامج، وتتوفر برامج مناسبة لرعاية وتحفيز ودعم كل فئة منهم.", ["students"]),
                    criterion("3-0-5", "يطبق البرنامج آلية فعالة للتواصل مع الخريجين وإشراكهم في مناسباته وأنشطته، واستطلاع آرائهم والاستفادة من خبراتهم ودعمهم، ويوفر قواعد بيانات محدثة وشاملة عنهم.", ["students", "quality"]),
                    criterion("3-0-6", "تطبق آليات فعالة لتقويم كفاية وجودة الخدمات المقدمة للطلاب وقياس رضاهم عنها، والاستفادة من النتائج في التحسين.", ["students", "quality"], True),
                ],
            }
        ],
    },
    {
        "id": "s4",
        "code": "المعيار الرابع",
        "title": "هيئة التدريس",
        "description": "كفاية هيئة التدريس ومشاركاتهم وتطويرهم وتقويم أدائهم.",
        "substandards": [
            {
                "title": "4-0 هيئة التدريس",
                "criteria": [
                    criterion("4-0-1", "يتوافر في البرنامج العدد الكافي من أعضاء هيئة التدريس، في جميع المواقع التي يقدم فيها، وتطبق آليات مناسبة للتحقق منها.", ["faculty"], True),
                    criterion("4-0-2", "تضم هيئة التدريس أو المتعاونين في البرامج المهنية بعض المهنيين من ذوي الخبرة والمهارة العالية في مجال البرنامج.", ["faculty"]),
                    criterion("4-0-3", "يشارك أعضاء هيئة التدريس في الأنشطة الأكاديمية والبحثية والإنتاج العلمي بكفاءة وانتظام، وتعد مشاركتهم في هذه الأنشطة أحد محكات تقييمهم.", ["faculty", "research"]),
                    criterion("4-0-4", "تشارك هيئة التدريس في أنشطة الشراكة المجتمعية، وتعد مشاركتهم في هذه الأنشطة أحد محكات تقييمهم.", ["faculty"]),
                    criterion("4-0-5", "يتلقى أعضاء هيئة التدريس برامج في التطوير المهني والأكاديمي، وفق خطة تلبي احتياجاتهم وتسهم في تطوير أدائهم.", ["faculty", "quality"]),
                    criterion("4-0-6", "يقيم أداء هيئة التدريس بانتظام وفق معايير محددة ومعلنة، وتقدم التغذية الراجعة لهم، ويستفاد من النتائج في تحسين الأداء.", ["faculty", "quality"], True),
                ],
            }
        ],
    },
    {
        "id": "s5",
        "code": "المعيار الخامس",
        "title": "مصادر التعلم والمرافق والتجهيزات",
        "description": "كفاية المصادر والمرافق والتجهيزات والسلامة والتقنية والتقويم.",
        "substandards": [
            {
                "title": "5-0 مصادر التعلم والمرافق والتجهيزات",
                "criteria": [
                    criterion("5-0-1", "يتحقق البرنامج من كفاية ومناسبة مصادر التعلم والخدمات المقدمة بما يتناسب مع احتياجاته وأعداد الطلاب، ويتم تحديثها بصورة دورية.", ["resources"]),
                    criterion("5-0-2", "يتوفر لهيئة التدريس والطلاب والموظفين في البرنامج التهيئة والدعم الفني المناسبين للاستخدام الفعال لمصادر ووسائل التعلم.", ["resources", "faculty", "students"]),
                    criterion("5-0-3", "تطبق معايير السلامة والحفاظ على البيئة والتخلص من النفايات الخطرة بكفاءة وفاعلية، مع توفر جميع متطلبات الصحة والسلامة العامة والمهنية في المرافق والتجهيزات والأنشطة التعليمية والبحثية.", ["resources"], True),
                    criterion("5-0-4", "يتوفر للبرنامج التقنيات والخدمات والبيئة المناسبة للمقررات التي تقدم إلكترونيًا أو عن بعد وفق المعايير الخاصة بها.", ["resources", "teaching"]),
                    criterion("5-0-5", "يعمل البرنامج على تقويم فاعلية وكفاءة مصادر التعلم والمرافق والتجهيزات بأنواعها، ويستفاد من ذلك في التحسين.", ["resources", "quality"]),
                ],
            }
        ],
    },
    {
        "id": "s6",
        "code": "المعيار السادس",
        "title": "البحوث العلمية والمشاريع",
        "description": "النشاط البحثي والأولويات والبيئة البحثية والرسائل والمشاريع وأخلاقيات البحث.",
        "substandards": [
            {
                "title": "6-0 البحوث العلمية والمشاريع",
                "criteria": [
                    criterion("6-0-1", "يتابع البرنامج معدلات نشاطه البحثي وفق دوره في خطة البحث العلمي للمؤسسة، وفق مؤشرات أداء واضحة ومحددة، ويعمل على تطوير أدائه.", ["research", "quality"], True),
                    criterion("6-0-2", "يحدد البرنامج الأولويات البحثية بما يتناسب مع رسالة المؤسسة والتوجهات الوطنية وخطط التنمية.", ["research"]),
                    criterion("6-0-3", "يتوفر للبرنامج البيئة المحفزة والإمكانات المالية والتجهيزات التقنية والبحثية اللازمة لتنفيذ أنشطته البحثية.", ["research", "resources"]),
                    criterion("6-0-4", "يطبق البرنامج آليات متنوعة لتنمية مهارات البحث العلمي والنشر لدى منسوبيه، وتبادل الخبرات ونتائج البحوث فيما بينهم، ويقوم تلك الآليات ويعمل على تطويرها وتحسينها.", ["research", "faculty", "quality"]),
                    criterion("6-0-5", "يطبق البرنامج آليات متنوعة لتمويل أنشطته البحثية من الجهات المانحة وجهات الاستثمار.", ["research"]),
                    criterion("6-0-6", "يطبق في البرنامج إجراءات أكاديمية وإدارية محددة وعادلة للموافقة على الرسائل العلمية والمشاريع البحثية في إطار زمني مناسب.", ["research", "ethics"]),
                    criterion("6-0-7", "يتوفر لدى البرنامج أدلة إرشادية واضحة ومعلنة لإعداد وتقييم الرسائل العلمية والمشاريع.", ["research"]),
                    criterion("6-0-8", "يطبق البرنامج آليات محددة لمتابعة فاعلية الإشراف العلمي على الرسائل والبحوث العلمية والمشاريع، ويتم تقويمها وتطويرها.", ["research", "quality"]),
                    criterion("6-0-9", "يراقب البرنامج عدالة وموضوعية ومصداقية تقييم البحوث ومناقشة الرسائل العلمية وإجازتها.", ["research", "ethics"]),
                    criterion("6-0-10", "يتحقق البرنامج من توفر الأصالة العلمية والإثراء المعرفي والابتكار في أنشطته البحثية بما يتناسب مع مستوى المؤهل والمعايير العالمية.", ["research"]),
                    criterion("6-0-11", "يطبق البرنامج سياسات واضحة لأخلاقيات وضوابط البحث العلمي ويتابع التزام الباحثين بها وفق آليات مناسبة ويعمل على تطويرها.", ["research", "ethics"], True),
                ],
            }
        ],
    },
]


COMMON_MISTAKES = [
    "إرفاق شاهد عام لا يظهر صلته المباشرة بالمحك.",
    "رفع وثيقة غير معتمدة أو غير مؤرخة أو غير موقعة عند الحاجة.",
    "غياب تحليل النتائج أو عدم وجود أثر للتحسين.",
    "تعارض البيانات بين الدراسة الذاتية والتوصيفات والتقارير السنوية.",
]

CHECKLIST = [
    "هل الشاهد معتمد؟",
    "هل الشاهد حديث ومؤرخ؟",
    "هل تظهر علاقة الشاهد بالمحك مباشرة؟",
    "هل يوجد تحليل لا مجرد سرد؟",
    "هل توجد إجراءات تحسين ومتابعة؟",
]

STATUS_OPTIONS = {
    "غير مقيّم": 0,
    "مكتمل": 1,
    "جزئي": 0.5,
    "غير متوفر": 0,
}


def flatten_criteria():
    rows = []
    for standard in STANDARDS:
        for sub in standard["substandards"]:
            for cr in sub["criteria"]:
                rows.append({
                    "standard_id": standard["id"],
                    "standard_code": standard["code"],
                    "standard_title": standard["title"],
                    "substandard": sub["title"],
                    "criterion_code": cr["code"],
                    "criterion_text": cr["text"],
                    "essential": cr["essential"],
                    "themes": cr["themes"],
                })
    return rows


def unique(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


def support_for_criterion(themes):
    evidences = []
    tips = []
    labels = []
    for theme in themes:
        item = EVIDENCE_LIBRARY.get(theme, {})
        evidences.extend(item.get("evidences", []))
        tips.extend(item.get("tips", []))
        if item.get("label"):
            labels.append(item["label"])
    return {
        "evidences": unique(evidences),
        "tips": unique(tips),
        "labels": unique(labels),
        "mistakes": COMMON_MISTAKES,
        "checklist": CHECKLIST,
    }


def init_session_state(rows):
    if "readiness" not in st.session_state:
        st.session_state.readiness = {row["criterion_code"]: "غير مقيّم" for row in rows}
    if "notes" not in st.session_state:
        st.session_state.notes = {row["criterion_code"]: "" for row in rows}


def calculate_score(rows):
    if not rows:
        return 0
    total = sum(STATUS_OPTIONS.get(st.session_state.readiness.get(row["criterion_code"], "غير مقيّم"), 0) for row in rows)
    return round((total / len(rows)) * 100)


def generate_criterion_report(row):
    support = support_for_criterion(row["themes"])
    status = st.session_state.readiness.get(row["criterion_code"], "غير مقيّم")
    note = st.session_state.notes.get(row["criterion_code"], "")
    return f"""
دليل الشواهد الذكي للاعتماد البرامجي
تاريخ التقرير: {datetime.now().strftime('%Y-%m-%d %H:%M')}

{row['standard_code']}: {row['standard_title']}
{row['substandard']}

المحك: {row['criterion_code']}
{row['criterion_text']}

نوع المحك: {'أساسي' if row['essential'] else 'غير أساسي'}
حالة الجاهزية: {status}

الأدلة والشواهد المقترحة:
- """ + "\n- ".join(support["evidences"]) + f"""

نصائح تنفيذية:
- """ + "\n- ".join(support["tips"]) + f"""

أخطاء شائعة:
- """ + "\n- ".join(support["mistakes"]) + f"""

قائمة تحقق قبل رفع الشاهد:
- """ + "\n- ".join(support["checklist"]) + f"""

ملاحظات البرنامج:
{note if note.strip() else 'لا توجد ملاحظات مدخلة.'}
""".strip()


def generate_gap_report(rows):
    lines = []
    score = calculate_score(rows)
    lines.append("تقرير فجوات الشواهد للاعتماد البرامجي")
    lines.append(f"تاريخ التقرير: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"نسبة الجاهزية العامة: {score}%")
    lines.append("")

    for row in rows:
        status = st.session_state.readiness.get(row["criterion_code"], "غير مقيّم")
        if status != "مكتمل":
            support = support_for_criterion(row["themes"])
            lines.append("-" * 60)
            lines.append(f"{row['standard_code']} - {row['standard_title']}")
            lines.append(row["substandard"])
            lines.append(f"المحك {row['criterion_code']}: {row['criterion_text']}")
            lines.append(f"الحالة: {status}")
            lines.append("أبرز الشواهد المطلوبة:")
            for ev in support["evidences"][:5]:
                lines.append(f"- {ev}")
            note = st.session_state.notes.get(row["criterion_code"], "")
            if note.strip():
                lines.append(f"ملاحظات البرنامج: {note}")
            lines.append("")

    return "\n".join(lines)


def rtl_css():
    st.markdown(
        """
        <style>
        html, body, [class*="css"] {
            direction: rtl;
            text-align: right;
            font-family: 'Tahoma', 'Arial', sans-serif;
        }
        .main-title {
            padding: 22px;
            border-radius: 24px;
            background: linear-gradient(135deg, #134e4a, #0f766e, #10b981);
            color: white;
            margin-bottom: 20px;
        }
        .main-title h1 {
            margin-bottom: 8px;
            font-size: 34px;
            font-weight: 900;
        }
        .main-title p {
            color: #ecfdf5;
            font-size: 16px;
        }
        .criterion-box {
            border: 1px solid #d1fae5;
            background: #f0fdfa;
            padding: 18px;
            border-radius: 20px;
            margin-bottom: 14px;
        }
        .small-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 999px;
            background: #ccfbf1;
            color: #134e4a;
            font-weight: 700;
            margin: 2px;
            font-size: 13px;
        }
        .essential-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 999px;
            background: #fee2e2;
            color: #991b1b;
            font-weight: 700;
            margin: 2px;
            font-size: 13px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    rtl_css()
    rows = flatten_criteria()
    init_session_state(rows)

    st.markdown(
        """
        <div class="main-title">
            <h1>دليل الشواهد الذكي للاعتماد البرامجي</h1>
            <p>نسخة تفاعلية لمساعدة البرامج الأكاديمية في اختيار الشواهد، وتقييم الجاهزية، وتوليد تقرير فجوات الاعتماد.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    score = calculate_score(rows)
    complete = sum(1 for row in rows if st.session_state.readiness[row["criterion_code"]] == "مكتمل")
    partial = sum(1 for row in rows if st.session_state.readiness[row["criterion_code"]] == "جزئي")
    missing = sum(1 for row in rows if st.session_state.readiness[row["criterion_code"]] == "غير متوفر")
    essential_count = sum(1 for row in rows if row["essential"])

    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("نسبة الجاهزية", f"{score}%")
    k2.metric("إجمالي المحكات", len(rows))
    k3.metric("المحكات الأساسية", essential_count)
    k4.metric("مكتمل", complete)
    k5.metric("جزئي/غير متوفر", partial + missing)

    st.progress(score / 100)

    with st.sidebar:
        st.header("لوحة التحكم")
        standard_titles = [f"{s['code']} - {s['title']}" for s in STANDARDS]
        selected_standard_title = st.selectbox("اختر المعيار", standard_titles)
        selected_standard_index = standard_titles.index(selected_standard_title)
        selected_standard = STANDARDS[selected_standard_index]

        search = st.text_input("بحث برقم المحك أو كلمة مفتاحية")
        filter_status = st.selectbox("فلترة حسب الجاهزية", ["الكل", "غير مقيّم", "مكتمل", "جزئي", "غير متوفر"])
        only_essential = st.checkbox("عرض المحكات الأساسية فقط")

        gap_report = generate_gap_report(rows)
        st.download_button(
            "تحميل تقرير فجوات الشواهد",
            data=gap_report,
            file_name="تقرير_فجوات_الشواهد.txt",
            mime="text/plain",
            use_container_width=True,
        )

    visible_rows = [row for row in rows if row["standard_id"] == selected_standard["id"]]

    if search.strip():
        q = search.strip().lower()
        visible_rows = [
            row for row in rows
            if q in f"{row['standard_code']} {row['standard_title']} {row['substandard']} {row['criterion_code']} {row['criterion_text']}".lower()
        ]

    if only_essential:
        visible_rows = [row for row in visible_rows if row["essential"]]

    if filter_status != "الكل":
        visible_rows = [row for row in visible_rows if st.session_state.readiness[row["criterion_code"]] == filter_status]

    st.subheader(f"{selected_standard['code']}: {selected_standard['title']}")
    st.write(selected_standard["description"])

    if not visible_rows:
        st.warning("لا توجد محكات مطابقة لخيارات البحث أو الفلترة.")
        return

    criterion_options = [f"{row['criterion_code']} - {row['criterion_text'][:90]}" for row in visible_rows]
    selected_criterion_option = st.selectbox("اختر المحك", criterion_options)
    selected_row = visible_rows[criterion_options.index(selected_criterion_option)]
    support = support_for_criterion(selected_row["themes"])

    essential_badge = '<span class="essential-badge">محك أساسي</span>' if selected_row["essential"] else ''
    criterion_html = f'''<div class="criterion-box">
<span class="small-badge">{selected_row["criterion_code"]}</span>
{essential_badge}
<span class="small-badge">{selected_row["substandard"]}</span>
<h3>{selected_row["criterion_text"]}</h3>
</div>'''
    st.markdown(criterion_html, unsafe_allow_html=True)

    st.markdown("### تقييم جاهزية المحك")
    current_status = st.session_state.readiness[selected_row["criterion_code"]]
    new_status = st.radio(
        "حالة الجاهزية",
        ["غير مقيّم", "مكتمل", "جزئي", "غير متوفر"],
        index=["غير مقيّم", "مكتمل", "جزئي", "غير متوفر"].index(current_status),
        horizontal=True,
    )
    st.session_state.readiness[selected_row["criterion_code"]] = new_status

    st.session_state.notes[selected_row["criterion_code"]] = st.text_area(
        "ملاحظات البرنامج على هذا المحك",
        value=st.session_state.notes.get(selected_row["criterion_code"], ""),
        height=100,
        placeholder="مثال: الشاهد موجود لكنه يحتاج توقيع الاعتماد، أو يلزم تحديث تقرير المؤشرات لهذا العام...",
    )

    tab1, tab2, tab3, tab4 = st.tabs(["الأدلة والشواهد", "نصائح تنفيذية", "أخطاء شائعة", "قائمة تحقق"])

    with tab1:
        for ev in support["evidences"]:
            st.markdown(f"- {ev}")

    with tab2:
        for tip in support["tips"]:
            st.markdown(f"- {tip}")

    with tab3:
        for mistake in support["mistakes"]:
            st.markdown(f"- {mistake}")

    with tab4:
        for item in support["checklist"]:
            st.checkbox(item, key=f"check_{selected_row['criterion_code']}_{item}")

    st.info("تنبيه مراجع جودة: الشاهد القوي ليس الملف الأكثر عددًا، بل الملف الأوضح صلة بالمحك، والأثبت اعتمادًا، والأقدر على إظهار التحليل والتحسين.")

    criterion_report = generate_criterion_report(selected_row)
    st.download_button(
        "تحميل تقرير هذا المحك",
        data=criterion_report,
        file_name=f"تقرير_محك_{selected_row['criterion_code']}.txt",
        mime="text/plain",
        use_container_width=True,
    )

    with st.expander("عرض جدول المحكات الحالي"):
        df = pd.DataFrame(visible_rows)
        df["status"] = df["criterion_code"].map(st.session_state.readiness)
        df = df[["standard_code", "standard_title", "substandard", "criterion_code", "criterion_text", "essential", "status"]]
        df.columns = ["المعيار", "عنوان المعيار", "المعيار الفرعي", "رمز المحك", "نص المحك", "أساسي", "الجاهزية"]
        st.dataframe(df, use_container_width=True, hide_index=True)


if __name__ == "__main__":
    main()
