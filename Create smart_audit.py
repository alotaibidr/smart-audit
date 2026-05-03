import React, { useMemo, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Search,
  ClipboardCheck,
  Download,
  Copy,
  BarChart3,
  ShieldCheck,
  FileText,
  AlertTriangle,
  CheckCircle2,
  Layers3,
  GraduationCap,
  Users,
  BookOpen,
  Building2,
  Microscope,
  Settings2,
  Sparkles,
  Filter,
} from "lucide-react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const evidenceLibrary = {
  governance: {
    label: "الحوكمة والإدارة",
    evidences: [
      "توصيف البرنامج المعتمد والنسخة المعلنة للرسالة والأهداف.",
      "محاضر مجالس القسم والكلية المتضمنة الاعتماد أو المراجعة.",
      "مصفوفة مواءمة بين رسالة البرنامج وأهدافه ورسالة الكلية/الجامعة.",
      "الخطة التشغيلية للبرنامج ومؤشرات الأداء المرتبطة بالأهداف.",
      "تقارير متابعة تنفيذ الخطة وقرارات التحسين.",
    ],
    tips: [
      "وحّد صياغة الرسالة والأهداف في جميع الوثائق؛ فاختلاف الصياغات علامة خطر أمام المراجع.",
      "اربط كل هدف بمؤشر أداء ومبادرة ومسؤول تنفيذ وزمن محدد.",
      "لا ترفع محضرًا عامًا؛ أبرز الفقرة التي تثبت الاعتماد أو المراجعة.",
    ],
  },
  quality: {
    label: "ضمان الجودة والتحسين",
    evidences: [
      "دليل نظام الجودة في البرنامج وآلية ارتباطه بالنظام المؤسسي.",
      "تقرير مؤشرات الأداء السنوي مع التحليل والمقارنة المرجعية.",
      "تقارير الدراسة الذاتية أو التقويم الدوري.",
      "خطط التحسين ومتابعة إغلاق دائرة الجودة.",
      "محاضر لجنة الجودة وما نتج عنها من قرارات.",
    ],
    tips: [
      "التحليل أهم من الرقم؛ لا تكتف بعرض المؤشر دون تفسير وقرار تحسين.",
      "أثبت أثر التحسين بسلسلة: نتيجة → قرار → إجراء → متابعة → أثر.",
      "استخدم مقارنات داخلية وخارجية موثقة حيث أمكن.",
    ],
  },
  learning: {
    label: "نواتج التعلم",
    evidences: [
      "وثيقة نواتج تعلم البرنامج المعتمدة.",
      "مصفوفة مواءمة النواتج مع الإطار الوطني للمؤهلات.",
      "مصفوفة ربط نواتج البرنامج بالمقررات.",
      "خطة قياس نواتج التعلم وأدواتها المباشرة وغير المباشرة.",
      "تقارير نتائج قياس النواتج وخطط التحسين.",
    ],
    tips: [
      "استخدم أفعالًا قابلة للقياس وتجنب العبارات الفضفاضة.",
      "يجب أن تكون آلية احتساب تحقق النواتج واضحة لا صندوقًا أسود.",
      "لا تجعل الاختبار النهائي يقيس كل شيء؛ هذه وصفة جاهزة لتعليق المراجع.",
    ],
  },
  curriculum: {
    label: "المنهج والخطة الدراسية",
    evidences: [
      "الخطة الدراسية المعتمدة.",
      "توصيف البرنامج وتوصيفات المقررات.",
      "مصفوفة التتابع والتكامل بين المقررات.",
      "محاضر مراجعة الخطة وتحديثها.",
      "مقارنات مرجعية مع برامج مناظرة ومتطلبات مهنية.",
    ],
    tips: [
      "أظهر كيف تخدم الخطة أهداف البرنامج ونواتجه لا مجرد سرد المقررات.",
      "وثّق المراجعة الدورية للخطة بمسوغات وقرارات لا بتواريخ صامتة.",
      "تحقق من الاتساق بين الشطرين أو الفروع عند وجودها.",
    ],
  },
  teaching: {
    label: "التدريس والتقويم",
    evidences: [
      "استراتيجية التعليم والتعلم والتقويم المعتمدة.",
      "نماذج من خطط المقررات والاختبارات والواجبات والمشاريع.",
      "سلالم تقدير لقياس المهارات والقيم.",
      "تقارير المقررات وتغذية راجعة للطلاب.",
      "تقارير تحقق جودة التقويم والنزاهة الأكاديمية.",
    ],
    tips: [
      "طابق بين ما في التوصيف وما يحدث فعليًا في القاعة والتقرير.",
      "نوّع استراتيجيات التدريس والتقويم بحسب طبيعة المخرج.",
      "احتفظ بعينات مقننة من أعمال الطلاب مع آلية تصحيح واضحة.",
    ],
  },
  students: {
    label: "الطلاب والخريجون",
    evidences: [
      "دليل الطالب واللوائح المنشورة للقبول والتسجيل والتخرج.",
      "أدلة الإرشاد الأكاديمي والمهني والنفسي والاجتماعي.",
      "قوائم المرشدين وخطط الإرشاد وسجلات المتابعة.",
      "آليات رعاية المتفوقين والمتعثرين والموهوبين.",
      "استبانات رضا الطلاب وتقارير التحسين.",
    ],
    tips: [
      "ميّز بين وجود الخدمة وفاعليتها؛ المراجع يريد أثرًا لا لوحة إعلانية.",
      "وثّق حالات المتابعة دون الإخلال بالخصوصية.",
      "استخدم نتائج رضا الطلاب في قرارات تحسين واضحة.",
    ],
  },
  faculty: {
    label: "هيئة التدريس",
    evidences: [
      "بيان أعضاء هيئة التدريس ونصابهم وتخصصاتهم.",
      "خطة التوظيف أو سد العجز عند الحاجة.",
      "خطة التطوير المهني وتقارير حضور البرامج التدريبية.",
      "تقارير تقييم أداء هيئة التدريس والتغذية الراجعة.",
      "بيانات الإنتاج العلمي والمشاركة المجتمعية.",
    ],
    tips: [
      "لا يكفي عدد أعضاء هيئة التدريس؛ أثبت الملاءمة للتخصص والمقررات والمواقع.",
      "اربط التدريب باحتياج فعلي وقيّم أثره بعد التنفيذ.",
      "استخدم مؤشرات واضحة للإنتاج العلمي والشراكة المجتمعية.",
    ],
  },
  resources: {
    label: "مصادر التعلم والمرافق",
    evidences: [
      "قائمة مصادر التعلم المرتبطة بالمقررات.",
      "تقرير المكتبة وقواعد البيانات والخدمات الإلكترونية.",
      "تقارير جاهزية القاعات والمعامل والتجهيزات.",
      "استبانات رضا الطلاب وهيئة التدريس عن المصادر والمرافق.",
      "خطة تحديث المصادر والمرافق بناءً على نتائج التقويم.",
    ],
    tips: [
      "اربط المصدر بالمقرر والناتج التعلمي لا ترفع قائمة كتب عائمة.",
      "أثبت كفاية المصادر بالأعداد، وحداثتها، ومدى استخدامها.",
      "اجعل نتائج الرضا مدخلًا لخطة تحسين قابلة للتتبع.",
    ],
  },
  research: {
    label: "البحث العلمي والمشاريع",
    evidences: [
      "خطة البحث العلمي للبرنامج وارتباطها بخطة المؤسسة.",
      "مؤشرات النشاط البحثي والنشر والإنتاج العلمي.",
      "قائمة الأولويات البحثية المعتمدة.",
      "أدلة أخلاقيات البحث العلمي وإجراءات الموافقة.",
      "تقارير متابعة الإشراف العلمي والرسائل والمشاريع.",
    ],
    tips: [
      "اربط البحث العلمي برسالة البرنامج والتوجهات الوطنية لا بالأمزجة الفردية.",
      "اعرض المؤشرات باتجاه زمني وتحليل، لا رقم سنة واحدة فقط.",
      "في الدراسات العليا تحديدًا: أدلة الرسائل والإشراف والعدالة في المناقشة محورية.",
    ],
  },
  ethics: {
    label: "النزاهة والأخلاقيات",
    evidences: [
      "سياسات النزاهة الأكاديمية والأمانة العلمية وحقوق الملكية الفكرية.",
      "آلية فحص التشابه والانتحال وتقاريرها الدورية.",
      "دليل السلوك المهني والأخلاقي.",
      "محاضر أو تقارير التوعية والتدريب.",
      "إجراءات التعامل مع المخالفات والشكاوى والتظلمات.",
    ],
    tips: [
      "وجود السياسة لا يكفي؛ أثبت التطبيق والمتابعة وحالات المعالجة إن وجدت.",
      "اربط النزاهة بالطلاب وأعضاء هيئة التدريس والبحث العلمي.",
      "احرص على وضوح الصلاحيات وسرية الإجراءات وعدالتها.",
    ],
  },
};

