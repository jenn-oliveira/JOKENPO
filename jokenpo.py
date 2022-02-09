from random import randint
import time
import streamlit as st

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
st.text('''ESCOLHA:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
j1 = st.number_input('Sua escolha: ')
st.spinner('JO')
time.sleep(1)
st.spinner('KEN')
time.sleep(1)
st.spinner('PO!!!')
time.sleep(1)
st.text('-=' * 15)
st.text('O computador escolheu {}'.format(itens[pc]))
st.text('Você escolheu {}'.format(itens[j1]))
st.text('-=' * 15)
if pc == 0:
    if j1 == 0:
        st.info('EMPATE!')
    elif j1 == 1:
        st.success('VOCÊ VENCEU!')
        st.balloons()
    elif j1 == 2:
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
