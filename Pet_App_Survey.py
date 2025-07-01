import streamlit as st
import pandas as pd
import datetime

# Language selection
lang = st.selectbox("🌐 Choose your language / 选择语言 / Elija su idioma / Choisissez votre langue:", ["English", "中文", "Español", "Français"])

if lang == "English":
    st.title("🐾 Pet Owner Insights Survey - Chicago")
    st.markdown("""
    We are a small team working on creating a new app that helps pet owners manage their pets’ health, services, and social life all in one place.
    This short survey will help us understand your needs, so we can design a product that truly works for you.
    Thank you for participating!
    """)
    st.markdown("Help us design the perfect pet care app! Your answers will help us better understand your needs.")

elif lang == "中文":
    st.title("🐾 宠物主人调研 - 芝加哥")
    st.markdown("""
    我们是一个正在开发宠物App的小团队，希望为宠物主人提供一站式的健康管理、服务对接和社交平台。
    这份简短的问卷将帮助我们更好地了解您的需求，以便我们打造出真正实用的产品。
    感谢您的参与！
    """)
    st.markdown("欢迎参与我们的调研，帮助我们打造更好的宠物App，满足您的需求！")

elif lang == "Español":
    st.title("🐾 Encuesta para dueños de mascotas - Chicago")
    st.markdown("""
    Somos un pequeño equipo que está desarrollando una aplicación para ayudar a los dueños de mascotas a gestionar la salud, servicios y comunidad de sus mascotas desde un solo lugar.
    Esta breve encuesta nos permitirá conocer tus necesidades y diseñar una aplicación que realmente funcione para ti.
    ¡Gracias por participar!
    """)
    st.markdown("¡Ayúdanos a diseñar la mejor app para el cuidado de mascotas! Tus respuestas nos ayudarán a entender tus necesidades.")

elif lang == "Français":
    st.title("🐾 Enquête des propriétaires d'animaux - Chicago")
    st.markdown("""
    Nous sommes une petite équipe en train de développer une application pour aider les propriétaires d’animaux à gérer la santé, les services et la vie sociale de leurs compagnons en un seul endroit.
    Ce court sondage nous aidera à mieux comprendre vos besoins pour concevoir une solution qui vous convient vraiment.
    Merci pour votre participation !
    """)
    st.markdown("Aidez-nous à concevoir la meilleure application pour les soins des animaux. Vos réponses nous aideront à comprendre vos besoins.")
