import streamlit as st
from utils import generate_rednote

#sidebar
with st.sidebar:
    api_key = st.sidebar.text_input("输入你的阿里云百炼API密钥",type="password")
    st.markdown("[如何获取阿里云百炼的API密钥?](https://bailian.console.aliyun.com/?tab=model#/api-key)")

# main body
st.title("爆款小红书文案AI写作助手")
subject = st.text_input("输入你想要发表的主题,让AI帮你写作")
submitted = st.button("开始写作")

# check input and run
if submitted and not api_key:
    st.info("请输入你的API Key")
    st.stop()
if submitted and not subject:
    st.info("请输入生成内容的主题")
    st.stop()
if submitted:
    st.divider()
    with st.spinner("AI正在努力写作中，请稍等..."):
        result = generate_rednote(api_key, subject)
    st.divider()
    column1, column2 = st.columns([1,2])
    with column1:
        for i in range(5):
            st.markdown(f"** 参考标题{i+1} **")
            st.write(result.titles[i])
    with column2:
        st.markdown("** 参考正文 **")
        st.write(result.content)
    