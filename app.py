# main.py
import streamlit as st
import time
from generate_label import get_label


def main():

    st.set_page_config(
        page_title="Aplikasi Klasifikasi Tugas Akhir | Klasifikasi Tugas Akhir ", page_icon="🎓")

    st.image("assets/banner.png", use_column_width=True)

    st.subheader(
        "Topic Classification: Aplikasi Kategori PTA Jurusan Teknik Informatika")
    st.caption(
        "Tugas akhir umumnya memiliki beberapa kategori terkait topic pembahasan pada tugas akhir tersebut. Program Studi Teknik Informatika ini dibagi menjadi 2 kategori umum yaitu Komputasi dan Rekayasa Perangkat Lunak (RPL). Topic classification ini digunakan untuk menentukan topik tugas akhir berdasarkan abstrak yang dimasukkan. 'Kunjungi juga 🧑‍🎓️ [PTA Universitas Trunojoyo Madura](https://pta.trunojoyo.ac.id/c_search/byprod/10)'")

    news_text = st.text_area(
        "Masukkan Abstrak Tugas Akhir", key="input_text", height=250)

    if st.button("Tentukan Topik"):
        if news_text:
            text = get_label(news_text)
            with st.expander('Tampilkan Hasil'):
                st.write(
                    'Abstrak yang anda masukkan termasuk dalam kategori tugas akhir: ')
                if text == "rpl":
                    st.info(text, icon="💻")
                elif text == "komputasi":
                    st.success(text, icon="🔢")
        else:
            time.sleep(.5)
            st.toast('Masukkan teks terlebih dahulu', icon='🤧')


if __name__ == "__main__":
    main()
