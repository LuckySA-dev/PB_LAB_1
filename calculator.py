import streamlit as st

if 'num2_error' not in st.session_state:
    st.session_state.num2_error = False

def get_number_input(label, key):
    initial_value = st.session_state.get(key, 0.0)
    return st.number_input(label, value=initial_value, step=0.1, format="%.2f",key=key)

def get_operator_input(label):
    valid_operators = ['+', '-', '*', '/', '%']
    return st.selectbox(label, valid_operators, key="operator_input")

def calculate(num1, num2, operator):
    if operator in ('/', '%') and num2 == 0:
        return None

    #copy โค้ดฟังก์ชั่น calculate มาใส่
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2

st.title('My Calculator')

# Get inputs from the user
num1 = get_number_input("ป้อนตัวเลขแรก:", key="num1_input")
operator = get_operator_input("เลือกตัวดำเนินการ:")

if operator not in ("/","%"):
    num2 = get_number_input("ป้อนตัวเลขที่สอง:", key="num2_input")
    st.session_state.num2_error = False
else:
    num2 = get_number_input("ป้อนตัวเลขที่สอง:", key="num2_input")

    if num2 == 0:
        st.session_state.num2_error = True
        st.error("ข้อผิดพลาด: ไม่สามารถหารด้วยศูนย์ได้ กรุณาเปลี่ยนตัวเลขที่สอง")
    else:
        st.session_state.num2_error = False

# Perform calculation when the button is clicked
if st.button('คำนวณ', disabled=st.session_state.num2_error):
    result = calculate(num1, num2, operator)
    if result is not None:
        st.success(f"ผลลัพธ์: {num1} {operator} {num2} = ***{result:.2f}***")
    elif st.session_state.num2_error:
        pass
