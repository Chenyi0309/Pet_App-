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

    st.header("1. About You and Your Pet")
    pet_type = st.radio("What kind of pet do you have?", ["Dog", "Cat", "Rabbit", "Bird", "Other"])
    if pet_type == "Other":
        other_pet = st.text_input("Please specify your pet type:")
    else:
        other_pet = pet_type
    num_pets = st.slider("How many pets do you currently have?", 1, 10, 1)

    st.header("2. Your Current Tools")
    current_apps = st.multiselect(
        "Which apps or websites do you currently use to help take care of your pet(s)?",
        ["Chewy", "Rover", "PetDesk", "Instagram", "Facebook Groups", "Reddit", "Google Calendar", "None", "Other"]
    )
    if "Other" in current_apps:
        other_apps = st.text_input("Please specify other apps you use:")
    else:
        other_apps = ""

    pain_points = st.multiselect(
        "What are the most frustrating parts of being a pet owner?",
        [
            "Remembering vaccines & vet appointments",
            "Finding trusted vets or groomers",
            "Shopping for the right food/toys",
            "No community or social features",
            "Hard to track health data",
            "Other"
        ]
    )
    if "Other" in pain_points:
        other_pain = st.text_input("Please describe other pain points:")
    else:
        other_pain = ""

    st.header("3. Your Interest in New Features")
    features_interest = st.multiselect(
        "Which features would you love to see in a pet care app?",
        [
            "Vaccination and medication reminders",
            "Online vet consultations",
            "Pet profile and health tracking",
            "Local pet services (grooming, sitting, walking)",
            "Pet community and sharing photos",
            "Pet product recommendations & shopping",
            "Event organization (pet meetups, competitions)"
        ]
    )
    pay_willingness = st.slider("How much would you be willing to pay monthly for a well-designed pet care app with the features above?", 0, 20, 0, step=1)

    st.header("4. Optional Contact")
    email = st.text_input("Leave your email if you’d like to get updates about the app or participate in beta testing (optional):")

    if st.button("Submit Survey"):
        response = {
            "Timestamp": datetime.datetime.now(),
            "Pet Type": other_pet,
            "Number of Pets": num_pets,
            "Current Apps": ", ".join(current_apps) + (f"; Other: {other_apps}" if other_apps else ""),
            "Pain Points": ", ".join(pain_points) + (f"; Other: {other_pain}" if other_pain else ""),
            "Interested Features": ", ".join(features_interest),
            "Willingness to Pay": pay_willingness,
            "Email": email
        }
        df = pd.DataFrame([response])
        df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
        st.success("✅ Thank you for your input! Your response has been recorded.")

elif lang == "中文":
    st.title("🐾 宠物主人调研 - 芝加哥")
st.markdown("""
我们是一个正在开发宠物App的小团队，希望为宠物主人提供一站式的健康管理、服务对接和社交平台。
这份简短的问卷将帮助我们更好地了解您的需求，以便我们打造出真正实用的产品。
感谢您的参与！
""")
    st.markdown("欢迎参与我们的调研，帮助我们打造更好的宠物App，满足您的需求！")

    st.header("1. 关于您和您的宠物")
    pet_type = st.radio("您养的宠物种类是？", ["狗", "猫", "兔子", "鸟", "其他"])
    if pet_type == "其他":
        other_pet = st.text_input("请填写您的宠物类型：")
    else:
        other_pet = pet_type
    num_pets = st.slider("您目前养了几只宠物？", 1, 10, 1)

    st.header("2. 您目前使用的工具")
    current_apps = st.multiselect(
        "您目前在使用哪些App或网站来照顾宠物？",
        ["Chewy", "Rover", "PetDesk", "Instagram", "Facebook Groups", "Reddit", "Google Calendar", "没有", "其他"]
    )
    if "其他" in current_apps:
        other_apps = st.text_input("请填写其他您使用的App：")
    else:
        other_apps = ""

    pain_points = st.multiselect(
        "作为宠物主，您觉得最烦恼的问题是什么？",
        [
            "记不住疫苗和看病时间",
            "找不到靠谱的医生或美容店",
            "买不到合适的食品和玩具",
            "没有社区或社交功能",
            "难以追踪健康记录",
            "其他"
        ]
    )
    if "其他" in pain_points:
        other_pain = st.text_input("请描述其他问题：")
    else:
        other_pain = ""

    st.header("3. 您对新功能的兴趣")
    features_interest = st.multiselect(
        "如果有新的宠物App，您希望它包含哪些功能？",
        [
            "疫苗与用药提醒",
            "在线兽医咨询",
            "宠物档案与健康记录",
            "本地宠物服务预约（洗护、寄养、遛狗）",
            "宠物社区与分享",
            "宠物商品推荐与购买",
            "组织活动（线下聚会、比赛等）"
        ]
    )
    pay_willingness = st.slider("如果这些功能都很好，您每月最多愿意支付多少钱？（单位：美元）", 0, 20, 0, step=1)

    st.header("4. 可选联系方式")
    email = st.text_input("如果您希望收到我们的产品更新或参与内测，可留下您的邮箱（选填）：")

    if st.button("提交调查"):
        response = {
            "时间戳": datetime.datetime.now(),
            "宠物类型": other_pet,
            "宠物数量": num_pets,
            "当前使用的App": ", ".join(current_apps) + (f"；其他：{other_apps}" if other_apps else ""),
            "烦恼点": ", ".join(pain_points) + (f"；其他：{other_pain}" if other_pain else ""),
            "感兴趣的功能": ", ".join(features_interest),
            "愿意支付金额": pay_willingness,
            "邮箱": email
        }
        df = pd.DataFrame([response])
        df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
        st.success("✅ 感谢您的参与，您的回答已记录！")

