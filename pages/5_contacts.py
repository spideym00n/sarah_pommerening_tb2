import streamlit as st


st.logo(
    "https://cdn-icons-png.flaticon.com/512/9029/9029906.png",
    size="large",
    icon_image="https://cdn-icons-png.flaticon.com/512/1256/1256449.png",
)


# Page Configuration
st.set_page_config(page_title="Contact Resources", layout="wide")

# Header
st.title("📞 Contact Resources")

# Language Switcher
language = st.radio("🌐 Choose Language:", ["English", "Deutsch"], horizontal=True)

# --- Language-Specific Content ---
if language == "English":
    st.write(
        "Listed below are various websites of organizations that are active in your area and might provide further useful resources as well as support hotlines."
    )

    # National and International Resources
    st.write("### 🌍 **National and International Resources**")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🇬🇧 UK Resources")
        if st.button("Mental Health Organisation (UK)"):
            st.write(
                "🔗 [Visit Mental Health Organisation](https://www.mentalhealth.org.uk/our-work/programmes/families-children-and-young-people/single-parents-projects)"
            )

        if st.button("Gingerbread (UK)"):
            st.write("🔗 [Visit Gingerbread Website](https://www.gingerbread.org.uk/our-work/support-for-single-parents/)")

    with col2:
        st.subheader("🇺🇸 USA Resources")
        if st.button("Mental Health America (USA)"):
            st.write("🔗 [Visit MHA Website](https://mhanational.org/mental-health-and-single-parent)")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🇨🇦 Canada Resources")
        if st.button("One Parent (CA)"):
            st.write("🔗 [Visit One Parent Website](https://oneparent.org/)")

elif language == "Deutsch":
    st.write(
        "Unten finden Sie verschiedene Websites von Organisationen, die in Ihrer Region aktiv sind und möglicherweise nützliche Ressourcen sowie Unterstützungshotlines anbieten."
    )

    # Nationale und Internationale Ressourcen
    st.write("### 🌍 **Nationale und Internationale Ressourcen**")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🇩🇪 Deutsche Ressourcen")
        if st.button("Verband alleinerziehender Mütter und Väter (DE)"):
            st.write("🔗 [Besuchen Sie die VAMV-Website](https://vamv.de/de/)")

        if st.button("AOK - Allgemeine Ortskrankenkasse (DE)"):
            st.write(
                "🔗 [Besuchen Sie die AOK-Website](https://www.aok.de/pk/magazin/familie/beziehung/alleinerziehende-muetter-und-vaeter-hier-finden-sie-hilfe/)"
            )

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("🇦🇹 Österreichische Ressourcen")
        if st.button("Alleinerziehend (AT)"):
            st.write("🔗 [Besuchen Sie Alleinerziehend.at](https://www.alleinerziehend.at/)")

    with col4:
        st.subheader("🇨🇭 Schweizer Ressourcen")
        if st.button("einelternfamilie (CH)"):
            st.write("🔗 [Besuchen Sie SVAMV.ch](https://svamv.ch/thema/)")

# Footer Note
st.write("---")
if language == "English":
    st.info(
        "These resources are carefully selected to provide support for single parents worldwide. They offer physical contact points as well as emergency phone numbers!"
    )
else:
    st.info(
        "Diese Ressourcen wurden sorgfältig ausgewählt, um Unterstützung für alleinerziehende Eltern weltweit bereitzustellen. Sie bieten physische Kontaktstellen sowie Notrufnummern!"
    )
