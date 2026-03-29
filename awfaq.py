import streamlit as st
import numpy as np

# --- 1. القوالب الثابتة المستخرجة من الصور ---

def get_preset_template(n):
    """
    إرجاع مصفوفة سير الأعداد بناءً على الصور المرفقة (التسكين اليدوي).
    """
    if n == 3: # المثلث
        return np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    elif n == 4: # المربع
        return np.array([[16, 2, 3, 13], [5, 11, 10, 8], [9, 7, 6, 12], [4, 14, 15, 1]])
    elif n == 5: # المخمس
        return np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]])
    elif n == 6: # المسدس (بناءً على صورة المسدس قبل الجبر)
        return np.array([[35, 1, 6, 26, 19, 24], [3, 32, 7, 21, 23, 25], [31, 9, 2, 22, 27, 20], [8, 28, 33, 17, 10, 15], [30, 5, 34, 12, 14, 16], [4, 36, 29, 13, 18, 11]])
    elif n == 7: # المسبع (بناءً على الصورة الملونة)
        return np.array([[22, 31, 40, 49, 2, 11, 20], [30, 39, 48, 1, 10, 19, 28], [38, 47, 7, 9, 18, 27, 29], [46, 6, 8, 17, 26, 35, 37], [5, 14, 16, 25, 34, 36, 45], [13, 15, 24, 33, 42, 44, 4], [21, 23, 32, 41, 43, 3, 12]])
    elif n == 8: # المثمن (بناءً على الصورة البنفسجية)
        return np.array([[39, 47, 22, 30, 60, 52, 9, 1], [55, 63, 6, 14, 44, 36, 25, 17], [28, 20, 41, 33, 7, 15, 54, 62], [12, 4, 57, 49, 23, 31, 38, 46], [5, 13, 56, 64, 26, 18, 43, 35], [21, 29, 40, 48, 10, 2, 59, 51], [58, 50, 11, 3, 37, 45, 24, 32], [42, 34, 27, 19, 53, 61, 8, 16]])
    elif n == 9: # المتسع (بناءً على الصورة الخضراء)
        return np.array([[10, 78, 35, 26, 55, 42, 6, 71, 46], [50, 7, 66, 30, 14, 79, 43, 21, 59], [63, 38, 22, 67, 54, 2, 74, 31, 18], [64, 51, 8, 80, 28, 15, 60, 44, 19], [23, 61, 39, 3, 68, 52, 16, 75, 32], [36, 11, 76, 40, 27, 56, 47, 4, 72], [37, 24, 62, 53, 1, 69, 33, 17, 73], [77, 34, 12, 57, 41, 25, 70, 48, 5], [9, 65, 49, 13, 81, 29, 20, 58, 45]])
    elif n == 10: # المعشر (بناءً على الصورة الصفراء)
        return np.array([[100, 89, 79, 65, 53, 46, 33, 27, 12, 1], [82, 22, 68, 47, 10, 91, 58, 32, 76, 19], [77, 34, 43, 7, 11, 90, 92, 56, 69, 26], [39, 41, 2, 14, 78, 25, 88, 94, 60, 64], [44, 9, 13, 80, 66, 36, 21, 86, 95, 55], [6, 17, 30, 35, 42, 59, 67, 71, 85, 93], [57, 97, 81, 23, 38, 63, 75, 20, 3, 48], [61, 52, 98, 84, 28, 73, 16, 8, 45, 40], [24, 70, 54, 99, 83, 18, 5, 49, 31, 72], [15, 74, 37, 51, 96, 4, 50, 62, 29, 87]])
    return np.zeros((n, n))

# --- 2. محرك الجمل والأرقام العربية ---

def to_arabic_numerals(number):
    arabic_digits = "٠١٢٣٤٥٦٧٨٩"
    return "".join(arabic_digits[int(d)] for d in str(number))

def calculate_jamal(text):
    jamal_table = {'أ': 1, 'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000}
    text = text.replace('ة', 'ه').replace('ى', 'ي').replace('إ', 'أ').replace('آ', 'ا')
    return sum(jamal_table.get(char, 0) for char in text)

# --- 3. محرك الجبر المتسلسل ---

def apply_preset_jabr(n, target):
    base = get_preset_template(n)
    standard_sum = np.sum(base[0])
    if target < standard_sum: return None, standard_sum
    
    diff = target - standard_sum
    quotient = diff // n
    remainder = diff % n
    
    final_sq = base + quotient
    flat = final_sq.flatten()
    start_index = (n * n) - n # نقطة البداية للجبر المتسلسل
    
    for r in range(remainder):
        if (start_index + r) < len(flat):
            flat[start_index + r] += 1
            
    return flat.reshape(n, n), standard_sum

# --- 4. واجهة الموقع ---

st.set_page_config(page_title="المولد التام للأوفاق", layout="wide")
st.markdown("<style>.magic-cell { border: 2px solid #8b4513; background: #fffcf0; color: #1a1a1a; font-size: 20px; font-weight: bold; text-align: center; padding: 10px; border-radius: 4px; }</style>", unsafe_allow_html=True)

st.title("🛡️ نظام توليد الأوفاق (المثلث - المعشر)")

user_sentence = st.text_input("أدخل الجملة المراد حساب جملها وتوليد وفقها:", value="يا فتاح")
jamal_val = calculate_jamal(user_sentence)

if user_sentence:
    st.info(f"قيمة الجملة: {to_arabic_numerals(jamal_val)} ({jamal_val})")

with st.sidebar:
    st.header("⚙️ الإعدادات")
    n = st.selectbox("اختر الوفق:", list(range(3, 11)), format_func=lambda x: f"وفق {x}x{x}")
    st.write("التسكين يعتمد على القوالب اليدوية المرفوعة.")

if st.button("تسكين الوفق"):
    result, min_val = apply_preset_jabr(n, jamal_val)
    if result is None:
        st.error(f"⚠️ العدد صغير! وفق {n}x{n} يحتاج لمجموع لا يقل عن {to_arabic_numerals(min_val)}")
    else:
        st.success(f"✅ تم التسكين لمجموع: {to_arabic_numerals(jamal_val)}")
        for row in result:
            cols = st.columns(n)
            for idx, val in enumerate(row):
                cols[idx].markdown(f"<div class='magic-cell'>{to_arabic_numerals(val)}</div>", unsafe_allow_html=True)