elif lang == "Español":
    st.title("🐾 Encuesta para dueños de mascotas - Chicago")
st.markdown("""
Somos un pequeño equipo que está desarrollando una aplicación para ayudar a los dueños de mascotas a gestionar la salud, servicios y comunidad de sus mascotas desde un solo lugar.
Esta breve encuesta nos permitirá conocer tus necesidades y diseñar una aplicación que realmente funcione para ti.
¡Gracias por participar!
""")
    st.markdown("¡Ayúdanos a diseñar la mejor app para el cuidado de mascotas! Tus respuestas nos ayudarán a entender tus necesidades.")

    st.header("1. Sobre ti y tu mascota")
    pet_type = st.radio("¿Qué tipo de mascota tienes?", ["Perro", "Gato", "Conejo", "Pájaro", "Otro"])
    if pet_type == "Otro":
        other_pet = st.text_input("Por favor especifica el tipo de mascota:")
    else:
        other_pet = pet_type
    num_pets = st.slider("¿Cuántas mascotas tienes actualmente?", 1, 10, 1)

    st.header("2. Herramientas actuales")
    current_apps = st.multiselect(
        "¿Qué aplicaciones o sitios web utilizas para cuidar a tu(s) mascota(s)?",
        ["Chewy", "Rover", "PetDesk", "Instagram", "Facebook Groups", "Reddit", "Google Calendar", "Ninguna", "Otro"]
    )
    if "Otro" in current_apps:
        other_apps = st.text_input("Por favor especifica otras aplicaciones que usas:")
    else:
        other_apps = ""

    pain_points = st.multiselect(
        "¿Cuáles son las partes más frustrantes de ser dueño de una mascota?",
        [
            "Recordar vacunas y citas veterinarias",
            "Encontrar veterinarios o peluqueros confiables",
            "Comprar la comida o juguetes adecuados",
            "Falta de comunidad o funciones sociales",
            "Dificultad para seguir el historial de salud",
            "Otro"
        ]
    )
    if "Otro" in pain_points:
        other_pain = st.text_input("Por favor describe otros puntos de dolor:")
    else:
        other_pain = ""

    st.header("3. Interés en nuevas funciones")
    features_interest = st.multiselect(
        "¿Qué funciones te gustaría ver en una app para cuidado de mascotas?",
        [
            "Recordatorios de vacunación y medicamentos",
            "Consultas veterinarias en línea",
            "Perfil de mascota y seguimiento de salud",
            "Servicios locales para mascotas (peluquería, cuidado, paseo)",
            "Comunidad de mascotas y compartir fotos",
            "Recomendaciones y compras de productos",
            "Organización de eventos (encuentros, competencias)"
        ]
    )
    pay_willingness = st.slider("¿Cuánto estarías dispuesto a pagar al mes por una app bien diseñada con las funciones anteriores?", 0, 20, 0, step=1)

    st.header("4. Contacto opcional")
    email = st.text_input("Deja tu correo si deseas recibir actualizaciones o participar en pruebas beta (opcional):")

    if st.button("Enviar encuesta"):
        response = {
            "Marca de tiempo": datetime.datetime.now(),
            "Tipo de mascota": other_pet,
            "Número de mascotas": num_pets,
            "Apps actuales": ", ".join(current_apps) + (f"; Otro: {other_apps}" if other_apps else ""),
            "Puntos de dolor": ", ".join(pain_points) + (f"; Otro: {other_pain}" if other_pain else ""),
            "Funciones deseadas": ", ".join(features_interest),
            "Pago mensual posible": pay_willingness,
            "Correo": email
        }
        df = pd.DataFrame([response])
        df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
        st.success("✅ ¡Gracias por tu participación! Tu respuesta ha sido registrada.")

