import streamlit as st
import pubchempy as pcp

def check_chemical_property(input_string):
    chemical_info = {
        "CommonName": None,
        "ChemicalName": None,
        "SMILES": None
    }

    # Determine the type of input (common name, chemical name, or SMILES)
    search_type = None
    if input_string.isalpha():
        search_type = 'name'  # Common name
    elif '=' in input_string:
        search_type = 'smiles'  # SMILES notation
    else:
        search_type = 'iupac_name'  # Chemical name

    # Try to search for the chemical compound
    compounds = pcp.get_compounds(input_string, search_type)

    if compounds:
        compound = compounds[0]
        chemical_info["CommonName"] = compound.synonyms[0] if compound.synonyms else None
        chemical_info["ChemicalName"] = compound.iupac_name
        chemical_info["SMILES"] = compound.isomeric_smiles

    # display
    data = []
    for key, value in chemical_info.items():
        data.append({"Properties": key, "Value": value})
    
    return data

def check_antifungal(chemical_name):
    # Replace this with your logic to check if the chemical is related to anti-fungal properties.
    return True  # Sample logic for demonstration

def check_candida_auris(chemical_name):
    # Replace this with your logic to check if the chemical is related to Candida auris.
    return False  # Sample logic for demonstration

def anti_checker_page():
    st.title("Chemical Property Checker for Candida auris")

    chemical_name = st.text_input("Enter the chemical name:", placeholder="aspirin")
    enter_name = ""
    
    if st.button("Check") or (chemical_name != enter_name):
        if not chemical_name:
            st.warning("Please enter a chemical name.")
        else:
            chemical_output_dict = check_chemical_property(chemical_name)
            st.table(chemical_output_dict)
            
            antifungal_result = check_antifungal(chemical_name)
            candida_auris_result = check_candida_auris(chemical_name)

            if antifungal_result:
                st.success(f"{chemical_name} is related to anti-fungal properties.")
            else:
                st.error(f"{chemical_name} is not related to anti-fungal properties.")

            if candida_auris_result:
                st.success(f"{chemical_name} is related to Candida auris.")
            else:
                st.error(f"{chemical_name} is not related to Candida auris.")