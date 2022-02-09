from random import randint
import time
import streamlit as st

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
option = st.selectbox(
     'ESCOLHA:',
     ('PEDRA', 'PAPEL', 'TESOURA'))

st.write('Você escolheu:', option)
st.text('JO')
time.sleep(1)
st.text('KEN')
time.sleep(1)
st.text('PO!!!')
time.sleep(1)
st.text('-=' * 15)
st.text('O computador escolheu {}'.format(itens[pc]))
st.text('-=' * 15)
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
    if j1 == 0:
        st.error('COMPUTADOR VENCEU!')
    elif j1 == 1:
        st.info('EMPATE')
    elif j1 == 2:
        st.success('VOCÊ VENCEU!')
        st.balloons()
    else:
        st.warning('JOGADA INVÁLIDA!')

elif pc == 2:
    if j1 == 0:
        st.success('VOCÊ VENCEU!')
    elif j1 == 1:
        st.error('COMPUTADOR VENCEU!')
    elif j1 == 2:
        st.info('EMPATE')
    else:
        st.warning('JOGADA INVÁLIDA!')
