import streamlit as st

# Language selection
st.sidebar.title("Language / Sprache / Idioma")
language = st.sidebar.radio(
    "Choose language / Sprache wählen / Seleccione idioma",
    ("English", "Deutsch", "Español")
)

# Translations dictionary
texts = {
    "English": {
        "title": "AUA Hematuria Guidelines Tool (Micro- & Gross Hematuria, 2025 Update)",
        "subtitle": "Interactive decision support based on AUA/SUFU Microhematuria Guideline (2025) and standard evaluation for Gross Hematuria",
        "info": "Educational purposes only • Source: auanet.org/guidelines/microhematuria",
        "select_type": "Select Hematuria Type",
        "micro": "Microhematuria (≥3 RBC/HPF on microscopy, not visible)",
        "gross": "Gross Hematuria (visible blood in urine)",
        "micro_title": "AUA/SUFU Microhematuria Diagnostic Algorithm (2025)",
        "gross_title": "Evaluation of Gross (Visible) Hematuria",
        "confirm_mh": "Patient has confirmed microhematuria (≥3 RBC/HPF on a single properly collected specimen)",
        "benign_causes": "Initial Evaluation: Rule out benign causes (e.g., UTI, menstruation, vigorous exercise, medical renal disease)",
        "benign_radio": "Was a benign cause identified and resolved?",
        "benign_no": "No",
        "benign_resolved_neg": "Yes - resolved, repeat UA negative",
        "benign_resolved_persist": "Yes - resolved, but microhematuria persists",
        "no_further": "No further urologic evaluation needed at this time.",
        "proceed_risk": "Proceed to risk stratification.",
        "risk_strat": "Risk Stratification (2025 Update)",
        "risk_explain": "Select patient factors. Risk is determined exactly per the 2025 AUA guideline criteria.",
        "age": "Age (years)",
        "sex": "Sex",
        "female": "Female",
        "male": "Male",
        "smoking": "Smoking history (pack-years)",
        "never": "Never / <10 pack-years",
        "former10_30": "10-30 pack-years",
        "current_or_more30": ">30 pack-years or current smoker",
        "degree": "Degree of microhematuria (highest RBC/HPF)",
        "low_degree": "3-10 RBC/HPF",
        "mid_degree": "11-25 RBC/HPF",
        "high_degree": ">25 RBC/HPF",
        "gross_history": "History of gross hematuria",
        "prior_malignancy": "Prior urothelial carcinoma",
        "additional": "Additional risk factors (e.g., irritative LUTS, pelvic radiation, cyclophosphamide, heavy occupational exposures)",
        "risk_category": "Risk Category (per 2025 AUA Guideline)",
        "low": "Low/Negligible Risk",
        "intermediate": "Intermediate Risk",
        "high": "High Risk",
        "recommend_low": """
        - Repeat urinalysis within 6-12 months.
        - If negative → no further evaluation.
        - If persistent → shared decision-making regarding cystoscopy and/or imaging.
        - Do not use urine-based tumor markers (UBTM) or cytology to decide on cystoscopy.
        """,
        "recommend_inter": """
        - Preferred: Cystoscopy + renal ultrasound.
        - Upper tract imaging: Axial imaging (CT urogram preferred if no contraindications).
        - Alternative (shared decision-making): In patients wishing to avoid cystoscopy, may use validated UBTM (e.g., Cxbladder Triage) or cytology for further stratification.
          - If negative → may defer cystoscopy; perform ultrasound; repeat UA in 12 months.
          - If positive → proceed to cystoscopy.
        """,
        "recommend_high": """
        - Mandatory cystoscopy.
        - Upper tract imaging: Multiphasic CT urogram (preferred); MRI urogram if contrast contraindicated.
        - Do not use UBTM or cytology to defer cystoscopy.
        """,
        "follow_up": "Follow-up After Negative Evaluation",
        "follow_up_text": """
        - Shared decision-making regarding repeat urinalysis (e.g., annually or based on symptoms).
        - Prompt re-evaluation if new gross hematuria, significant increase in microhematuria, or new symptoms.
        """,
        "gross_eval": "First, rule out benign causes (infection, trauma, etc.).",
        "gross_recommend": """
        Gross hematuria carries higher malignancy risk (~10-20%).

        Full urologic evaluation recommended (no risk stratification):
        - **Cystoscopy** (mandatory in adults).
        - **Upper tract imaging**: Multiphasic CT urogram (preferred).
        - Consider urine cytology (especially with risk factors for urothelial cancer, e.g., smoking).
        """,
        "gross_follow": "If initial evaluation negative: Shared decision-making for surveillance (e.g., annual UA ± cytology). Prompt re-evaluation for recurrent gross hematuria.",
        "disclaimer": "This tool is for educational use only and closely follows the 2025 AUA guideline. Always consult the full guideline and use clinical judgment.",
        "algo_image": "Official 2025 AUA Microhematuria Diagnostic Algorithm",
        "gross_algo": "Example Gross Hematuria Evaluation Algorithm (general approach)",
    },
    "Deutsch": {
        "title": "AUA Hämaturie-Leitlinien-Tool (Mikro- & Makrohämaturie, Update 2025)",
        "subtitle": "Interaktives Entscheidungshilfe-Tool basierend auf der AUA/SUFU Mikrohämaturie-Leitlinie (2025) und Standardabklärung bei Makrohämaturie",
        "info": "Nur zu Ausbildungszwecken • Quelle: auanet.org/guidelines/microhematuria",
        "select_type": "Art der Hämaturie auswählen",
        "micro": "Mikrohämaturie (≥3 Ery/HPF mikroskopisch, nicht sichtbar)",
        "gross": "Makrohämaturie (sichtbares Blut im Urin)",
        "micro_title": "AUA/SUFU Diagnostikalgorithmus Mikrohämaturie (2025)",
        "gross_title": "Abklärung der Makrohämaturie (sichtbares Blut)",
        "confirm_mh": "Patient hat bestätigte Mikrohämaturie (≥3 Ery/HPF in einer ordnungsgemäß gesammelten Probe)",
        "benign_causes": "Erstuntersuchung: Benigne Ursachen ausschließen (z. B. HWI, Menstruation, intensiver Sport, medizinische Nierenerkrankung)",
        "benign_radio": "Wurde eine benigne Ursache gefunden und behoben?",
        "benign_no": "Nein",
        "benign_resolved_neg": "Ja – behoben, Kontroll-UA negativ",
        "benign_resolved_persist": "Ja – behoben, aber Mikrohämaturie persistiert",
        "no_further": "Keine weitere urologische Abklärung nötig.",
        "proceed_risk": "Weiter zur Risikostratifizierung.",
        "risk_strat": "Risikostratifizierung (Update 2025)",
        "risk_explain": "Patientenfaktoren auswählen. Das Risiko wird exakt nach den Kriterien der AUA-Leitlinie 2025 bestimmt.",
        "age": "Alter (Jahre)",
        "sex": "Geschlecht",
        "female": "Weiblich",
        "male": "Männlich",
        "smoking": "Rauchanamnese (Packungsjahre)",
        "never": "Nie / <10 Packungsjahre",
        "former10_30": "10-30 Packungsjahre",
        "current_or_more30": ">30 Packungsjahre oder aktueller Raucher",
        "degree": "Grad der Mikrohämaturie (höchster Ery/HPF)",
        "low_degree": "3-10 Ery/HPF",
        "mid_degree": "11-25 Ery/HPF",
        "high_degree": ">25 Ery/HPF",
        "gross_history": "Anamnese von Makrohämaturie",
        "prior_malignancy": "Vorheriges Urothelkarzinom",
        "additional": "Zusätzliche Risikofaktoren (z. B. irritative LUTS, Beckenbestrahlung, Cyclophosphamid, starke berufliche Expositionen)",
        "risk_category": "Risikokategorie (gemäß AUA-Leitlinie 2025)",
        "low": "Niedrig/Negligibles Risiko",
        "intermediate": "Intermediäres Risiko",
        "high": "Hohes Risiko",
        "recommend_low": """
        - Urinuntersuchung in 6-12 Monaten wiederholen.
        - Bei negativ → keine weitere Abklärung.
        - Bei persistierend → gemeinsame Entscheidung über Zystoskopie und/oder Bildgebung.
        - Keine Urintumormarker oder Zytologie zur Entscheidung über Zystoskopie verwenden.
        """,
        "recommend_inter": """
        - Bevorzugt: Zystoskopie + Nierensonografie.
        - Bildgebung oberer Harnwege: Axiale Bildgebung (CT-Urogramm bevorzugt, wenn keine Kontraindikationen).
        - Alternativ (gemeinsame Entscheidung): Bei Patienten, die Zystoskopie vermeiden möchten, validierte Urintumormarker (z. B. Cxbladder Triage) oder Zytologie zur weiteren Stratifizierung einsetzen.
          - Bei negativ → Zystoskopie ggf. aufschieben; Sonografie durchführen; UA in 12 Monaten wiederholen.
          - Bei positiv → Zystoskopie durchführen.
        """,
        "recommend_high": """
        - Obligate Zystoskopie.
        - Bildgebung oberer Harnwege: Multiphasisches CT-Urogramm (bevorzugt); MRI-Urogramm bei Kontrastmittel-Kontraindikation.
        - Marker/Zytologie nicht verwenden, um Zystoskopie aufzuschieben.
        """,
        "follow_up": "Nachsorge nach negativer Abklärung",
        "follow_up_text": """
        - Gemeinsame Entscheidung über wiederholte Urinkontrollen (z. B. jährlich oder symptomabhängig).
        - Rasche Reevaluation bei neuer Makrohämaturie, deutlicher Zunahme der Mikrohämaturie oder neuen Symptomen.
        """,
        "gross_eval": "Zuerst benigne Ursachen (Infekt, Trauma etc.) ausschließen.",
        "gross_recommend": """
        Makrohämaturie hat ein höheres Malignitätsrisiko (~10-20%).

        Vollständige urologische Abklärung empfohlen (keine Risikostratifizierung):
        - **Zystoskopie** (obligat bei Erwachsenen).
        - **Bildgebung oberer Harnwege**: Multiphasisches CT-Urogramm (bevorzugt).
        - Urinzytologie in Betracht ziehen (besonders bei Risikofaktoren für Urothelkarzinom, z. B. Rauchen).
        """,
        "gross_follow": "Bei negativer Erstabklärung: Gemeinsame Entscheidung über Surveillance (z. B. jährlicher UA ± Zytologie). Rasche Reevaluation bei rezidivierender Makrohämaturie.",
        "disclaimer": "Dieses Tool dient nur zu Ausbildungszwecken und folgt eng der AUA-Leitlinie 2025. Immer die vollständige Leitlinie konsultieren und klinisches Urteil anwenden.",
        "algo_image": "Offizieller AUA Mikrohämaturie-Diagnostikalgorithmus 2025",
        "gross_algo": "Beispiel-Algorithmus zur Abklärung der Makrohämaturie (allgemeiner Ansatz)",
    },
    "Español": {
        "title": "Herramienta AUA para Hematuria (Micro y Macrohematuria, Actualización 2025)",
        "subtitle": "Apoyo interactivo a la decisión basado en la Guía AUA/SUFU de Microhematuria (2025) y evaluación estándar de hematuria visible",
        "info": "Solo con fines educativos • Fuente: auanet.org/guidelines/microhematuria",
        "select_type": "Seleccionar tipo de hematuria",
        "micro": "Microhematuria (≥3 hematíes/CAM en microscopía, no visible)",
        "gross": "Macrohematuria (sangre visible en orina)",
        "micro_title": "Algoritmo Diagnóstico AUA/SUFU de Microhematuria (2025)",
        "gross_title": "Evaluación de Macrohematuria (sangre visible)",
        "confirm_mh": "El paciente tiene microhematuria confirmada (≥3 hematíes/CAM en una muestra recogida correctamente)",
        "benign_causes": "Evaluación inicial: descartar causas benignas (p. ej., ITU, menstruación, ejercicio intenso, enfermedad renal médica)",
        "benign_radio": "¿Se identificó y resolvió una causa benigna?",
        "benign_no": "No",
        "benign_resolved_neg": "Sí – resuelta, análisis de orina repetido negativo",
        "benign_resolved_persist": "Sí – resuelta, pero persiste la microhematuria",
        "no_further": "No es necesaria más evaluación urológica en este momento.",
        "proceed_risk": "Proceder a la estratificación de riesgo.",
        "risk_strat": "Estratificación de riesgo (Actualización 2025)",
        "risk_explain": "Seleccionar factores del paciente. El riesgo se determina exactamente según los criterios de la guía AUA 2025.",
        "age": "Edad (años)",
        "sex": "Sexo",
        "female": "Mujer",
        "male": "Hombre",
        "smoking": "Historia tabáquica (paquetes-año)",
        "never": "Nunca / <10 paquetes-año",
        "former10_30": "10-30 paquetes-año",
        "current_or_more30": ">30 paquetes-año o fumador actual",
        "degree": "Grado de microhematuria (máximo hematíes/CAM)",
        "low_degree": "3-10 hematíes/CAM",
        "mid_degree": "11-25 hematíes/CAM",
        "high_degree": ">25 hematíes/CAM",
        "gross_history": "Antecedente de macrohematuria",
        "prior_malignancy": "Carcinoma urotelial previo",
        "additional": "Factores de riesgo adicionales (p. ej., síntomas irritativos de vías urinarias bajas, radioterapia pélvica, ciclofosfamida, exposiciones ocupacionales intensas)",
        "risk_category": "Categoría de riesgo (según Guía AUA 2025)",
        "low": "Riesgo Bajo/Negligible",
        "intermediate": "Riesgo Intermedio",
        "high": "Alto Riesgo",
        "recommend_low": """
        - Repetir análisis de orina en 6-12 meses.
        - Si negativo → no más evaluación.
        - Si persiste → decisión compartida sobre cistoscopia y/o pruebas de imagen.
        - No utilizar marcadores tumorales urinarios ni citología para decidir sobre cistoscopia.
        """,
        "recommend_inter": """
        - Preferido: Cistoscopia + ecografía renal.
        - Imagen de tracto superior: Imagen axial (uro-TAC preferido si no hay contraindicaciones).
        - Alternativa (decisión compartida): En pacientes que deseen evitar cistoscopia, se puede usar marcador tumoral urinario validado (p. ej., Cxbladder Triage) o citología para mayor estratificación.
          - Si negativo → posible aplazamiento de cistoscopia; realizar ecografía; repetir análisis en 12 meses.
          - Si positivo → proceder a cistoscopia.
        """,
        "recommend_high": """
        - Cistoscopia obligatoria.
        - Imagen de tracto superior: Uro-TAC multifásico (preferido); uro-RM si contraindicación al contraste.
        - No usar marcadores ni citología para aplazar la cistoscopia.
        """,
        "follow_up": "Seguimiento tras evaluación negativa",
        "follow_up_text": """
        - Decisión compartida sobre repetición de análisis de orina (p. ej., anual o según síntomas).
        - Reevaluación rápida si aparece macrohematuria nueva, aumento significativo de microhematuria o nuevos síntomas.
        """,
        "gross_eval": "Primero, descartar causas benignas (infección, traumatismo, etc.).",
        "gross_recommend": """
        La macrohematuria conlleva mayor riesgo de malignidad (~10-20%).

        Se recomienda evaluación urológica completa (sin estratificación de riesgo):
        - **Cistoscopia** (obligatoria en adultos).
        - **Imagen de tracto urinario superior**: Uro-TAC multifásico (preferido).
        - Considerar citología urinaria (especialmente con factores de riesgo para carcinoma urotelial, p. ej., tabaquismo).
        """,
        "gross_follow": "Si la evaluación inicial es negativa: Decisión compartida sobre vigilancia (p. ej., análisis anual ± citología). Reevaluación rápida en caso de macrohematuria recurrente.",
        "disclaimer": "Esta herramienta es solo para uso educativo y sigue de cerca la guía AUA 2025. Consulte siempre la guía completa y aplique juicio clínico.",
        "algo_image": "Algoritmo Diagnóstico Oficial AUA Microhematuria 2025",
        "gross_algo": "Ejemplo de algoritmo de evaluación de macrohematuria (enfoque general)",
    }
}

