'''
OVERVIEW OF APP:
    - Upload multichannel song (look into file support)
    - View all channels at once, give option of viewing individual channels
    - Heirarchy of viewing
        - Waveform
        - FFT/FCT Spectrum
        - Spectrogram
        - MFCCs
    - Various snippet lengths with sliders (might be computationally expensive)
    - Use uploaded song for source separation? (Look into later)
'''

import streamlit as st
import pandas as pd
import numpy as np
st.title('Title!')

df = pd.DataFrame({
    'Col 1': [2,3,3,4],
    'Col 2': [3,3,32,5]
    })

# Can output when called. 
'This is a dataframe!'
df

