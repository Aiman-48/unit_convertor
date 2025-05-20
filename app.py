import streamlit as st
def convert_units(value: float, unit_from: str, unit_to: str): # def means define func
   # print("value", value)
   # print("unit from", unit_from)
   # print("unit to", unit_to)

    # 1km = 1000 m
    # 1m = 0.001km
    #1kg = 1000 gm
    # 1 gm = 0.001 kg

    if unit_from == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "conversion is not supported"

# result = convert_units(3,"kilometers","meters")
# print("the value in meter is:", result)
# result2 = convert_units(5,"grams","kilograms")
# print("the value in kilogram is:", result2)

def main():

    st.title("unit converter")
    st.write("welcome to unit converter")
    value = st.number_input("enter the value you want to convert:", min_value=0.0)
    unit_from = st.text_input("enter the value you want to convert from eg:meters grams kilograms kilometers:")
    unit_to = st.text_input("enter the value you want conversion eg:meters grams kilograms kilometers:")

    if st.button("convert"):
       result = convert_units(value, unit_from, unit_to)
       st.write("converted values is:", result)

#     print("value", value)
#     print("unit-from",unit_from)
#     print("unit-to",unit_to)
#     result = convert_units(value, unit_from, unit_to)
#     print("converted values is:", result)

main()    