const standards = [
  {
    id: "s1",
    icon: Building2,
    title: "إدارة البرنامج وضمان جودته",
    code: "المعيار الأول",
    description: "حوكمة البرنامج ورسالته وأهدافه وضمان الجودة والتحسين المستمر.",
    substandards: [
      {
        title: "1-1 إدارة البرنامج",
        criteria: [
          c("1-1-1", "تتسق رسالة البرنامج وأهدافه مع رسالة المؤسسة/الكلية وتوجه جميع عملياته وأنشطته.", ["governance"]),
          c("1-1-2", "يتوفر لدى البرنامج العدد الكافي من الكوادر المؤهلة للقيام بالمهام الإدارية والمهنية والفنية، ولهم مهام وصلاحيات محددة.", ["governance", "faculty"], true),
          c("1-1-3", "يتوفر للبرنامج مناخ تنظيمي وبيئة أكاديمية داعمة.", ["governance", "students"]),
          c("1-1-4", "يتابع القائمون على البرنامج مدى تحقق أهدافه وتتخذ الإجراءات اللازمة للتحسين.", ["governance", "quality"]),
          c("1-1-5", "تطبق إدارة البرنامج آليات تضمن النزاهة والعدالة والمساواة في جميع ممارساتها الأكاديمية والإدارية، وبين شطري الطلاب والطالبات والفروع إن وجدت.", ["governance", "ethics"]),
          c("1-1-6", "تستفيد إدارة البرنامج من آراء المهنيين والخبراء في تخصص البرنامج في تقييم وتطوير وتحسين أدائه.", ["governance", "quality"]),
          c("1-1-7", "تتيح إدارة البرنامج معلومات موثوقة ومعلنة تتضمن وصف البرنامج وأداءه وإنجازاته بما يتناسب مع احتياجات المستفيدين.", ["governance", "quality"]),
          c("1-1-8", "تلتزم إدارة البرنامج بتفعيل قيم الأمانة العلمية وحقوق الملكية الفكرية وقواعد الممارسات الأخلاقية والسلوك القويم في جميع المجالات والأنشطة الأكاديمية والبحثية والإدارية والخدمية.", ["ethics"], true),
          c("1-1-9", "تطبق إدارة البرنامج الأنظمة واللوائح والإجراءات المعتمدة من قبل المؤسسة/الكلية، بما في ذلك التظلم والشكاوى والقضايا التأديبية.", ["governance", "ethics"]),
        ],
      },
      {
        title: "1-2 ضمان جودة البرنامج",
        criteria: [
          c("1-2-1", "تطبق إدارة البرنامج نظامًا فاعلًا لضمان الجودة وإدارتها، يتسق مع نظام الجودة المؤسسي.", ["quality"]),
          c("1-2-2", "يقوم البرنامج بتحليل مؤشرات الأداء الرئيسة وبيانات التقويم سنويًا ويستفاد منها في عمليات التخطيط والتطوير واتخاذ القرارات.", ["quality"], true),
          c("1-2-3", "يجري البرنامج تقويمًا دوريًا شاملًا ويضع خططًا للتحسين، ويتابع تنفيذها.", ["quality"]),
        ],
      },
    ],
  },
  {
    id: "s2",
    icon: GraduationCap,
    title: "التعليم والتعلم",
    code: "المعيار الثاني",
    description: "نواتج التعلم والمنهج الدراسي وجودة التدريس والتقويم.",
    substandards: [
      {
        title: "2-1 نواتج التعلم",
        criteria: [
          c("2-1-1", "يحدد البرنامج نواتج التعلم المستهدفة وبما يتسق مع رسالته ويتواءم مع خصائص الخريجين على المستوى المؤسسي، ويتم اعتمادها وإعلانها، وتراجع دوريًا.", ["learning"]),
          c("2-1-2", "تتوافق نواتج التعلم مع متطلبات الإطار الوطني للمؤهلات، ومتطلبات سوق العمل.", ["learning"], true),
          c("2-1-3", "يحدد البرنامج نواتج التعلم للمسارات المختلفة إن وجدت.", ["learning"]),
          c("2-1-4", "يطبق البرنامج آليات وأدوات مناسبة لقياس نواتج التعلم والتحقق من استيفائها وفق مستويات أداء وخطط تقييم محددة.", ["learning", "teaching"], true),
          c("2-1-5", "يطبق البرنامج استراتيجية واضحة ومعتمدة للتعليم والتعلم والتقييم، توضح فلسفته التعليمية وتكفل تحقيق نواتج التعلم في البرنامج.", ["learning", "teaching"]),
        ],
      },
      {
        title: "2-2 المنهج الدراسي",
        criteria: [
          c("2-2-1", "يراعي المنهج الدراسي تحقيق أهداف البرنامج ونواتجه التعليمية والتطورات العلمية والتقنية والمهنية في مجال التخصص، ويراجع بصورة دورية.", ["curriculum"], true),
          c("2-2-2", "تحقق الخطة الدراسية التوازن بين المتطلبات العامة ومتطلبات التخصص، وبين الجوانب النظرية والتطبيقية، كما تراعي التتابع والتكامل بين المقررات الدراسية.", ["curriculum"], true),
          c("2-2-3", "ترتبط نواتج التعلم في المقررات مع نواتج التعلم في البرنامج في مصفوفة توزيع نواتج تعلم البرنامج على المقررات.", ["curriculum", "learning"]),
          c("2-2-4", "يتأكد البرنامج من تطبيق موحد للخطة الدراسية وتوصيف البرنامج والمقررات التي تقدم في أكثر من موقع، مثل أقسام الطلاب والطالبات.", ["curriculum", "quality"], true),
        ],
      },
      {
        title: "2-3 جودة التدريس وتقييم الطلاب",
        criteria: [
          c("2-3-1", "يتحقق البرنامج من فعالية استراتيجيات التعليم والتعلم وطرق التقييم الواردة في توصيفات البرنامج والمقررات ومدى التزام هيئة التدريس بها من خلال آليات محددة.", ["teaching", "quality"], true),
          c("2-3-2", "تتنوع استراتيجيات التعليم والتعلم وطرق التقييم في البرنامج بما يتناسب مع طبيعته ومستواه، وتتوافق مع نواتج التعلم المستهدفة على مستوى البرنامج والمقررات.", ["teaching", "learning"]),
          c("2-3-3", "يقدم التدريب اللازم لهيئة التدريس على استراتيجيات التعليم والتعلم وطرق التقييم المحددة في توصيف البرنامج والمقررات، والاستخدام الفعال للتقنية الحديثة والمتطورة، ويتابع استخدامهم لها.", ["teaching", "faculty"]),
          c("2-3-4", "يزود الطلاب في بداية تدريس كل مقرر بمعلومات شاملة عنه، تتضمن نواتج التعلم، واستراتيجيات التعليم والتعلم وطرق التقييم ومواعيدها، وما يتوقع منهم خلال دراسة المقرر، ويقدم لهم تغذية راجعة عن أدائهم.", ["teaching", "students"]),
          c("2-3-5", "يطبق البرنامج آليات لدعم وتحفيز التميز في التدريس وتشجيع الإبداع والابتكار لدى هيئة التدريس.", ["teaching", "faculty"]),
          c("2-3-6", "يطبق البرنامج إجراءات واضحة ومعلنة للتحقق من جودة طرق التقييم ومصداقيتها، والتأكد من مستوى تحصيل الطلاب.", ["teaching", "quality"]),
          c("2-3-7", "تستخدم إجراءات فعالة لضبط النزاهة الأكاديمية على مستوى البرنامج للتحقق من أن الأعمال والواجبات التي يقدمها الطلاب هي من إنتاجهم.", ["teaching", "ethics"], true),
        ],
      },
    ],
  },
  {
    id: "s3",
    icon: Users,
    title: "الطلاب",
    code: "المعيار الثالث",
    description: "قبول الطلاب وخدماتهم وإرشادهم ورعاية فئاتهم وقياس رضاهم.",
    substandards: [
      {
        title: "3-0 الطلاب",
        criteria: [
          c("3-0-1", "يطبق البرنامج معايير وشروط معتمدة ومعلنة لقبول الطلاب وتسجيلهم وتخرجهم، والانتقال إلى البرنامج ومعادلة ما تعلمه الطلاب سابقًا، بما يتناسب مع طبيعة البرنامج، وتطبق بعدالة.", ["students", "governance"]),
          c("3-0-2", "يوفر البرنامج المعلومات الأساسية للطلاب، مثل متطلبات الدراسة، والخدمات، والتكاليف المالية إن وجدت، بوسائل متنوعة.", ["students"]),
          c("3-0-3", "يتوفر لطلاب البرنامج خدمات فعالة للإرشاد والتوجيه الأكاديمي والمهني والنفسي والاجتماعي، من خلال كوادر مؤهلة وكافية.", ["students"], true),
          c("3-0-4", "تطبق آليات ملائمة للتعرف على الطلاب الموهوبين والمبدعين والمتفوقين والمتعثرين في البرنامج، وتتوفر برامج مناسبة لرعاية وتحفيز ودعم كل فئة منهم.", ["students"]),
          c("3-0-5", "يطبق البرنامج آلية فعالة للتواصل مع الخريجين وإشراكهم في مناسباته وأنشطته، واستطلاع آرائهم والاستفادة من خبراتهم ودعمهم، ويوفر قواعد بيانات محدثة وشاملة عنهم.", ["students", "quality"]),
          c("3-0-6", "تطبق آليات فعالة لتقويم كفاية وجودة الخدمات المقدمة للطلاب وقياس رضاهم عنها، والاستفادة من النتائج في التحسين.", ["students", "quality"], true),
        ],
      },
    ],
  },
  {
    id: "s4",
    icon: BookOpen,
    title: "هيئة التدريس",
    code: "المعيار الرابع",
    description: "كفاية هيئة التدريس ومشاركاتهم وتطويرهم وتقويم أدائهم.",
    substandards: [
      {
        title: "4-0 هيئة التدريس",
        criteria: [
          c("4-0-1", "يتوافر في البرنامج العدد الكافي من أعضاء هيئة التدريس، في جميع المواقع التي يقدم فيها، وتطبق آليات مناسبة للتحقق منها.", ["faculty"], true),
          c("4-0-2", "تضم هيئة التدريس أو المتعاونين في البرامج المهنية بعض المهنيين من ذوي الخبرة والمهارة العالية في مجال البرنامج.", ["faculty"]),
          c("4-0-3", "يشارك أعضاء هيئة التدريس في الأنشطة الأكاديمية والبحثية والإنتاج العلمي بكفاءة وانتظام، وتعد مشاركتهم في هذه الأنشطة أحد محكات تقييمهم.", ["faculty", "research"]),
          c("4-0-4", "تشارك هيئة التدريس في أنشطة الشراكة المجتمعية، وتعد مشاركتهم في هذه الأنشطة أحد محكات تقييمهم.", ["faculty"]),
          c("4-0-5", "يتلقى أعضاء هيئة التدريس برامج في التطوير المهني والأكاديمي، وفق خطة تلبي احتياجاتهم وتسهم في تطوير أدائهم.", ["faculty", "quality"]),
          c("4-0-6", "يقيم أداء هيئة التدريس بانتظام وفق معايير محددة ومعلنة، وتقدم التغذية الراجعة لهم، ويستفاد من النتائج في تحسين الأداء.", ["faculty", "quality"], true),
        ],
      },
    ],
  },
  {
    id: "s5",
    icon: Layers3,
    title: "مصادر التعلم والمرافق والتجهيزات",
    code: "المعيار الخامس",
    description: "كفاية المصادر والمرافق والتجهيزات والسلامة والتقنية والتقويم.",
    substandards: [
      {
        title: "5-0 مصادر التعلم والمرافق والتجهيزات",
        criteria: [
          c("5-0-1", "يتحقق البرنامج من كفاية ومناسبة مصادر التعلم والخدمات المقدمة بما يتناسب مع احتياجاته وأعداد الطلاب، ويتم تحديثها بصورة دورية.", ["resources"]),
          c("5-0-2", "يتوفر لهيئة التدريس والطلاب والموظفين في البرنامج التهيئة والدعم الفني المناسبين للاستخدام الفعال لمصادر ووسائل التعلم.", ["resources", "faculty", "students"]),
          c("5-0-3", "تطبق معايير السلامة والحفاظ على البيئة والتخلص من النفايات الخطرة بكفاءة وفاعلية، مع توفر جميع متطلبات الصحة والسلامة العامة والمهنية في المرافق والتجهيزات والأنشطة التعليمية والبحثية.", ["resources"], true),
          c("5-0-4", "يتوفر للبرنامج التقنيات والخدمات والبيئة المناسبة للمقررات التي تقدم إلكترونيًا أو عن بعد وفق المعايير الخاصة بها.", ["resources", "teaching"]),
          c("5-0-5", "يعمل البرنامج على تقويم فاعلية وكفاءة مصادر التعلم والمرافق والتجهيزات بأنواعها، ويستفاد من ذلك في التحسين.", ["resources", "quality"]),
        ],
      },
    ],
  },
  {
    id: "s6",
    icon: Microscope,
    title: "البحوث العلمية والمشاريع",
    code: "المعيار السادس",
    description: "النشاط البحثي والأولويات والبيئة البحثية والرسائل والمشاريع وأخلاقيات البحث.",
    substandards: [
      {
        title: "6-0 البحوث العلمية والمشاريع",
        criteria: [
          c("6-0-1", "يتابع البرنامج معدلات نشاطه البحثي وفق دوره في خطة البحث العلمي للمؤسسة، وفق مؤشرات أداء واضحة ومحددة، ويعمل على تطوير أدائه.", ["research", "quality"], true),
          c("6-0-2", "يحدد البرنامج الأولويات البحثية بما يتناسب مع رسالة المؤسسة والتوجهات الوطنية وخطط التنمية.", ["research"]),
          c("6-0-3", "يتوفر للبرنامج البيئة المحفزة والإمكانات المالية والتجهيزات التقنية والبحثية اللازمة لتنفيذ أنشطته البحثية.", ["research", "resources"]),
          c("6-0-4", "يطبق البرنامج آليات متنوعة لتنمية مهارات البحث العلمي والنشر لدى منسوبيه، وتبادل الخبرات ونتائج البحوث فيما بينهم، ويقوم تلك الآليات ويعمل على تطويرها وتحسينها.", ["research", "faculty", "quality"]),
          c("6-0-5", "يطبق البرنامج آليات متنوعة لتمويل أنشطته البحثية من الجهات المانحة وجهات الاستثمار.", ["research"]),
          c("6-0-6", "يطبق في البرنامج إجراءات أكاديمية وإدارية محددة وعادلة للموافقة على الرسائل العلمية والمشاريع البحثية في إطار زمني مناسب.", ["research", "ethics"]),
          c("6-0-7", "يتوفر لدى البرنامج أدلة إرشادية واضحة ومعلنة لإعداد وتقييم الرسائل العلمية والمشاريع.", ["research"]),
          c("6-0-8", "يطبق البرنامج آليات محددة لمتابعة فاعلية الإشراف العلمي على الرسائل والبحوث العلمية والمشاريع، ويتم تقويمها وتطويرها.", ["research", "quality"]),
          c("6-0-9", "يراقب البرنامج عدالة وموضوعية ومصداقية تقييم البحوث ومناقشة الرسائل العلمية وإجازتها.", ["research", "ethics"]),
          c("6-0-10", "يتحقق البرنامج من توفر الأصالة العلمية والإثراء المعرفي والابتكار في أنشطته البحثية بما يتناسب مع مستوى المؤهل والمعايير العالمية.", ["research"]),
          c("6-0-11", "يطبق البرنامج سياسات واضحة لأخلاقيات وضوابط البحث العلمي ويتابع التزام الباحثين بها وفق آليات مناسبة ويعمل على تطويرها.", ["research", "ethics"], true),
        ],
      },
    ],
  },
];

