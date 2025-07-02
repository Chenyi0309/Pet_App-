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

    pet_type = st.radio("What kind of pet do you have?", ["Dog", "Cat", "Rabbit", "Bird", "Other"])
    if pet_type == "Other":
        other_pet = st.text_input("Please specify your pet type:")
    else:
        other_pet = pet_type
    num_pets = st.slider("How many pets do you currently have?", 1, 10, 1)

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
    pay_willingness = st.slider("How much would you be willing to pay monthly for a well-designed pet care app with the features above?", 0, 20, 0, step=1, key="pay_slider_en")

    # Additional questions
    share_platforms = st.multiselect("Which platforms do you normally use to share pet-related content?", ["Instagram", "TikTok", "Facebook", "Reddit", "YouTube", "WeChat",  "Rednote", "Other"])
    share_content_interest = st.multiselect("What kind of content would you like to see or follow on those platforms?", ["Pet care tips", "Funny videos", "Pet product reviews", "Health updates", "Pet training", "Pet community events", "Other"])

    shopping_places = st.multiselect("Where do you usually shop for your pet's needs?", ["PetSmart", "Chewy", "Amazon", "Walmart", "Local pet stores", "Vet office", "Other"])
    paid_before = st.radio("Have you ever paid for a pet-related app or subscription?", ["Yes", "No"])
    share_interest = st.radio("Would you like to share pictures or updates about your pet with other pet owners?", ["Yes", "No", "Maybe"])
    magic_solution = st.text_input("If you could magically solve one pet-related problem with an app, what would it be?")
    usage_freq = st.radio("How often do you expect to use a pet care app?", ["Daily", "A few times a week", "Weekly", "Only when needed"])
    usage_scenarios = st.multiselect("In which situations would you most likely use a pet app?", ["Emergency help", "Regular checkups and tracking", "Shopping for food, toys, or medicine", "Social interaction (photos, events, communities)", "Travel planning with pets"])

    # Demographics and platform ratings
    age = st.selectbox("What is your age range?", ["Under 18", "18–24", "25–34", "35–44", "45–54", "55+"])
    location = st.text_input("Which city do you currently live in?")
    monthly_spend = st.slider("How much do you spend monthly on your pet (food, vet, grooming, etc.)?", 0, 500, 50, step=10)

    selected_platforms = st.multiselect("Which platforms have you used? Rate them below:", ["Chewy", "Rover", "PetDesk", "Other"])
    platform_ratings = {}
    for platform in selected_platforms:
        score = st.slider(f"How satisfied are you with {platform}?", 0, 10, 5, key=f"platform_{platform}")
        platform_ratings[platform] = score
    if "Other" in selected_platforms:
        other_platform = st.text_input("Please name the other platform:")
        other_platform_score = st.slider(f"How satisfied are you with {other_platform}?", 0, 10, 5, key="other_platform_score")
        platform_ratings[other_platform] = other_platform_score

    notification_pref = st.selectbox("How would you prefer to receive reminders?", ["App Notification", "Text Message", "Email", "Calendar Sync"])
    open_feedback = st.text_area("Do you have any other suggestions or features you'd like to see?")
    email = st.text_input("Leave your email if you’d like to get updates about the app or participate in beta testing (optional):")

    if st.button("Submit Survey"):
        platform_scores = ", ".join([f"{k}: {v}" for k, v in platform_ratings.items()])
        response = {
            "Timestamp": datetime.datetime.now(),
            "Pet Type": other_pet,
            "Number of Pets": num_pets,
            "Current Apps": ", ".join(current_apps) + (f"; Other: {other_apps}" if other_apps else ""),
            "Pain Points": ", ".join(pain_points) + (f"; Other: {other_pain}" if other_pain else ""),
            "Interested Features": ", ".join(features_interest),
            "Willingness to Pay": pay_willingness,
            "Email": email,
            "Age": age,
            "City": location,
            "Monthly Spend": monthly_spend,
            "App Satisfaction Scores": platform_scores,
            "Reminder Preference": notification_pref,
            "Additional Feedback": open_feedback,
            "Sharing Platforms": ", ".join(share_platforms),
            "Content Interests": ", ".join(share_content_interest),
            "Shopping Places": ", ".join(shopping_places),
            "Paid for App": paid_before,
            "Willing to Share Pet Content": share_interest,
            "Magic Solution": magic_solution,
            "App Usage Frequency": usage_freq,
            "App Usage Scenarios": ", ".join(usage_scenarios)
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

    pet_type = st.radio("您养的宠物种类是？", ["狗", "猫", "兔子", "鸟", "其他"])
    if pet_type == "其他":
        other_pet = st.text_input("请填写您的宠物类型：")
    else:
        other_pet = pet_type
    num_pets = st.slider("您目前养了几只宠物？", 1, 10, 1)

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

    # 新增问题
    share_platforms = st.multiselect("您通常在哪些平台上分享宠物相关内容？", ["Instagram", "TikTok", "Facebook", "Reddit", "YouTube", "微信", "小红书", "其他"])
    share_content_interest = st.multiselect("您希望在这些平台上看到或关注哪些内容？", ["宠物护理小贴士", "搞笑视频", "宠物产品测评", "健康更新", "宠物训练", "宠物社区活动", "其他"])

    shopping_places = st.multiselect("您通常在哪里买宠物相关用品？", ["PetSmart", "Chewy", "Amazon", "Walmart", "本地宠物店", "兽医诊所", "其他"])
    paid_before = st.radio("您是否曾为宠物相关App或订阅服务付费？", ["是", "否"])
    share_interest = st.radio("您是否愿意与其他宠物主人分享宠物的照片或动态？", ["愿意", "不愿意", "看情况"])
    magic_solution = st.text_input("如果可以用一个App神奇地解决一个与宠物相关的问题，您希望解决什么？")
    usage_freq = st.radio("您希望多频繁使用宠物App？", ["每天", "每周几次", "每周一次", "仅在需要时"])
    usage_scenarios = st.multiselect("您最可能在哪些场景中使用宠物App？", ["紧急求助", "日常健康记录", "购物（食品/玩具/药品）", "社交互动（照片、活动、社区）", "出行安排"])

    age = st.selectbox("您的年龄范围是？", ["18岁以下", "18–24岁", "25–34岁", "35–44岁", "45–54岁", "55岁以上"])
    location = st.text_input("您目前所在的城市是？")
    monthly_spend = st.slider("您每月在宠物上的花费大约是多少？（美元）", 0, 500, 50, step=10)

    selected_platforms = st.multiselect("您使用过哪些平台？请为它们评分：", ["Chewy", "Rover", "PetDesk", "其他"])
    platform_ratings = {}
    for platform in selected_platforms:
        score = st.slider(f"您对 {platform} 的满意度（0-10）：", 0, 10, 5)
        platform_ratings[platform] = score
    if "其他" in selected_platforms:
        other_platform = st.text_input("请填写其他平台名称：")
        other_platform_score = st.slider(f"您对 {other_platform} 的满意度（0-10）：", 0, 10, 5)
        platform_ratings[other_platform] = other_platform_score

    notification_pref = st.selectbox("您更希望通过哪种方式收到宠物相关提醒？", ["App通知", "短信", "邮件", "日历同步"])
    open_feedback = st.text_area("您还有其他想法或希望App具备的功能吗？")

    email = st.text_input("如果您希望收到我们的产品更新或参与内测，可留下您的邮箱（选填）：")

    if st.button("提交调查"):
        platform_scores = ", ".join([f"{k}: {v}" for k, v in platform_ratings.items()])
        response = {
            "时间戳": datetime.datetime.now(),
            "宠物类型": other_pet,
            "宠物数量": num_pets,
            "当前使用的App": ", ".join(current_apps) + (f"；其他：{other_apps}" if other_apps else ""),
            "烦恼点": ", ".join(pain_points) + (f"；其他：{other_pain}" if other_pain else ""),
            "感兴趣的功能": ", ".join(features_interest),
            "愿意支付金额": pay_willingness,
            "邮箱": email,
            "年龄": age,
            "城市": location,
            "月支出": monthly_spend,
            "平台评分": platform_scores,
            "提醒偏好": notification_pref,
            "其他建议": open_feedback,
            "分享平台": ", ".join(share_platforms),
            "内容兴趣": ", ".join(share_content_interest),
            "购物地点": ", ".join(shopping_places),
            "是否付费": paid_before,
            "是否愿意分享宠物": share_interest,
            "希望解决的问题": magic_solution,
            "使用频率": usage_freq,
            "使用场景": ", ".join(usage_scenarios)
        }
        df = pd.DataFrame([response])
        df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
        st.success("✅ 感谢您的参与，您的回答已记录！")

# --- Spanish (Español) full survey ---
elif lang == "Español":
    st.title("🐾 Encuesta para dueños de mascotas - Chicago")
    st.markdown("""
    Somos un pequeño equipo que está desarrollando una aplicación para ayudar a los dueños de mascotas a gestionar la salud, servicios y comunidad de sus mascotas desde un solo lugar.
    Esta breve encuesta nos permitirá conocer tus necesidades y diseñar una aplicación que realmente funcione para ti.
    ¡Gracias por participar!
    """)

    pet_type = st.radio("¿Qué tipo de mascota tienes?", ["Perro", "Gato", "Conejo", "Pájaro", "Otro"])
    if pet_type == "Otro":
        other_pet = st.text_input("Por favor especifica el tipo de mascota:")
    else:
        other_pet = pet_type
    num_pets = st.slider("¿Cuántas mascotas tienes actualmente?", 1, 10, 1)

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

    # Nuevas preguntas
    share_platforms = st.multiselect("¿En qué plataformas sueles compartir contenido relacionado con mascotas?", ["Instagram", "TikTok", "Facebook", "Reddit", "YouTube", "WeChat", "Otro"])
    share_content_interest = st.multiselect("¿Qué tipo de contenido te gustaría ver o seguir en esas plataformas?", ["Consejos de cuidado", "Videos graciosos", "Reseñas de productos", "Actualizaciones de salud", "Entrenamiento de mascotas", "Eventos comunitarios de mascotas", "Otro"])
    shopping_places = st.multiselect("¿Dónde sueles comprar cosas para tu mascota?", ["PetSmart", "Chewy", "Amazon", "Walmart", "Tiendas locales", "Clínica veterinaria", "Otro"])
    paid_before = st.radio("¿Alguna vez has pagado por una app o suscripción relacionada con mascotas?", ["Sí", "No"])
    share_interest = st.radio("¿Te gustaría compartir fotos o actualizaciones de tu mascota con otros dueños?", ["Sí", "No", "Tal vez"])
    magic_solution = st.text_input("Si pudieras resolver mágicamente un problema relacionado con tu mascota mediante una app, ¿cuál sería?")
    usage_freq = st.radio("¿Con qué frecuencia usarías una app de cuidado de mascotas?", ["Diariamente", "Varias veces a la semana", "Semanalmente", "Solo cuando sea necesario"])
    usage_scenarios = st.multiselect("¿En qué situaciones usarías más probablemente una app para mascotas?", ["Emergencias", "Seguimiento y chequeos regulares", "Compras (comida, juguetes, medicina)", "Interacción social (fotos, eventos, comunidades)", "Planeación de viajes con mascotas"])

    age = st.selectbox("¿Cuál es tu rango de edad?", ["Menos de 18", "18–24", "25–34", "35–44", "45–54", "55+"])
    location = st.text_input("¿En qué ciudad vives actualmente?")
    monthly_spend = st.slider("¿Cuánto gastas mensualmente en tu mascota (comida, veterinario, grooming, etc.)?", 0, 500, 50, step=10)

    selected_platforms = st.multiselect("¿Qué plataformas has utilizado? Califícalas abajo:", ["Chewy", "Rover", "PetDesk", "Otro"])
    platform_ratings = {}
    for platform in selected_platforms:
        score = st.slider(f"¿Qué tan satisfecho estás con {platform}?", 0, 10, 5)
        platform_ratings[platform] = score
    if "Otro" in selected_platforms:
        other_platform = st.text_input("Por favor nombra la otra plataforma:")
        other_platform_score = st.slider(f"¿Qué tan satisfecho estás con {other_platform}?", 0, 10, 5)
        platform_ratings[other_platform] = other_platform_score

    notification_pref = st.selectbox("¿Cómo prefieres recibir recordatorios?", ["Notificación de app", "Mensaje de texto", "Correo electrónico", "Sincronización con calendario"])
    open_feedback = st.text_area("¿Tienes otras sugerencias o funciones que te gustaría ver?")
    email = st.text_input("Deja tu correo si deseas recibir actualizaciones o participar en pruebas beta (opcional):")

    if st.button("Enviar encuesta"):
        platform_scores = ", ".join([f"{k}: {v}" for k, v in platform_ratings.items()])
        response = {
            "Marca de tiempo": datetime.datetime.now(),
            "Tipo de mascota": other_pet,
            "Número de mascotas": num_pets,
            "Apps actuales": ", ".join(current_apps) + (f"; Otro: {other_apps}" if other_apps else ""),
            "Puntos de dolor": ", ".join(pain_points) + (f"; Otro: {other_pain}" if other_pain else ""),
            "Funciones deseadas": ", ".join(features_interest),
            "Pago mensual posible": pay_willingness,
            "Correo": email,
            "Edad": age,
            "Ciudad": location,
            "Gasto mensual": monthly_spend,
            "Puntuación de plataformas": platform_scores,
            "Preferencia de notificación": notification_pref,
            "Sugerencias adicionales": open_feedback,
            "Plataformas donde comparte contenido": ", ".join(share_platforms),
            "Tipo de contenido que sigue": ", ".join(share_content_interest),
            "Lugares donde compra": ", ".join(shopping_places),
            "Ha pagado por app": paid_before,
            "Desea compartir contenido": share_interest,
            "Solución mágica": magic_solution,
            "Frecuencia de uso de app": usage_freq,
            "Escenarios de uso": ", ".join(usage_scenarios)
        }
        df = pd.DataFrame([response])
        df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
        st.success("✅ ¡Gracias por tu participación! Tu respuesta ha sido registrada.")

# --- French (Français) full survey ---
elif lang == "Français":
    st.title("🐾 Enquête des propriétaires d'animaux - Chicago")
    st.markdown("""
    Nous sommes une petite équipe en train de développer une application pour aider les propriétaires d’animaux à gérer la santé, les services et la vie sociale de leurs compagnons en un seul endroit.
    Ce court sondage nous aidera à mieux comprendre vos besoins pour concevoir une solution qui vous convient vraiment.
    Merci pour votre participation !
    """)

    pet_type = st.radio("Quel type d'animal avez-vous ?", ["Chien", "Chat", "Lapin", "Oiseau", "Autre"])
    if pet_type == "Autre":
        other_pet = st.text_input("Veuillez spécifier le type d'animal :")
    else:
        other_pet = pet_type
    num_pets = st.slider("Combien d'animaux avez-vous actuellement ?", 1, 10, 1)

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

    # Nouvelles questions
    share_platforms = st.multiselect("Sur quelles plateformes partagez-vous généralement du contenu lié aux animaux ?", ["Instagram", "TikTok", "Facebook", "Reddit", "YouTube", "WeChat", "Autre"])
    share_content_interest = st.multiselect("Quel type de contenu souhaitez-vous voir ou suivre sur ces plateformes ?", ["Conseils de soins", "Vidéos amusantes", "Avis sur des produits", "Mises à jour de santé", "Dressage", "Événements communautaires pour animaux", "Autre"])
    shopping_places = st.multiselect("Où achetez-vous habituellement les produits pour votre animal ?", ["PetSmart", "Chewy", "Amazon", "Walmart", "Magasins locaux", "Cabinet vétérinaire", "Autre"])
    paid_before = st.radio("Avez-vous déjà payé pour une application ou un abonnement lié aux animaux ?", ["Oui", "Non"])
    share_interest = st.radio("Souhaitez-vous partager des photos ou des mises à jour de votre animal avec d'autres propriétaires ?", ["Oui", "Non", "Peut-être"])
    magic_solution = st.text_input("Si une application pouvait magiquement résoudre un problème lié à votre animal, lequel serait-ce ?")
    usage_freq = st.radio("À quelle fréquence pensez-vous utiliser une application de soins pour animaux ?", ["Tous les jours", "Quelques fois par semaine", "Chaque semaine", "Uniquement en cas de besoin"])
    usage_scenarios = st.multiselect("Dans quelles situations seriez-vous le plus susceptible d'utiliser une application pour animaux ?", ["Urgences", "Suivi et contrôles réguliers", "Achats (nourriture, jouets, médicaments)", "Interaction sociale (photos, événements, communauté)", "Planification de voyages avec des animaux"])

    age = st.selectbox("Quel est votre groupe d'âge ?", ["Moins de 18 ans", "18–24 ans", "25–34 ans", "35–44 ans", "45–54 ans", "55+ ans"])
    location = st.text_input("Dans quelle ville habitez-vous actuellement ?")
    monthly_spend = st.slider("Combien dépensez-vous par mois pour votre animal (nourriture, vétérinaire, toilettage, etc.) ?", 0, 500, 50, step=10)

    selected_platforms = st.multiselect("Quelles plateformes avez-vous utilisées ? Évaluez-les ci-dessous :", ["Chewy", "Rover", "PetDesk", "Autre"])
    platform_ratings = {}
    for platform in selected_platforms:
        score = st.slider(f"Quel est votre niveau de satisfaction avec {platform} ?", 0, 10, 5)
        platform_ratings[platform] = score
    if "Autre" in selected_platforms:
        other_platform = st.text_input("Veuillez nommer l'autre plateforme :")
        other_platform_score = st.slider(f"Quel est votre niveau de satisfaction avec {other_platform} ?", 0, 10, 5)
        platform_ratings[other_platform] = other_platform_score

    notification_pref = st.selectbox("Comment préférez-vous recevoir les rappels ?", ["Notification d'application", "SMS", "Email", "Synchronisation avec calendrier"])
    open_feedback = st.text_area("Avez-vous d'autres suggestions ou des fonctionnalités que vous aimeriez voir ?")
    email = st.text_input("Laissez votre e-mail si vous souhaitez recevoir des mises à jour ou participer à la phase de test (facultatif) :")

    if st.button("Soumettre l'enquête"):
        platform_scores = ", ".join([f"{k}: {v}" for k, v in platform_ratings.items()])
        response = {
            "Horodatage": datetime.datetime.now(),
            "Type d'animal": other_pet,
            "Nombre d'animaux": num_pets,
            "Applications utilisées": ", ".join(current_apps) + (f"; Autre: {other_apps}" if other_apps else ""),
            "Points de douleur": ", ".join(pain_points) + (f"; Autre: {other_pain}" if other_pain else ""),
            "Fonctionnalités souhaitées": ", ".join(features_interest),
            "Disposé à payer": pay_willingness,
            "Email": email,
            "Âge": age,
            "Ville": location,
            "Dépense mensuelle": monthly_spend,
            "Notes des plateformes": platform_scores,
            "Préférence de rappel": notification_pref,
            "Suggestions supplémentaires": open_feedback,
            "Plateformes de partage": ", ".join(share_platforms),
            "Contenus préférés": ", ".join(share_content_interest),
            "Lieux d'achat": ", ".join(shopping_places),
            "A déjà payé pour app": paid_before,
            "Souhaite partager": share_interest,
            "Solution magique": magic_solution,
            "Fréquence d'utilisation": usage_freq,
            "Scénarios d'utilisation": ", ".join(usage_scenarios)
        }
        df = pd.DataFrame([response])
        df.to_csv("pet_survey_responses.csv", mode='a', header=False, index=False)
        st.success("✅ Merci pour votre participation ! Votre réponse a été enregistrée.")
