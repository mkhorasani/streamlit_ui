import streamlit as st
import pandas as pd

st.title('Data Explorer')
st.sidebar.subheader('Upload a file')

uploaded_file = st.sidebar.file_uploader("Upload a file")

if uploaded_file is not None:  
	df = pd.read_csv(uploaded_file)
	st.sidebar.info('File successfully uploaded')

	col1, col2 = st.beta_columns(2)

	with col1:
		st.subheader('Raw dataframe')
		st.write(df)

		st.subheader('Select columns')
		columns = list(df.columns)
		columns_sel = st.multiselect('Select columns',columns,columns)
		df = df[columns_sel]
		st.write(df)

	with col2:
		st.subheader('Select rows')
		start, stop = st.slider('Rows',0,len(df)-1,[0,len(df)-1],1)
		df = df.iloc[start:stop]
		st.write(df)

		st.subheader('Visualize data')
		value = st.radio('Value',columns_sel)
		df = df[value]
		st.line_chart(df)