from random import randint
import time
import streamlit as st
from PIL import Image
image = Image.open('1.jpg')
st.image(image)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
option = st.selectbox(
     'ESCOLHA:',
     ('PEDRA', 'PAPEL', 'TESOURA'))

st.write('Você escolheu:', option)
time.sleep(3)
st.text('JO')
time.sleep(1)
st.text('KEN')
time.sleep(1)
st.text('PO!!!')
time.sleep(1)

if pc == 0:
    if option == 'PEDRA':
        st.info('EMPATE!')
    elif option == 'PAPEL':
        st.success('VOCÊ VENCEU!')
        st.balloons()
    elif option == 'TESOURA':
        st.error('COMPUTADOR VENCEU!')
    else:
        st.warning('JOGADA INVÁLIDA!')

elif pc == 1:
    if option == 'PEDRA':
        st.error('COMPUTADOR VENCEU!')
    elif option == 'PAPEL':
        st.info('EMPATE')
    elif option == 'TESOURA':
        st.success('VOCÊ VENCEU!')
        st.balloons()
    else:
        st.warning('JOGADA INVÁLIDA!')

elif pc == 2:
    if option == 'PEDRA':
        st.success('VOCÊ VENCEU!')
        st.balloons()
    elif option == 'PAPEL':
        st.error('COMPUTADOR VENCEU!')
    elif option == 'TESOURA':
        st.info('EMPATE')
    else:
        st.warning('JOGADA INVÁLIDA!')
          
st.text('-=' * 15)
st.text('O computador escolheu {}'.format(itens[pc]))
st.text('-=' * 15)
