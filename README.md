# t5-streamlit

Start the project by creating a virtual environment and installing all required packages

```shell
python3 -m venv myenv
pip install -r requirements.txt
```

**T5 (Text-To-Text Transfer Transformer)** is a family of models developed by Google AI and it is designed for various natural langugage understanding and generating tasks. It has been pre-trained on large language corpus and fine-tuned for different NLP tasks. 

In this project, we use [HuggingFace T5-base](https://huggingface.co/t5-base) and transformers to handle text input and generate text output.

First, we use [PubChemPy](https://pubchempy.readthedocs.io/en/latest/) package to analyze the text from user input. Users can type common name, chemical name, and [SMILE structure](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system), and we convert them to chemical name for our next steps.

Drug data was downloaded from [DrugBank](https://go.drugbank.com/) with the Academic License. The version of the data is 5.1.10 (2023-01-04 released). We then look for the user input from DrugBank table.


