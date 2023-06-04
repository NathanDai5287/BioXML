import streamlit as st

from model import Model
model = Model()

# multi-page app

# title
st.title('Raven AI')

# text input with label
sequence = st.text_input('Enter Amino Acid Sequence')

# submit button
if st.button('Submit'):
	# run model
	locations = model.fit(sequence)
	# display results
	st.write(locations)
