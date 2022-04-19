import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('/home/felipelx/Documents/consulting/logo_brand.png')

st.image(image, use_column_width=True)

st.write(""""
# DNA count Web App
""")

# input text box
st.header('Enter DNA sequence')

sequence_input = '>DNA query\ntgagcatagcgccattcggaatatccttatcattctttgttaaaagtgatcactattgta\nacccctatacggtaagccatttgagaaggatgcagtacccttaaatatctctcagtgcag\nttggaccgcgagactgaacgtgctccgcgtggccctccaactgctcctgggatgtctagacttgccgcacgcactcgaaacatacatcgaagattggaatcgaacttttaccccgtgact'

sequence = st.text_area('Sequence input: ', sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence).upper()

st.write("""
*
""")

st.header('Input (DNA query)')

# nucleotide count
st.header('OUTPUT (Nucleotide count)')

st.subheader('Print dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', str(seq).count('A')),
        ('T', str(seq).count('T')),
        ('G', str(seq).count('G')),
        ('C', str(seq).count('C'))
    ])
    return d

X = DNA_nucleotide_count(sequence)

X_label = list(X)
X_value = list(X.values())

# display text with the count
st.subheader('Print Text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

# display dataframe
st.subheader('Print Dataframe')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'Count'}, axis='columns')
df.reset_index(level=0, inplace=True)
df = df.rename(columns={'index': 'Nucleotide'})
st.write(df)

# display barchart
st.subheader('Print Bar Chart')
dnaBarChart = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count'
)

dnaBarChart = dnaBarChart.properties(width=500, height=300)
st.write(dnaBarChart)