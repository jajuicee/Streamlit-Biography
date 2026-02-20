import streamlit as st
import pandas as pd
import altair as alt


st.set_page_config(page_title="Reinzo's Portfolio", page_icon="", layout="centered")

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("<h1 style='text-align: center; font-size: 90px;'></h1>", unsafe_allow_html=True)

with col2:
    st.title("Reinzo Carlo G. Olo")
    st.subheader(" BSIT - 3rd Year")
    st.caption("Future AI Engineer & Web Developer")

st.divider() 


st.header(" About Me")
st.info(
    "I love to play videogames  and I am currently exploring the ever-evolving world of tech. "
    "I am working hard with the hope of becoming an **AI Engineer**, **Backend Developer**, or **Frontend Developer** in the near future! 🚀💻"
)

st.divider()


st.header(" My Skills")
st.write("Here is a breakdown of my current skills (out of 5):")


skills_data = pd.DataFrame({
    "Skill": ["Programming", "Debug", "Documentation", "Procrastinate", "Video Games"],
    "Level": [3, 4, 3, 5, 5]
})


base_chart = alt.Chart(skills_data).mark_bar(
    cornerRadiusEnd=10,
    height=40           
).encode(
    x=alt.X('Level:Q', scale=alt.Scale(domain=[0, 5]), title='Skill Level (Out of 5)'),
    y=alt.Y('Skill:N', sort='-x', title=''),
    color=alt.Color('Level:Q', scale=alt.Scale(scheme='tealblues'), legend=None),
    tooltip=['Skill', 'Level']
)


text_labels = base_chart.mark_text(
    align='left',
    baseline='middle',
    dx=5, 
).encode(
    text='Level:Q'
)


final_chart = (base_chart + text_labels).properties(height=350)


st.altair_chart(final_chart, use_container_width=True)


st.divider()