function c(code, text, themes, essential = false) {
  return { code, text, themes, essential };
}

function flattenCriteria() {
  return standards.flatMap((standard) =>
    standard.substandards.flatMap((sub) =>
      sub.criteria.map((criterion) => ({ standard, sub, criterion }))
    )
  );
}

function unique(items) {
  return [...new Set(items)];
}

function getCriterionSupport(criterion) {
  const evidences = unique(criterion.themes.flatMap((theme) => evidenceLibrary[theme]?.evidences || []));
  const tips = unique(criterion.themes.flatMap((theme) => evidenceLibrary[theme]?.tips || []));
  const themeLabels = criterion.themes.map((theme) => evidenceLibrary[theme]?.label).filter(Boolean);
  const mistakes = [
    "إرفاق شاهد عام لا يظهر صلته المباشرة بالمحك.",
    "رفع وثيقة غير معتمدة أو غير مؤرخة أو غير موقعة عند الحاجة.",
    "غياب تحليل النتائج أو عدم وجود أثر للتحسين.",
    "تعارض البيانات بين الدراسة الذاتية والتوصيفات والتقارير السنوية.",
  ];
  const checklist = [
    "هل الشاهد معتمد؟",
    "هل الشاهد حديث ومؤرخ؟",
    "هل تظهر علاقة الشاهد بالمحك مباشرة؟",
    "هل يوجد تحليل لا مجرد سرد؟",
    "هل توجد إجراءات تحسين ومتابعة؟",
  ];
  return { evidences, tips, mistakes, checklist, themeLabels };
}