elif lang == "Français":
    st.title("🐾 Enquête des propriétaires d'animaux - Chicago")
st.markdown("""
Nous sommes une petite équipe en train de développer une application pour aider les propriétaires d’animaux à gérer la santé, les services et la vie sociale de leurs compagnons en un seul endroit.
Ce court sondage nous aidera à mieux comprendre vos besoins pour concevoir une solution qui vous convient vraiment.
Merci pour votre participation !
""")
    st.markdown("Aidez-nous à concevoir la meilleure application pour les soins des animaux. Vos réponses nous aideront à comprendre vos besoins.")

    st.header("1. À propos de vous et de votre animal")
    pet_type = st.radio("Quel type d'animal avez-vous ?", ["Chien", "Chat", "Lapin", "Oiseau", "Autre"])
    if pet_type == "Autre":
        other_pet = st.text_input("Veuillez spécifier le type d'animal :")
    else:
        other_pet = pet_type
    num_pets = st.slider("Combien d'animaux avez-vous actuellement ?", 1, 10, 1)

    st.header("2. Vos outils actuels")
    current_apps = st.multiselect(
        "Quelles applications ou sites web utilisez-vous pour prendre soin de votre/vos animal(aux) ?",
        ["Chewy", "Rover", "PetDesk", "Instagram", "Facebook Groups", "Reddit", "Google Calendar", "Aucun", "Autre"]
    )
    if "Autre" in current_apps:
        other_apps = st.text_input("Veuillez préciser d'autres applications que vous utilisez :")
    else:
        other_apps = ""

    pain_points = st.multiselect(
        "Quelles sont les parties les plus frustrantes du fait d'être propriétaire d'un animal ?",
        [
            "Se souvenir des vaccins et des rendez-vous vétérinaires",
            "Trouver des vétérinaires ou toiletteurs fiables",
            "Acheter les bons aliments ou jouets",
            "Pas de communauté ou de fonctions sociales",
            "Suivi difficile des données de santé",
            "Autre"
        ]
    )
    if "Autre" in pain_points:
        other_pain = st.text_input("Veuillez décrire les autres points de frustration :")
    else:
        other_pain = ""

    st.header("3. Intérêt pour de nouvelles fonctionnalités")
    features_interest = st.multiselect(
        "Quelles fonctionnalités aimeriez-vous voir dans une application de soins pour animaux ?",
        [
            "Rappels de vaccination et de médicaments",
            "Consultations vétérinaires en ligne",
            "Profil de l'animal et suivi de la santé",
            "Services locaux pour animaux (toilettage, garde, promenade)",
            "Communauté et partage de photos",
            "Recommandations de produits et achats",
            "Organisation d'événements (rencontres, concours)"
        ]
    )
    pay_willingness = st.slider("Combien seriez-vous prêt à payer par mois pour une application bien conçue avec les fonctionnalités ci-dessus ?", 0, 20, 0, step=1)

    st.header("4. Contact facultatif")
    email = st.text_input("Laissez votre e-mail si vous souhaitez recevoir des mises à jour ou participer à la phase de test (facultatif) :")

    if st.button("Soumettre l'enquête"):
        response = {
            "Horodatage": datetime.datetime.now(),
            "Type d'animal": other_pet,
            "Nombre d'animaux": num_pets,
            "Applications utilisées": ", ".join(current_apps) + (f"; Autre: {other_apps}" if other_apps else ""),
            "Points de douleur": ", ".join(pain_points) + (f"; Autre: {other_pain}" if other_pain else ""),
            "Fonctionnalités souhaitées": ", ".join(features_interest),
            "Disposé à payer": pay_willingness,
            "Email": email
        }
        df = pd.DataFrame([response])
        df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
        st.success("✅ Merci pour votre participation ! Votre réponse a été enregistrée.")
