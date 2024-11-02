import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader

GROQ_API_KEY="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"
api_key=GROQ_API_KEY
llm=ChatGroq(groq_api_key=api_key,model="Gemma-7b-It")

## Streamlit App
st.set_page_config(page_title="Langchain: Summarize Text from YT or Website",page_icon="Langchain")
st.title("Langchain: Summarize Text from YT or Website")
st.subheader('Summarize URL')


## Get the Groq API key and url(YT or Website) to be summarized
with st.sidebar:
    groq_api_key=st.text_input("GROQ_API_KEY",value="",type="password")

generic_url=st.text_input("URL",label_visibility="collapsed")

## Gemma model using Groq API
#llm=ChatGroq(model="Gemma-7b-It",groq_api_key=groq_api_key)

prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}

"""
prompt=PromptTemplate(template=prompt_template,input_variables=['text'])

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid url. It can may be a YT video URL or website url")
    else:
        try:
            with st.spinner("Waiting....."):
                ## loading the website or yt video data
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info = True)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,
                                                 headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()

                ## Chain for summarization
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)

                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception:{e}")

