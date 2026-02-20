import streamlit as st
from modules.feature_encoder import FeatureEncoder
from modules.stability_engine import StabilityEngine
from modules.ramachandran_rules import RamachandranValidator
from modules.energy_funnel import EnergyFunnel

st.title("🧬 ProFold-X: Protein Folding Stability Engine")

sequence = st.text_area("Enter Protein Sequence (FASTA without header)")

if st.button("Analyze Protein"):

    encoder = FeatureEncoder("data/amino_acids.csv")
    stability_engine = StabilityEngine()
    rama = RamachandranValidator()
    funnel = EnergyFunnel()

    features = encoder.encode_sequence(sequence.upper())
    st.subheader("Residue Features")
    st.dataframe(features)

    norm_score, raw_score = stability_engine.calculate_stability(features)
    st.subheader("Stability Score")
    st.write(f"Raw Score: {raw_score}")
    st.write(f"Normalized Stability Probability: {norm_score:.3f}")

    compliance = rama.validate(sequence.upper())
    st.subheader("Ramachandran Compliance")
    st.write(f"Compliance Score: {compliance:.2f}")

    fig = funnel.generate_funnel(raw_score)
    st.pyplot(fig)
