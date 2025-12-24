import streamlit as st
import requests

st.title("Pokémon Visual App")

if st.button("Get Random Pokémon"):
    res = requests.get("http://127.0.0.1:8000/pokemon/random")
    data = res.json()

    st.subheader(data["name"].capitalize())
    st.write(f"Height: {data['height']}")
    st.write(f"Weight: {data['weight']}")
    st.write(f"Types: {', '.join(data['types'])}")
