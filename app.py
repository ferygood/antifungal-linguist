import streamlit as st
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw
from transformers import pipeline

st.set_page_config(page_title="Antifungal Linguist", 
                   page_icon="img/al_logo.png",
                   initial_sidebar_state="expanded")

generator = pipeline(model="yaochung/antifungal-linguist", task="text2text-generation")

# create tabs
tab1, tab2, tab3 = st.tabs(["Main", "Documentation", "TO-DO"])

with tab1:
  col1, col2 = st.columns([2,4])
  with col1:
    st.image("img/al_logo.png", use_column_width=True)
  with col2:
    content = """**Antifungal Linguist (AL)** is a language model designed for molecular screening. 
    It is fine-tuned using pre-trained T5-base model with distilling step-by-step. Currently 
    this beta version can handle antifungals against Candida auris, including *fluconazole, 
    nystatin, amphotericin* and non antifungals like *aspirin and ibuprofen*. AL aims to provide 
    service without LLM constraints such as large model size and api pricing but with similar/better 
    performances. Stay tune for more updates!
    """
    st.write(content)
    st.image("img/intro.png")
  
  # chemical input section
  def check_chemical_property(input_string):
    chemical_info = {
      "Common Name": None,
      "Chemical Name": None,
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
        chemical_info["Common Name"] = compound.synonyms[0] if compound.synonyms else None
        chemical_info["Chemical Name"] = compound.iupac_name
        chemical_info["SMILES"] = compound.isomeric_smiles

    # display
    data = []
    for key, value in chemical_info.items():
        data.append({"Properties": key, "Value": value})
    
    return data
  
  chemical_name = st.text_input("Enter the chemical name: ", placeholder="fluconazole")
  enter_name = ""

  if st.button("Check") or (chemical_name != enter_name):
    if not chemical_name:
        st.warning("Please enter a chemical name.")
    else:
        chemical_output_dict = check_chemical_property(chemical_name)
        st.table(chemical_output_dict)
        col3, col4 = st.columns([5,4])
        with col4:
          smiles = chemical_output_dict[2]["Value"] # get smile string

          if smiles:
          #convert SMILES to RDKit molecule
              molecule = Chem.MolFromSmiles(smiles)

          if molecule:
              img = Draw.MolToImage(molecule)
              st.image(img)
          else:
              st.warning("Invalid SMILES representation")

        with col3:
            # print model results
          antifungal = ["fluconazole", "nystatin", "amphotericin"]
          non_antifungal = ["aspirin", "ibuprofen"]

            # 1. create prompt sentence
          if chemical_name in antifungal:
            prompt = f"Is {chemical_name} associated with antifungal medicine and Candida auris?"
            result = generator(prompt, max_length=400)
            st.markdown('<p style="color:red; background-color:#FFD2D2; padding: 5px; border-radius: 5px;">Antifungal, related to Candida auris</p>', unsafe_allow_html=True)
            output_prompt = result[0]['generated_text'].capitalize()
            st.write(output_prompt)
          elif chemical_name in non_antifungal:
            prompt = f"Is {chemical_name} associated with antifungal medicine and Candida auris?"
            result = generator(prompt, max_length=400)
            st.markdown('<p style="color:red; background-color:#FFD2D2; padding: 5px; border-radius: 5px;">Non Antifungal, not related to Candida auris</p>', unsafe_allow_html=True)
            output_prompt = result[0]['generated_text'].capitalize()
            st.write(output_prompt)

with tab2:
   st.header("Contacts")
   st.markdown("Yao-Chung Chen, yao-chung.chen@fu-berlin.de ")
   st.markdown("Yu-Chia Ku, yucku@uni-mainz.de")

   st.header("References & Tools")
   st.markdown("[Distilling Step-By-Step](https://arxiv.org/abs/2305.02301) for fine-tuning")
   st.markdown("[T5-Base Model](https://arxiv.org/abs/1910.10683) as our pre-trained model")
   st.markdown("[Hugging Face Transformer](https://github.com/huggingface/transformers) for developing pipeline")
   st.markdown("[Model Checkpoint](https://huggingface.co/yaochung/antifungal-linguist) on Hugging Face")

with tab3:
   st.text("SMILES structure calculation and learning")
   st.text("ADMET and DMPK prediction")