import numpy as np
import pandas as pd
import streamlit as st
import pickle
from rdkit import Chem
from rdkit.Chem import Descriptors

def AromaticProportion(m):
    aromatic_atoms = [m.GetAtomWithIdx(i).GetIsAromatic() for i in range(m.GetNumAtoms())]
    aa_count = []
    for i in aromatic_atoms:
        if i == True:
            aa_count.append(1)
        else:
            aa_count.append(0)
    AromaticAtom = sum(aa_count)
    Heavy_Atom = Descriptors.HeavyAtomCount(m)
    AR = AromaticAtom/Heavy_Atom
    return AR

def generate(smiles, verbose=False):
    moldata = []
    for elem in smiles:
        m = Chem.MolFromSmiles(elem)
        moldata.append(m)

    baseData = np.arange(1,1)
    i=0
    for mol in moldata:
        descMolLogP = Descriptors.MolLogP(mol)
        descMolWt = Descriptors.MolWt(mol)
        descNumRotableBonds = Descriptors.NumRotatableBonds(mol)
        descAromaticProportion = AromaticProportion(mol)

        row = np.array([descMolLogP, descMolWt, descNumRotableBonds, descAromaticProportion])

        if(i==0):
            baseData = row
        else:
            baseData = np.vstack((baseData, row))
        i=i+1
    columnName = ['MolLogP', 'MolWt', 'NumRotableBonds', 'AromaticProportion']
    descriptors = pd.DataFrame(data=baseData, columns=columnName)

    return descriptors


# input molecules
st.sidebar.header('User Input Features')

Smiles_input = 'CCCCC\nCCC\nCN'
Smiles = st.sidebar.text_area('Smiles Input', Smiles_input)
Smiles = 'C\n' + Smiles
Smiles = Smiles.split('\n')

st.header('Input Smiles')
Smiles[1:]

# calculate molecular description
st.header('Computed molecular description')
X = generate(Smiles)
X[1:]

# prebuilt model
load_model = pickle.load(open('solubility_model.pkl', 'rb'))

# apply model to make prediction
prediction = load_model.predict(X)

st.header('Predict LogS values')
prediction[1:]