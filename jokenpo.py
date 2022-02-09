from random import randint
import time
import streamlit as st

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
st.text('''ESCOLHA:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j1 = st.text_input('Sua escolha: ')
st.text('Você escolheu ", j1)
