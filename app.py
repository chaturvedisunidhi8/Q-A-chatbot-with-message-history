import streamlit as st
#import openai
#from langchain_openai import ChatOpenAI
from langchain.llms import Ollama ##from langchain_community.llms import Ollama this is for new langchain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["langchain_api_key"] = os.getenv("langchain_api_key") ## to track the changes you can check it in langsmith website
os.environ["langchain_tracing_v2"] = "true"
os.environ["langchain_project"] = "Q/A chatbot with ollama"

##prompt template
prompt=ChatPromptTemplate(
    [
        ("system","you are a helpful assistant.Please response to the user queries"),
        ("user","Question:{question}")
    ]
)  
## In function api key refers to open ai api key which we are not using
##def generate_response(question,api_key,temperature,max_tokens):
def generate_response(question,temperature,max_tokens): ## value of temperature is set between 0-1 ,0--means model won't be much more creative w.r.t answers means if you ask same question multiple times it will give you same answer,and if it is 1 then vice versa    
    #openai.api_key=api_key
    llm=Ollama(model="gemma:2b")
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer

##title of app
st.title("Enhanced Q&A chatbot with openai/ollama ")

##sidebar for settings
st.sidebar.title("Settings")

##api_key=st.sidebar.text_input("Enter your OpenAI API key",type="password") beacuse we dont have open ai model api key

##dropdown to select various open ai models
llm=st.sidebar.selectbox("Select LLM model",["gpt-3.5-turbo","gpt-4","gemma:2b"])   
temperature=st.sidebar.slider("Select temperature",min_value=0.0,max_value=1.0,value=0.7,)
max_tokens=st.sidebar.slider("Select max tokens",min_value=50,max_value=300,value=150)

#main interface for user input
st.write("Go ahead and ask your question!")
user_input=st.text_input("You: ")
if user_input:
   #response=generate_response(user_input,api_key,temperature,max_tokens)
   response=generate_response(user_input,temperature,max_tokens)
   st.write("Bot: ",response)
else:
    st.write("Bot: Please enter your question.")



##here in environment variable we have not given any open ai key we have given openai api key in streamlit app


##Enter your OpenAI API key →
#This is required only if you select an OpenAI model (like gpt-3.5-turbo or gpt-4).
#The app uses the key to authenticate requests to the OpenAI API.
#Without it, OpenAI models won’t run.
#Select LLM model (gemma:2b in your case) →
#gemma:2b is a model from Ollama, which runs locally on your machine.
#Ollama models do not require an API key, since they don’t connect to OpenAI’s servers.

##✅ You must provide an OpenAI API key (because GPT-4 lives on OpenAI’s servers, not locally).
##Your app will connect over the internet to OpenAI’s API endpoint.
##The key is what authenticates your requests and bills usage.






