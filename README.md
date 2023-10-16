# t5-streamlit

**T5 (Text-To-Text Transfer Transformer)** is a family of models developed by Google AI and it is designed for various natural langugage understanding and generating tasks. It has been pre-trained on large language corpus and fine-tuned for different NLP tasks. **T5-small** variant is a light-weight version of the T5 model and it is created for handling tasks with less computational calculation and memory consumption. With less parameters, T5-sall is more easily to be deployed for usage and that is the reason we are using t5-small in this project to tacke specific domain questions.


## Retrieving FDA data
From the [Drug API Endpoints](https://open.fda.gov/apis/drug/event/), there are different categories, including adverse events, product labeling, NDC directory, recall enforcement reports, and Drugs@FDA. 