t = texts[language]

st.set_page_config(page_title=t["title"], layout="centered")
st.title(t["title"])
st.markdown(f"**{t['subtitle']}**")
st.info(t["info"])

# Official Microhematuria Algorithm Image
st.subheader(t["algo_image"])
st.image(
    "https://www.auajournals.org/cms/asset/ef1b4ed4-cd21-47d9-ac70-c0b061e4c18a/ju.0000000000004490f1.gif",
    use_column_width=True
)

hematuria_type = st.radio(t["select_type"], (t["micro"], t["gross"]))

if hematuria_type == t["micro"]:
    st.header(t["micro_title"])

    confirmed_mh = st.checkbox(t["confirm_mh"])
    if not confirmed_mh:
        st.stop()

    st.subheader(t["benign_causes"])
    benign_cause = st.radio(
        t["benign_radio"],
        (t["benign_no"], t["benign_resolved_neg"], t["benign_resolved_persist"])
    )

    if benign_cause == t["benign_resolved_neg"]:
        st.success(t["no_further"])
        st.stop()
    elif benign_cause == t["benign_resolved_persist"]:
        st.warning(t["proceed_risk"])

    st.header(t["risk_strat"])
    st.markdown(t["risk_explain"])

    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input(t["age"], min_value=0, max_value=120, value=50)
        sex = st.selectbox(t["sex"], [t["female"], t["male"]])
        smoking = st.selectbox(t["smoking"], [t["never"], t["former10_30"], t["current_or_more30"]])
        degree = st.selectbox(t["degree"], [t["low_degree"], t["mid_degree"], t["high_degree"]])

    with col2:
        prior_gross = st.checkbox(t["gross_history"])
        prior_uc = st.checkbox(t["prior_malignancy"])
        additional = st.checkbox(t["additional"])

    # Precise 2025 AUA risk stratification logic
    if prior_gross or prior_uc:
        risk_category = t["high"]
    elif smoking == t["current_or_more30"]:
        risk_category = t["high"]
    elif degree == t["high_degree"]:
        risk_category = t["high"]
    elif sex == t["male"] and age >= 60:
        risk_category = t["high"]
    elif (additional and (degree in [t["mid_degree"], t["high_degree"]] or smoking != t["never"])):
        risk_category = t["high"]
    elif (sex == t["female"] and age >= 60) or (sex == t["male"] and 40 <= age < 60):
        risk_category = t["intermediate"]
    elif smoking == t["former10_30"]:
        risk_category = t["intermediate"]
    elif degree == t["mid_degree"]:
        risk_category = t["intermediate"]
    elif additional:
        risk_category = t["intermediate"]
    else:
        risk_category = t["low"]

    st.subheader(f"{t['risk_category']}: **{risk_category}**")

    st.header("Recommended Evaluation / Empfohlene Abklärung / Evaluación recomendada")
    if risk_category == t["low"]:
        st.success(t["recommend_low"])
    elif risk_category == t["intermediate"]:
        st.warning(t["recommend_inter"])
    elif risk_category == t["high"]:
        st.error(t["recommend_high"])

    st.header(t["follow_up"])
    st.markdown(t["follow_up_text"])

else:  # Gross Hematuria
    st.header(t["gross_title"])
    st.markdown(t["gross_eval"])
    st.image(
        "https://www.researchgate.net/publication/50271801/figure/fig1/AS:340599485026312@1458216653435/Adult-hematuria-workup-algorithm-C-S-culture-and-sensitivity-e-gfr-estimated.png",
        caption=t["gross_algo"],
        use_column_width=True
    )
    st.error(t["gross_recommend"])
    st.markdown(t["gross_follow"])

st.caption(t["disclaimer"])
