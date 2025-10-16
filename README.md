# Transcript Q&A
Transcript Q&A is a Python program that allows you to input PDFs of your transcript to then answer questions based on that information. 
This program is specifically for __computer science students__ attending __Stony Brook University__, as so far the sample space data used is limited to students within the CSE program.


## Installation
This program assumes you have downloaded the __Python__ programming language, which also comes with __pip__ package manager.


## Virtual Environment
It is recommended to run this program using a __virtual environment__ which can be achieved by the following

```
python -m venv env 
.env\Scripts\Activate
```

This also assumes you are running this program on a __Windows application__ 
It is also recommended to have the virtual environment in the __parent directory__ as it saves the trouble of creating a virtual environment in every folder. 


## Installing Packages
Once inside the virutal environment, you can then install the packages by the following

```
pip install -r requirements.txt
```


## Running the Program
The application is divided into __four__ separate components
- WebInterface 
- ParserService
- VDatabase
- QAService


### Web Interface
Where most of the users will be interacting with the program. Users are able to sign up, upload transcripts, and converse with an LLM that answers questions for them regarding the Transcript data. 

To run the client side
```
npm run dev
```

### Parser Service
When the user uploads the PDF of their transcript, this service will receive the document and parse the contents of it. This newly created data is then fed to VDatabase

To run this service
```
cd Apps\ParserService
python .\Main.py 
```

This will launch a FastAPI server on __http://127.0.0.1:8000__


### VDatabase
The newly parsed data is fed onto the a vector database known as __ChromaDB__ where it is used by the LLM in the QAService. 

To run this service
```
cd Apps\Database
python .\Main.py 
```

This will launch a FastAPI server on __http://127.0.0.1:8001__

### QA Service
This service utilizes Anthropic's API key to establish connection with Claude. 

To use this service, __you will need to provide your own API key from Anthropic OR from another organization__ 

Once you have the API key, create a __.env__ file in the __QAService directory__ where you write the following

```
cd Apps\QAService
New-Item .env 
API_KEY=<API-KEY-VALUE>
```

After that, you can then run the service as follows

```
python .\Main.py
```

This will launch a FastAPI server on __http://127.0.0.1:8002__

## Docker Installation

Coming Soon...



