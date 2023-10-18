# t5-streamlit

Start the project with creating a virtual environment

```shell
virtualenv t5-streamlit
pip install -r requirements.txt
```

**T5 (Text-To-Text Transfer Transformer)** is a family of models developed by Google AI and it is designed for various natural langugage understanding and generating tasks. It has been pre-trained on large language corpus and fine-tuned for different NLP tasks. **T5-small** variant is a light-weight version of the T5 model and it is created for handling tasks with less computational calculation and memory consumption. With less parameters, T5-sall is more easily to be deployed for usage and that is the reason we are using t5-small in this project to tacke specific domain questions.


## Retrieving FDA data
From the [Drug API Endpoints](https://open.fda.gov/apis/drug/event/), there are different categories, including adverse events, product labeling, NDC directory, recall enforcement reports, and Drugs@FDA. 
We get Drugs@FDA data from this [link](https://download.open.fda.gov/drug/drugsfda/drug-drugsfda-0001-of-0001.json.zip) and then we can retrieve substance information.

### Purple Book
The Purple Book is a database that contains information about all FDA-licensed biological products regulated by the Center for Drug Evaluation and Research (CDER), including licensed biosimilar and interchangeable products, and their reference products. The Purple Book also contains information on all FDA-licensed allergenic, cellular and gene therapy, hematologic, and vaccine products regulated by the Center for Biologics Evaluation and Research (CBER). [More Info](https://purplebooksearch.fda.gov/)

## DRUGBANK