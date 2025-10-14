import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tempo = st.sidebar.slider("Tempo", 0, 100)

t = np.linspace(0,tempo,1000)
T = 20+80*(1-np.exp(-0.1*t))

AQ = {'Tempo (min)':t,
        'Temperatura (oC)':T}
aq = pd.DataFrame(AQ)

st.line_chart(aq,x = 'Tempo (min)', y = 'Temperatura (oC)')

