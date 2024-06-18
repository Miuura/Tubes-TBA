import streamlit as st
st.set_page_config(page_title="Tugas Besar Teori Bahasa dan Automata", page_icon=":🤖:")

st.title(':blue[Token Recognizer & Parser PDA] 📜')

st.markdown("""
### 👾 Tugas Besar Teori Bahsa dan Automata:
- Valentino Hartanto 1301223020
- Gede Bagus Krishnanditya Merta 1301223088 
- Raka Aditya Waluya 1301220192

### 🪽 Deskripsi: 
\nTugas besar ini bertujuan untuk membuat sebuah sistem token recognizer dan parser menggunakan Pushdown Automata (PDA) untuk mengenali struktur kalimat berbahasa Indonesia yang memiliki pola Subjek-Predikat-Objek-Keterangan (SPOK).\nStruktur SPOK yang akan dikenali dalam tugas ini dibatasi pada kumpulan kata berikut ini:\n1. Subjek (S): ibu, ayah, anjing, siswa, saya\n2. Predikat (P): memasak, membaca, menulis, mengejar, belajar\n3. Objek (O): nasi, buku, surat, bola, kimia\n4. Keterangan (K): di dapur, di taman, di kamar, tadi pagi, kemarin\n
Dengan sistem ini, kita dapat secara otomatis memverifikasi kalimat berdasarkan struktur SPOK yang telah ditentukan. 
""")
st.write('')

kalimat = st.text_input("Input Kalimat Anda:", placeholder="Contoh: ayah membaca buku di taman")
alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ListState = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
              'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20',
              'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30',
              'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40',
              'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50',
              'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60',
              'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70',
              'q71', 'q72', 'q73', 'q74', 'q75', 'q76', 'q77', 'q78', 'q79', 'q80']

TransitionTable = {}
ParseTable = {}

for state in ListState:
    for alp in alpabet:
        TransitionTable[(state, alp)] = 'error'
    TransitionTable[(state, ' ')] = 'error'
    TransitionTable[(state, '#')] = 'error'

