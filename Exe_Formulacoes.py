import streamlit as st
import pandas as pd
import numpy as np

st.title('Trabalhando com Abas')

aba1, aba2, aba3, aba4, aba5 = st.tabs(['Plano Inclinado',
                            'Meia Vida',
                            'Lançamento Obriquo',
                            'Colisões',
                            'Sen, Cos, Tg'])

with aba1:
    st.header('Decomposição de forças no plano inclinado')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Contantes')
        g = 9.8
        st.metric(label = 'Aceleração da gravidade',
                  value = f'{g} m/s²')

        ang = st.slider('Angulo (°)',0,90) #graus
        st.metric(label = '''Inclinação $\Theta$''',
                  value = f'{ang}°')
        m = st.slider('Massa (g)',0,100) #gramas
        st.metric(label = 'Massa', value = f'{m}g')
        
    with col2:
        p = m*g
        st.metric(label = 'Força peso', value = f'P={p}N')
        st.write('Decomposição da força Peso')
        px = np.round(p*np.sin(ang*np.pi/180),2)
        py = np.round(p*np.cos(ang*np.pi/180),2)
        st.metric(label = '''Px = P.sen($\Theta$)''',
                  value = f'Px={px}N')
        st.metric(label = '''Py = P.cos($\Theta$)''',
                  value = f'Py={py}N')
    with col3:
        if ang==0:
            st.image('PI0.png')
        else:
            st.image('PII.png')
    
    

with aba2:
    st.header('''Decaimento radioativo -  meia-vida''')
    col1, col2 = st.columns(2)
    with col1:
        
        tempo = st.slider('Tempo (Anos)',0,100)
        t = np.linspace(0,tempo,100)
        n = st.slider('Massa Inicial (g)',0,100)
        sigma = st.slider('Taxa de decaimento (g/A)',0.10,0.20)
        N = n*np.exp(-sigma*t)

        massa = {'Tempo (anos)':t,
             'Massa':N}

        M = pd.DataFrame(massa)
    with col2:
        st.line_chart(M,x = 'Tempo (anos)', y = 'Massa')
        cola,colb = st.columns(2)
        cola.write('Massa atual (g)')
        colb.write(np.round(M['Massa'].iloc[-1],2))

with aba3:
    st.header('Lançamento Obliquo')
    col1, col2, col3 = st.columns(3)
    with col1:
        V = st.slider('Velocidade Inicial (m/s)',0,20)
    with col2:
        theta = st.slider('Angulo Inicial (°)',0,90)
    with col3:
        tempo = st.slider('Tempo (s)',0,10)
    t = np.linspace(0,tempo,1000)
    H = V*np.sin(theta*np.pi/180*t)/4
    A = V*np.cos(theta*np.pi/180)*t
    LO = {'t':t,
          'H':H,
          'A':A}

    lo = pd.DataFrame(LO)
    col1, col2, col3 = st.columns(3)
    col1.line_chart(lo,x='t',y='A',x_label='Tempo (s)',
                    y_label='Alcance (m)')
    col2.line_chart(lo,x='t',y='H',x_label='Tempo (s)',
                    y_label='Altura (m)')
    col3.line_chart(lo,x='A',y='H',x_label='Altura (m)',
                    y_label='Alcance (m)')

with aba4:
    st.header('Colisões')
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Objeto 1')
        M1 = st.slider('Massa 1 (Kg)',1,100)
        Vi1 = st.slider('Vel. 1 Antes (m/s)',0,100)
        Vf1 = st.slider('Vel. 1 Depois (m/s)',
                        min_value=-100, max_value=100,
                        value = 0)
    with col2:
        st.subheader('Objeto 2')
        M2 = st.slider('Massa 2 (Kg)',1,100)
        Vi2 = st.slider('Vel. 2 Antes (m/s)',0,100)
        Vf2 = st.slider('Vel. 2 Depois (m/s)',
                        min_value=-100, max_value=100,
                        value = 0)
    EcA = (M1*Vi1**2)/2+(M2*Vi2**2)/2
    EcD = (M1*Vf1**2)/2+(M2*Vf2**2)/2
    col = 'Nenhuma'

    try:
        e = (Vf2-Vf1)/(Vi1-Vi2)
    except:
        e = 0
    st.write(e)
    if e == 1:
        col = 'Elástica'
    if e>0 and e<1 :
        col = 'Perfeitamente Inelástica'
    if e == 0:
        col = 'Inalástica'
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Energia Cinética Antes')
        st.write(EcA)
    with col2:
        st.subheader('Energia Cinética Depois')
        st.write(EcD)
    st.subheader(f'Tipo de Colisão: {col}')
    
with aba5:
    st.header('Seno, Cosseno e Tangente no trinagulo de Pitagoras')
    col1, col2= st.columns(2)
    with col1:
        C1 = st.number_input('Cateto 1')
        C2 = st.number_input('Cateto 2')
    with col2:
        st.subheader('Hipotenusa:')
        H = np.sqrt(C1**2 + C2**2)
        st.subheader(f'{H}')
    st.markdown('---')

    st.subheader('Seno, Cosseno e Tangente')
    st.image('SCT.png')
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader('Seno')
        ang = st.slider('''Angulo $ \\alpha $''',0,90,key = 'sen')
        CO = st.number_input('Cateto Oposto (b)')
        H1 = np.round(CO/np.sin(ang*np.pi/180),2)
        st.subheader('Hipotenusa (a)')
        st.subheader(f'{H1}')

    with col2:
        st.subheader('Cosseno')
        ang2 = st.slider('''Angulo $ \\alpha $''',0,90, key = 'cos')
        CA = st.number_input('Cateto Adjacente (c)')
        H1 = np.round(CA/np.cos(ang*np.pi/180),2)
        st.subheader('Hipotenusa (a)')
        st.subheader(f'{H1}')
    
    with col3:
        st.subheader('Tangente')
        ang3 = st.slider('''Angulo $ \\alpha $''',0,90, key = 'tg')
        CO = st.number_input('Cateto Oposto (c)')
        CA = np.round(CO/np.tan(ang*np.pi/180),2)
        st.subheader('Cateto Adjacente (b)')
        st.subheader(f'{CA}')
    
    