function statusLabel(status) {
  if (status === "complete") return "مكتمل";
  if (status === "partial") return "جزئي";
  if (status === "missing") return "غير متوفر";
  return "غير مقيّم";
}

function statusWeight(status) {
  if (status === "complete") return 1;
  if (status === "partial") return 0.5;
  return 0;
}

function makeReport(selection, readiness) {
  const { standard, sub, criterion } = selection;
  const support = getCriterionSupport(criterion);
  return `${standard.code}: ${standard.title}\n${sub.title}\nالمحك: ${criterion.code}\n${criterion.text}\n\nحالة الجاهزية: ${statusLabel(readiness[criterion.code])}\n\nالأدلة والشواهد المقترحة:\n- ${support.evidences.join("\n- ")}\n\nنصائح تنفيذية:\n- ${support.tips.join("\n- ")}\n\nأخطاء شائعة:\n- ${support.mistakes.join("\n- ")}\n\nقائمة تحقق قبل الرفع:\n- ${support.checklist.join("\n- ")}`;
}

export default function SmartAccreditationEvidenceApp() {
  const allCriteria = useMemo(() => flattenCriteria(), []);
  const [selectedStandardId, setSelectedStandardId] = useState("s1");
  const [selectedCode, setSelectedCode] = useState("1-1-1");
  const [query, setQuery] = useState("");
  const [filter, setFilter] = useState("all");
  const [readiness, setReadiness] = useState({});
  const [copied, setCopied] = useState(false);

  const selectedStandard = standards.find((s) => s.id === selectedStandardId) || standards[0];
  const selected = allCriteria.find((item) => item.criterion.code === selectedCode) || allCriteria[0];
  const support = getCriterionSupport(selected.criterion);

  const filteredCriteria = useMemo(() => {
    const q = query.trim().toLowerCase();
    return allCriteria.filter(({ standard, sub, criterion }) => {
      const text = `${standard.code} ${standard.title} ${sub.title} ${criterion.code} ${criterion.text}`.toLowerCase();
      const matchesQuery = !q || text.includes(q);
      const matchesFilter = filter === "all" || (filter === "essential" && criterion.essential) || readiness[criterion.code] === filter;
      return matchesQuery && matchesFilter;
    });
  }, [allCriteria, query, filter, readiness]);

  const total = allCriteria.length;
  const essentialTotal = allCriteria.filter((x) => x.criterion.essential).length;
  const evaluated = allCriteria.filter((x) => readiness[x.criterion.code]).length;
  const score = Math.round((allCriteria.reduce((sum, x) => sum + statusWeight(readiness[x.criterion.code]), 0) / total) * 100);
  const complete = allCriteria.filter((x) => readiness[x.criterion.code] === "complete").length;
  const partial = allCriteria.filter((x) => readiness[x.criterion.code] === "partial").length;
  const missing = allCriteria.filter((x) => readiness[x.criterion.code] === "missing").length;

  const standardStats = selectedStandard.substandards.flatMap((sub) => sub.criteria);
  const standardScore = Math.round(
    (standardStats.reduce((sum, cr) => sum + statusWeight(readiness[cr.code]), 0) / standardStats.length) * 100
  );

  const handleCriterionClick = (item) => {
    setSelectedStandardId(item.standard.id);
    setSelectedCode(item.criterion.code);
  };

  const setStatus = (status) => {
    setReadiness((prev) => ({ ...prev, [selected.criterion.code]: status }));
  };

  const copyReport = async () => {
    await navigator.clipboard.writeText(makeReport(selected, readiness));
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  const downloadReport = () => {
    const text = makeReport(selected, readiness);
    const blob = new Blob([text], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `دليل-الشواهد-${selected.criterion.code}.txt`;
    a.click();
    URL.revokeObjectURL(url);
  };

  const generateGapReport = () => {
    const gaps = allCriteria
      .filter((item) => readiness[item.criterion.code] !== "complete")
      .map((item) => {
        const s = getCriterionSupport(item.criterion);
        return `${item.standard.code} - ${item.standard.title}\n${item.sub.title}\n${item.criterion.code}: ${item.criterion.text}\nالحالة: ${statusLabel(readiness[item.criterion.code])}\nأبرز الشواهد المطلوبة:\n- ${s.evidences.slice(0, 4).join("\n- ")}\n`;
      })
      .join("\n-----------------------------\n");

    const report = `تقرير فجوات الشواهد للاعتماد البرامجي\nنسبة الجاهزية الحالية: ${score}%\nالمحكات المقيمة: ${evaluated} من ${total}\nالمكتمل: ${complete}\nالجزئي: ${partial}\nغير المتوفر: ${missing}\n\n${gaps || "لا توجد فجوات مسجلة. جميع المحكات مكتملة."}`;
    const blob = new Blob([report], { type: "text/plain;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "تقرير-فجوات-الشواهد.txt";
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div dir="rtl" className="min-h-screen bg-slate-50 text-slate-950 font-sans">
      <div className="relative overflow-hidden bg-gradient-to-br from-teal-950 via-teal-800 to-emerald-600 text-white">
        <div className="absolute -top-24 -left-24 h-72 w-72 rounded-full bg-white/10 blur-3xl" />
        <div className="absolute bottom-0 right-1/3 h-40 w-40 rounded-full bg-cyan-300/20 blur-3xl" />
        <div className="mx-auto max-w-7xl px-5 py-8 md:py-10 relative">
          <div className="grid gap-6 lg:grid-cols-[1.6fr_.9fr] lg:items-center">
            <motion.div initial={{ opacity: 0, y: 14 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.5 }}>
              <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-white/20 bg-white/10 px-4 py-2 text-sm text-teal-50 backdrop-blur">
                <Sparkles className="h-4 w-4" />
                نموذج احترافي قابل للعرض والتطوير المؤسسي
              </div>
              <h1 className="text-3xl font-black tracking-tight md:text-5xl">
                دليل الشواهد الذكي للاعتماد البرامجي
              </h1>
              <p className="mt-4 max-w-3xl text-base leading-8 text-teal-50 md:text-lg">
                منصة مساعدة للبرامج الأكاديمية في الجامعة الإسلامية؛ تربط كل معيار ومحك بالشواهد المقترحة، والتنبيهات التنفيذية، وقياس الجاهزية، وتوليد تقارير فجوات الشواهد.
              </p>
              <div className="mt-5 flex flex-wrap gap-3">
                <Button className="rounded-2xl bg-white px-5 py-5 text-teal-900 hover:bg-teal-50" onClick={generateGapReport}>
                  <Download className="ml-2 h-4 w-4" />
                  تحميل تقرير الفجوات
                </Button>
                <Button variant="outline" className="rounded-2xl border-white/30 bg-white/10 px-5 py-5 text-white hover:bg-white/20">
                  <ShieldCheck className="ml-2 h-4 w-4" />
                  جاهزية البرنامج: {score}%
                </Button>
              </div>
            </motion.div>

            <motion.div initial={{ opacity: 0, scale: 0.96 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 0.45, delay: 0.1 }}>
              <Card className="rounded-3xl border-white/20 bg-white/10 text-white shadow-2xl backdrop-blur">
                <CardContent className="p-6">
                  <div className="flex items-center justify-between gap-4">
                    <div>
                      <p className="text-sm text-teal-50">المؤشر العام</p>
                      <div className="mt-1 text-5xl font-black">{score}%</div>
                    </div>
                    <div className="rounded-3xl bg-white/15 p-4">
                      <BarChart3 className="h-10 w-10" />
                    </div>
                  </div>
                  <div className="mt-5 h-3 rounded-full bg-white/20">
                    <div className="h-3 rounded-full bg-white" style={{ width: `${score}%` }} />
                  </div>
                  <div className="mt-5 grid grid-cols-3 gap-3 text-center text-sm">
                    <div className="rounded-2xl bg-white/10 p-3">
                      <div className="text-xl font-bold">{complete}</div>
                      <div className="text-teal-50">مكتمل</div>
                    </div>
                    <div className="rounded-2xl bg-white/10 p-3">
                      <div className="text-xl font-bold">{partial}</div>
                      <div className="text-teal-50">جزئي</div>
                    </div>
                    <div className="rounded-2xl bg-white/10 p-3">
                      <div className="text-xl font-bold">{missing}</div>
                      <div className="text-teal-50">غير متوفر</div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          </div>
        </div>
      </div>

      <main className="mx-auto grid max-w-7xl gap-5 px-5 py-6 lg:grid-cols-[310px_1fr]">
        <aside className="space-y-4 lg:sticky lg:top-5 lg:self-start">
          <Card className="rounded-3xl border-slate-200 shadow-sm">
            <CardContent className="p-4">
              <div className="relative">
                <Search className="absolute right-3 top-3.5 h-4 w-4 text-slate-400" />
                <input
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="ابحث برقم المحك أو كلمة..."
                  className="w-full rounded-2xl border border-slate-200 bg-white py-3 pr-10 pl-4 text-sm outline-none transition focus:border-teal-500 focus:ring-4 focus:ring-teal-100"
                />
              </div>
              <div className="mt-3 flex items-center gap-2">
                <Filter className="h-4 w-4 text-slate-500" />
                <select
                  value={filter}
                  onChange={(e) => setFilter(e.target.value)}
                  className="w-full rounded-2xl border border-slate-200 bg-white px-3 py-2 text-sm outline-none focus:border-teal-500"
                >
                  <option value="all">كل المحكات</option>
                  <option value="essential">المحكات الأساسية فقط</option>
                  <option value="complete">المكتملة</option>
                  <option value="partial">الجزئية</option>
                  <option value="missing">غير المتوفرة</option>
                </select>
              </div>
            </CardContent>
          </Card>

          <Card className="rounded-3xl border-slate-200 shadow-sm">
            <CardContent className="p-3">
              <div className="mb-2 px-2 text-sm font-bold text-slate-600">المعايير</div>
              <div className="space-y-2">
                {standards.map((standard) => {
                  const Icon = standard.icon;
                  const count = standard.substandards.reduce((s, sub) => s + sub.criteria.length, 0);
                  const active = selectedStandardId === standard.id;
                  return (
                    <button
                      key={standard.id}
                      onClick={() => {
                        setSelectedStandardId(standard.id);
                        const first = standard.substandards[0].criteria[0];
                        setSelectedCode(first.code);
                      }}
                      className={`w-full rounded-2xl border p-3 text-right transition ${
                        active ? "border-teal-500 bg-teal-50 text-teal-950 shadow-sm" : "border-slate-200 bg-white hover:border-teal-300 hover:bg-slate-50"
                      }`}
                    >
                      <div className="flex items-start gap-3">
                        <div className={`rounded-2xl p-2 ${active ? "bg-teal-600 text-white" : "bg-slate-100 text-slate-600"}`}>
                          <Icon className="h-5 w-5" />
                        </div>
                        <div className="min-w-0 flex-1">
                          <div className="text-xs text-slate-500">{standard.code}</div>
                          <div className="text-sm font-extrabold leading-6">{standard.title}</div>
                          <div className="mt-1 text-xs text-slate-500">{count} محك</div>
                        </div>
                      </div>
                    </button>
                  );
                })}
              </div>
            </CardContent>
          </Card>
        </aside>

        <section className="space-y-5">
          <div className="grid gap-4 md:grid-cols-4">
            <StatCard icon={ClipboardCheck} label="إجمالي المحكات" value={total} />
            <StatCard icon={ShieldCheck} label="المحكات الأساسية" value={essentialTotal} />
            <StatCard icon={Settings2} label="المحكات المقيمة" value={evaluated} />
            <StatCard icon={BarChart3} label="جاهزية المعيار الحالي" value={`${standardScore}%`} />
          </div>

          {query ? (
            <Card className="rounded-3xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <div className="mb-4 flex items-center justify-between gap-3">
                  <div>
                    <h2 className="text-xl font-black">نتائج البحث</h2>
                    <p className="text-sm text-slate-500">عدد النتائج: {filteredCriteria.length}</p>
                  </div>
                </div>
                <div className="grid gap-3 md:grid-cols-2">
                  {filteredCriteria.map((item) => (
                    <CriterionButton key={item.criterion.code} item={item} active={selectedCode === item.criterion.code} readiness={readiness} onClick={() => handleCriterionClick(item)} />
                  ))}
                </div>
              </CardContent>
            </Card>
          ) : (
            <Card className="rounded-3xl border-slate-200 shadow-sm">
              <CardContent className="p-5">
                <div className="mb-5 flex flex-col gap-2 md:flex-row md:items-end md:justify-between">
                  <div>
                    <p className="text-sm font-bold text-teal-700">{selectedStandard.code}</p>
                    <h2 className="text-2xl font-black">{selectedStandard.title}</h2>
                    <p className="mt-1 text-sm leading-7 text-slate-500">{selectedStandard.description}</p>
                  </div>
                  <div className="rounded-2xl border border-teal-100 bg-teal-50 px-4 py-2 text-sm font-bold text-teal-800">
                    جاهزية هذا المعيار: {standardScore}%
                  </div>
                </div>

                <div className="space-y-4">
                  {selectedStandard.substandards.map((sub) => (
                    <div key={sub.title} className="rounded-3xl border border-slate-200 bg-slate-50 p-4">
                      <div className="mb-3 flex items-center justify-between gap-3">
                        <h3 className="font-black">{sub.title}</h3>
                        <span className="rounded-full bg-white px-3 py-1 text-xs font-bold text-slate-500 shadow-sm">{sub.criteria.length} محك</span>
                      </div>
                      <div className="grid gap-3 md:grid-cols-2">
                        {sub.criteria.map((criterion) => {
                          const item = { standard: selectedStandard, sub, criterion };
                          if (filter === "essential" && !criterion.essential) return null;
                          if (["complete", "partial", "missing"].includes(filter) && readiness[criterion.code] !== filter) return null;
                          return (
                            <CriterionButton key={criterion.code} item={item} active={selectedCode === criterion.code} readiness={readiness} onClick={() => handleCriterionClick(item)} />
                          );
                        })}
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          <AnimatePresence mode="wait">
            <motion.div
              key={selected.criterion.code}
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.25 }}
            >
              <Card className="rounded-3xl border-teal-100 bg-white shadow-sm">
                <CardContent className="p-5 md:p-6">
                  <div className="flex flex-col gap-4 md:flex-row md:items-start md:justify-between">
                    <div>
                      <div className="mb-3 flex flex-wrap items-center gap-2">
                        <span className="rounded-full bg-teal-100 px-3 py-1 text-sm font-black text-teal-800">{selected.criterion.code}</span>
                        {selected.criterion.essential && <span className="rounded-full bg-red-50 px-3 py-1 text-sm font-black text-red-700">محك أساسي</span>}
                        <span className="rounded-full bg-slate-100 px-3 py-1 text-sm font-bold text-slate-600">{statusLabel(readiness[selected.criterion.code])}</span>
                      </div>
                      <h2 className="text-xl font-black leading-9 md:text-2xl">{selected.criterion.text}</h2>
                      <p className="mt-2 text-sm text-slate-500">{selected.standard.code} — {selected.standard.title} / {selected.sub.title}</p>
                    </div>
                    <div className="flex flex-wrap gap-2">
                      <Button onClick={copyReport} className="rounded-2xl bg-teal-700 hover:bg-teal-800">
                        <Copy className="ml-2 h-4 w-4" />
                        {copied ? "تم النسخ" : "نسخ التقرير"}
                      </Button>
                      <Button onClick={downloadReport} variant="outline" className="rounded-2xl">
                        <Download className="ml-2 h-4 w-4" />
                        تحميل
                      </Button>
                    </div>
                  </div>

                  <div className="mt-5 grid gap-3 md:grid-cols-3">
                    <StatusButton label="مكتمل" icon={CheckCircle2} active={readiness[selected.criterion.code] === "complete"} onClick={() => setStatus("complete")} tone="green" />
                    <StatusButton label="جزئي" icon={AlertTriangle} active={readiness[selected.criterion.code] === "partial"} onClick={() => setStatus("partial")} tone="amber" />
                    <StatusButton label="غير متوفر" icon={AlertTriangle} active={readiness[selected.criterion.code] === "missing"} onClick={() => setStatus("missing")} tone="red" />
                  </div>

                  <div className="mt-5 flex flex-wrap gap-2">
                    {support.themeLabels.map((label) => (
                      <span key={label} className="rounded-full border border-teal-100 bg-teal-50 px-3 py-1 text-xs font-bold text-teal-700">
                        {label}
                      </span>
                    ))}
                  </div>

                  <div className="mt-6 grid gap-4 lg:grid-cols-2">
                    <InfoBox title="الأدلة والشواهد المقترحة" icon={FileText} items={support.evidences} />
                    <InfoBox title="نصائح تنفيذية" icon={Sparkles} items={support.tips} />
                    <InfoBox title="أخطاء شائعة" icon={AlertTriangle} items={support.mistakes} />
                    <InfoBox title="قائمة تحقق قبل رفع الشاهد" icon={ClipboardCheck} items={support.checklist} />
                  </div>

                  <div className="mt-5 rounded-3xl border border-amber-200 bg-amber-50 p-4 text-sm leading-8 text-amber-900">
                    <strong>تنبيه مراجع جودة:</strong> الشاهد القوي ليس الملف الأكثر عددًا، بل الملف الأوضح صلة بالمحك، والأثبت اعتمادًا، والأقدر على إظهار التحليل والتحسين. كثرة المرفقات بلا صلة مثل كثرة المفاتيح في جيب لا يفتح بابًا.
                  </div>
                </CardContent>
              </Card>
            </motion.div>
          </AnimatePresence>
        </section>
      </main>
    </div>
  );
}

function StatCard({ icon: Icon, label, value }) {
  return (
    <Card className="rounded-3xl border-slate-200 shadow-sm">
      <CardContent className="flex items-center gap-3 p-4">
        <div className="rounded-2xl bg-teal-50 p-3 text-teal-700">
          <Icon className="h-5 w-5" />
        </div>
        <div>
          <div className="text-2xl font-black">{value}</div>
          <div className="text-xs font-bold text-slate-500">{label}</div>
        </div>
      </CardContent>
    </Card>
  );
}

function CriterionButton({ item, active, readiness, onClick }) {
  const { criterion, standard } = item;
  const status = readiness[criterion.code];
  const badgeClass =
    status === "complete"
      ? "bg-emerald-50 text-emerald-700 border-emerald-100"
      : status === "partial"
      ? "bg-amber-50 text-amber-700 border-amber-100"
      : status === "missing"
      ? "bg-red-50 text-red-700 border-red-100"
      : "bg-slate-50 text-slate-500 border-slate-100";

  return (
    <button
      onClick={onClick}
      className={`rounded-3xl border p-4 text-right transition hover:-translate-y-0.5 hover:shadow-sm ${
        active ? "border-teal-500 bg-teal-50" : "border-slate-200 bg-white hover:border-teal-200"
      }`}
    >
      <div className="mb-2 flex flex-wrap items-center gap-2">
        <span className="rounded-full bg-teal-100 px-3 py-1 text-sm font-black text-teal-800">{criterion.code}</span>
        {criterion.essential && <span className="rounded-full bg-red-50 px-3 py-1 text-xs font-black text-red-700">أساسي</span>}
        <span className={`rounded-full border px-3 py-1 text-xs font-bold ${badgeClass}`}>{statusLabel(status)}</span>
      </div>
      <p className="text-sm font-bold leading-7 text-slate-800">{criterion.text}</p>
      <p className="mt-2 text-xs text-slate-400">{standard.code}</p>
    </button>
  );
}

function StatusButton({ label, icon: Icon, active, onClick, tone }) {
  const palette = {
    green: active ? "border-emerald-500 bg-emerald-50 text-emerald-800" : "border-slate-200 bg-white text-slate-600 hover:bg-emerald-50",
    amber: active ? "border-amber-500 bg-amber-50 text-amber-800" : "border-slate-200 bg-white text-slate-600 hover:bg-amber-50",
    red: active ? "border-red-500 bg-red-50 text-red-800" : "border-slate-200 bg-white text-slate-600 hover:bg-red-50",
  };
  return (
    <button onClick={onClick} className={`flex items-center justify-center gap-2 rounded-2xl border px-4 py-3 text-sm font-black transition ${palette[tone]}`}>
      <Icon className="h-4 w-4" />
      {label}
    </button>
  );
}

function InfoBox({ title, icon: Icon, items }) {
  return (
    <div className="rounded-3xl border border-slate-200 bg-slate-50 p-5">
      <div className="mb-3 flex items-center gap-2">
        <div className="rounded-2xl bg-white p-2 text-teal-700 shadow-sm">
          <Icon className="h-5 w-5" />
        </div>
        <h3 className="font-black">{title}</h3>
      </div>
      <ul className="space-y-2 pr-5 text-sm leading-7 text-slate-700">
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </div>
  );
}