TransitionTable[('q0', 'a')] = 'q1'
TransitionTable[('q0', 's')] = 'q7' 
TransitionTable[('q0', 'i')] = 'q3'
TransitionTable[('q0', 'm')] = 'q4'
TransitionTable[('q0', 'b')] = 'q5'
TransitionTable[('q0', 'n')] = 'q6'
TransitionTable[('q0', 's')] = 'q7'
TransitionTable[('q0', 'k')] = 'q8'
TransitionTable[('q0', 'd')] = 'q9'
TransitionTable[('q0', 't')] = 'q10'
TransitionTable[('q1', 'y')] = 'q11'
TransitionTable[('q1', 'n')] = 'q12'
TransitionTable[('q7', 'a')] = 'q17' 
TransitionTable[('q7', 'i')] = 'q19' 
TransitionTable[('q3', 'b')] = 'q22'
TransitionTable[('q4', 'e')] = 'q23'
TransitionTable[('q5', 'e')] = 'q39'
TransitionTable[('q5', 'u')] = 'q42'
TransitionTable[('q5', 'o')] = 'q43'
TransitionTable[('q6', 'a')] = 'q46'
TransitionTable[('q7', 'u')] = 'q48'
TransitionTable[('q8', 'i')] = 'q51'
TransitionTable[('q8', 'e')] = 'q54'
TransitionTable[('q9', 'i')] = 'q59'
TransitionTable[('q10', 'a')] = 'q72'
TransitionTable[('q11', 'a')] = 'q13'
TransitionTable[('q13', 'h')] = 'q21'
TransitionTable[('q12', 'j')] = 'q14'
TransitionTable[('q14', 'i')] = 'q15'
TransitionTable[('q15', 'n')] = 'q16'
TransitionTable[('q16', 'g')] = 'q21'
TransitionTable[('q17', 'y')] = 'q18'
TransitionTable[('q18', 'a')] = 'q21'
TransitionTable[('q19', 's')] = 'q20'
TransitionTable[('q20', 'w')] = 'q18'
TransitionTable[('q22', 'u')] = 'q21'
TransitionTable[('q21', ' ')] = 'q0'
TransitionTable[('q23', 'm')] = 'q24'
TransitionTable[('q23', 'n')] = 'q25'
TransitionTable[('q24', 'a')] = 'q26'
TransitionTable[('q24', 'b')] = 'q27'
TransitionTable[('q26', 's')] = 'q28'
TransitionTable[('q28', 'a')] = 'q30'
TransitionTable[('q30', 'k')] = 'q41'
TransitionTable[('q27', 'a')] = 'q29'
TransitionTable[('q29', 'c')] = 'q31'
TransitionTable[('q31', 'a')] = 'q41'
TransitionTable[('q25', 'u')] = 'q32'
TransitionTable[('q25', 'g')] = 'q33'
TransitionTable[('q32', 'l')] = 'q34'
TransitionTable[('q34', 'i')] = 'q36'
TransitionTable[('q36', 's')] = 'q41'
TransitionTable[('q33', 'e')] = 'q35'
TransitionTable[('q35', 'j')] = 'q37'
TransitionTable[('q37', 'a')] = 'q38'
TransitionTable[('q38', 'r')] = 'q41'
TransitionTable[('q39', 'l')] = 'q40'
TransitionTable[('q40', 'a')] = 'q35'
TransitionTable[('q41', ' ')] = 'q0'
TransitionTable[('q42', 'k')] = 'q44'
TransitionTable[('q44', 'u')] = 'q53'
TransitionTable[('q43', 'l')] = 'q45'
TransitionTable[('q45', 'a')] = 'q53'
TransitionTable[('q46', 's')] = 'q47'
TransitionTable[('q47', 'i')] = 'q53'
TransitionTable[('q48', 'r')] = 'q49'
TransitionTable[('q49', 'a')] = 'q50'
TransitionTable[('q50', 't')] = 'q53'
TransitionTable[('q51', 'm')] = 'q52'
TransitionTable[('q52', 'i')] = 'q80'
TransitionTable[('q80', 'a')] = 'q53'
TransitionTable[('q53', ' ')] = 'q0'
TransitionTable[('q54', 'm')] = 'q55'
TransitionTable[('q55', 'a')] = 'q56'
TransitionTable[('q56', 'r')] = 'q57'
TransitionTable[('q57', 'i')] = 'q58'
TransitionTable[('q58', 'n')] = 'q79'
TransitionTable[('q59', ' ')] = 'q60'
TransitionTable[('q60', 'd')] = 'q61'
TransitionTable[('q60', 'k')] = 'q62'
TransitionTable[('q60', 't')] = 'q63'
TransitionTable[('q61', 'a')] = 'q64'
TransitionTable[('q64', 'p')] = 'q65'
TransitionTable[('q65', 'u')] = 'q66'
TransitionTable[('q66', 'r')] = 'q79'
TransitionTable[('q62', 'a')] = 'q67'
TransitionTable[('q67', 'm')] = 'q68'
TransitionTable[('q68', 'a')] = 'q66'
TransitionTable[('q63', 'a')] = 'q69'
TransitionTable[('q69', 'm')] = 'q70'
TransitionTable[('q70', 'a')] = 'q71'
TransitionTable[('q71', 'n')] = 'q79'
TransitionTable[('q72', 'd')] = 'q73'
TransitionTable[('q73', 'i')] = 'q74'
TransitionTable[('q74', ' ')] = 'q75'
TransitionTable[('q75', 'p')] = 'q76'
TransitionTable[('q76', 'a')] = 'q77'
TransitionTable[('q77', 'g')] = 'q78'
TransitionTable[('q78', 'i')] = 'q79'
TransitionTable[('q79', ' ')] = 'q0'
ParseTable[('START', 'ibu')] = ['S']
ParseTable[('START', 'ayah')] = ['S']
ParseTable[('START', 'anjing')] = ['S']
ParseTable[('START', 'siswa')] = ['S']
ParseTable[('START', 'saya')] = ['S']
ParseTable[('START', 'memasak')] = ['error']
ParseTable[('START', 'membaca')] = ['error']
ParseTable[('START', 'menulis')] = ['error']
ParseTable[('START', 'mengejar')] = ['error']
ParseTable[('START', 'belajar')] = ['error']
ParseTable[('START', 'nasi')] = ['error']
ParseTable[('START', 'buku')] = ['error']
ParseTable[('START', 'surat')] = ['error']
ParseTable[('START', 'bola')] = ['error']
ParseTable[('START', 'kimia')] = ['error']
ParseTable[('START', 'didapur')] = ['error']
ParseTable[('START', 'ditaman')] = ['error']
ParseTable[('START', 'dikamar')] = ['error']
ParseTable[('START', 'tadipagi')] = ['error']
ParseTable[('START', 'kemarin')] = ['error']
ParseTable[('START', 'EOS')] = ['error']
ParseTable[('S', 'ibu')] = ['ibu', 'P']
ParseTable[('S', 'ayah')] = ['ayah', 'P']
ParseTable[('S', 'anjing')] = ['anjing', 'P']
ParseTable[('S', 'siswa')] = ['siswa', 'P']
ParseTable[('S', 'saya')] = ['saya', 'P']
ParseTable[('S', 'memasak')] = ['error']
ParseTable[('S', 'membaca')] = ['error']
ParseTable[('S', 'menulis')] = ['error']
ParseTable[('S', 'mengejar')] = ['error']
ParseTable[('S', 'belajar')] = ['error']
ParseTable[('S', 'nasi')] = ['error']
ParseTable[('S', 'buku')] = ['error']
ParseTable[('S', 'surat')] = ['error']
ParseTable[('S', 'bola')] = ['error']
ParseTable[('S', 'kimia')] = ['error']
ParseTable[('S', 'didapur')] = ['error']
ParseTable[('S', 'ditaman')] = ['error']
ParseTable[('S', 'dikamar')] = ['error']
ParseTable[('S', 'tadipagi')] = ['error']
ParseTable[('S', 'kemarin')] = ['error']
ParseTable[('S', 'EOS')] = ['error']
ParseTable[('P', 'ibu')] = ['error']
ParseTable[('P', 'ayah')] = ['error']
ParseTable[('P', 'anjing')] = ['error']
ParseTable[('P', 'siswa')] = ['error']
ParseTable[('P', 'saya')] = ['error']
ParseTable[('P', 'memasak')] = ['memasak', 'O']
ParseTable[('P', 'membaca')] = ['membaca', 'O']
ParseTable[('P', 'menulis')] = ['menulis', 'O']
ParseTable[('P', 'mengejar')] = ['mengejar', 'O']
ParseTable[('P', 'belajar')] = ['belajar', 'O']
ParseTable[('P', 'nasi')] = ['error']
ParseTable[('P', 'buku')] = ['error']
ParseTable[('P', 'surat')] = ['error']
ParseTable[('P', 'bola')] = ['error']
ParseTable[('P', 'kimia')] = ['error']
ParseTable[('P', 'didapur')] = ['error']
ParseTable[('P', 'ditaman')] = ['error']
ParseTable[('P', 'dikamar')] = ['error']
ParseTable[('P', 'tadipagi')] = ['error']
ParseTable[('P', 'kemarin')] = ['error']
ParseTable[('P', 'EOS')] = ['error']
ParseTable[('O', 'ibu')] = ['error']
ParseTable[('O', 'ayah')] = ['error']
ParseTable[('O', 'anjing')] = ['error']
ParseTable[('O', 'siswa')] = ['error']
ParseTable[('O', 'saya')] = ['error']
ParseTable[('O', 'memasak')] = ['error']
ParseTable[('O', 'membaca')] = ['error']
ParseTable[('O', 'menulis')] = ['error']
ParseTable[('O', 'mengejar')] = ['error']
ParseTable[('O', 'belajar')] = ['error']
ParseTable[('O', 'nasi')] = ['nasi', 'K']
ParseTable[('O', 'buku')] = ['buku', 'K']
ParseTable[('O', 'surat')] = ['surat', 'K']
ParseTable[('O', 'bola')] = ['bola', 'K']
ParseTable[('O', 'kimia')] = ['kimia', 'K']
ParseTable[('O', 'didapur')] = ['K']
ParseTable[('O', 'ditaman')] = ['K']
ParseTable[('O', 'dikamar')] = ['K']
ParseTable[('O', 'tadipagi')] = ['K']
ParseTable[('O', 'kemarin')] = ['K']
ParseTable[('O', 'EOS')] = ['epsilon']
ParseTable[('K', 'ibu')] = ['error']
ParseTable[('K', 'ayah')] = ['error']
ParseTable[('K', 'anjing')] = ['error']
ParseTable[('K', 'siswa')] = ['error']
ParseTable[('K', 'saya')] = ['error']
ParseTable[('K', 'memasak')] = ['error']
ParseTable[('K', 'membaca')] = ['error']
ParseTable[('K', 'menulis')] = ['error']
ParseTable[('K', 'mengejar')] = ['error']
ParseTable[('K', 'belajar')] = ['error']
ParseTable[('K', 'nasi')] = ['error']
ParseTable[('K', 'buku')] = ['error']
ParseTable[('K', 'surat')] = ['error']
ParseTable[('K', 'bola')] = ['error']
ParseTable[('K', 'kimia')] = ['error']
ParseTable[('K', 'didapur')] = ['didapur']
ParseTable[('K', 'ditaman')] = ['ditaman']
ParseTable[('K', 'dikamar')] = ['dikamar']
ParseTable[('K', 'tadipagi')] = ['tadipagi']
ParseTable[('K', 'kemarin')] = ['kemarin']
ParseTable[('K', 'EOS')] = ['epsilon']

