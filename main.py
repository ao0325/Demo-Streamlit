import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここが右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせの回答')

# st.write('DataFrame')

# df = pd.DataFrame(
#     np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon'],
# )

# # st.line_chart(df)
# st.map(df)

# st.write(df)
# st.dataframe(df)

# st.write('Display Image')

# img = Image.open('019.jpg')

# st.image(img, caption='019.jpg', use_column_width=True)
