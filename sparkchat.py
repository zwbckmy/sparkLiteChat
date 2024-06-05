from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import gradio as gr


#星火认知大模型Spark3.5 Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_URL = 'ws(s)://spark-api.xf-yun.com/v1.1/chat'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
SPARKAI_APP_ID = '2b33064a'
SPARKAI_API_SECRET = 'MmQyMjQ5Nzg4ZDE0OTI2NGZjMTczZDBl'
SPARKAI_API_KEY = '6ff2814e48994a22216b5ade62ad48b7'
#星火认知大模型Spark3.5 Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'general'

if __name__ == '__main2__':
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content='你好呀'
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    print(a)
    #print(type(a))
    #print(a.llm_output['token_usage'])
    #print(a.generations[0])
    print(a.generations[0][0])
    print(a.generations[0][0].text)

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("清除")


    def respond(message, chat_history):
        spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
        messages = [ChatMessage(
            role="user",
            content=message
        )]
        handler = ChunkPrintHandler()
        a = spark.generate([messages], callbacks=[handler])
        print(a.generations[0][0].text)
        chat_history.append((message, a.generations[0][0].text))
        return "", chat_history


    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

demo.launch()