if kalimat:
    st.write("--------------------------------------------------------")
    st.subheader("🪧 Token Recognizer")
    st.write("--------------------------------------------------------")

    tokens = []
    token = ""
    state = 'q0'
    temp = kalimat+'#' 
    struktur = []
    for i in range(len(temp)):
        if temp[i] != ' ':
            token += temp[i]
        state = TransitionTable[(state, temp[i])]
        if state == 'q21':
            st.write(f'Token: "{token}" Valid, kata tersebut merupakan Subjek')
            struktur.append('Subjek')
            tokens.append(token)
            token = ""
        elif state == 'q41':
            st.write(f'Token: "{token}" Valid, kata tersebut merupakan Predikat')
            struktur.append('Predikat')
            tokens.append(token)
            token = ""
        elif state == 'q53':
            st.write(f'Token: "{token}" Valid, kata tersebut merupakan Objek')
            struktur.append('Objek')
            tokens.append(token)
            token = ""
        elif state == 'q79':
            st.write(f'Token: "{token}" Valid, kata tersebut merupakan Keterangan')
            struktur.append('Keterangan')
            tokens.append(token)
            token = ""
        
        if state == 'error' and temp[i] == '#':
            valid = True
            break
        elif state == 'error':
            st.write("index", i)
            i+=1
            while True:
                if temp[i] == ' ' or temp[i] == '#':
                    break
                token += temp[i]
                i+=1
            valid = False
            break
    st.write("--------------------------------------------------------")
    if valid:
        st.write(f'\nSeluruh kata dalam "{kalimat}" adalah valid')
        st.write(f"Token: {tokens}")
    else:
        st.write(f'\nTerdapat kesalahan kata dalam "{kalimat}", kata "{token}" tidak valid')

    # PARSER PDA
    tokens.append("EOS")
    stack = []
    nonterminal = ['START', 'S', 'P', 'O', 'K']
    terminal = ['ibu', 'ayah', 'anjing', 'siswa', 'saya', 'memasak', 'membaca', 'menulis', 'mengejar', 'belajar', 'nasi', 'buku', 'surat', 'bola', 'kimia', 'didapur', 'ditaman', 'dikamar', 'tadipagi', 'kemarin', 'EOS', 'epsilon']

    stack.append('#')
    stack.append('START')

    st.write("\n--------------------------------------------------------")
    st.subheader("🪧 Parser PDA")
    st.write("--------------------------------------------------------")

    indeks = 0
    while True:
        if stack[-1] in terminal:
            st.write(f"\nStack: {stack}")
            st.write("Top Stack: ", stack[-1])
            st.write("Top Stack Merupakan Variabel Terminal")
            if stack[-1] == tokens[indeks]:
                st.write(f'Token: "{tokens[indeks]}" Valid')
                st.write("\n--------------------------------------------------------")
                stack.pop()
                indeks += 1
            elif stack[-1] == 'epsilon':
                st.write('Epsilon ditemukan, melakukan pop pada stack')
                stack.pop()
            else:
                st.write(f'Token: "{tokens[indeks]}" Tidak Valid')
                break
        elif stack[-1] in nonterminal:
            st.write(f"\nStack: {stack}")
            st.write("Top Stack: ", stack[-1])
            st.write("Top Stack Merupakan Variabel Non-Terminal")
            st.write("\n--------------------------------------------------------")
            temp = ParseTable[(stack[-1], tokens[indeks])]
            stack.pop()
            for i in range(len(temp)):
                stack.append(temp[len(temp)-1-i])
        elif stack[-1] == 'error':
            st.write(f'\nError, kalimat "{kalimat}" tidak sesuai dengan grammar atau struktur SPOK/SPO/SPK/SP')
            break
        elif stack[-1] == '#':
            if tokens[indeks] == "EOS":
                st.write(f'\nValid, kalimat "{kalimat}" sudah sesuai dengan grammar. struktur pada kalimat tersebut adalah {struktur}')
            else:
                st.write(f'\nError, kalimat "{kalimat}" tidak sesuai dengan grammar atau struktur SPOK/SPO/SPK/SP')
            break

    st.write("\n--------------------------------------------------------")
