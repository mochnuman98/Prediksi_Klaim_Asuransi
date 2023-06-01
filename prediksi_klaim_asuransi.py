import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('insurance3r2.sav', 'rb'))

st.title('Prediksi Klaim Asuransi')
col1, col2 = st.columns(2)

with col1:
    age = st.number_input('Input Usia Peserta Asuransi')
    sex = st.number_input('Input Jenis Kelamin Peserta Wanita = 0, Laki-laki=1')
    bmi = st.number_input('Input Berat Badan Ideal Peserta')
    steps = st.number_input('Input Rata-rata Berjalan Per Hari')

with col2:
    children = st.number_input('Input Jumlah Anak/tanggunngan pemegang polis')
    smoker = st.number_input('Input Apakah Peserta Asuransi Merokok Tidak Merokok =0, Merokok=1')
    region = st.number_input('Input Area Tempat Tinggal Peserta Asuransi di AS northeast=0, northwest=1, southeast=2, southwest=3')
    charges = st.number_input('Input Biaya Medis Individu Yang Ditagih Oleh asuransi kesehatan')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[age,sex, bmi, steps, children, smoker, region, charges]])

    if(predik[0] == 1):
        predik = 'Peserta Melakukan Klaim Asuransi'
    else:
        predik = 'Peserta Tidak Melakukan Klaim Asuransi'
st.success(predik)