from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from RedNote_class import RedNote
from prompt_templates import system_template_text,user_template_text


def generate_rednote(api_key,subject):
    prompt_template = ChatPromptTemplate.from_messages(
        [
        ("system", system_template_text),
        ("user", user_template_text)
        ]
    )
    
    llm = ChatOpenAI(
        api_key = api_key,
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
        model = "deepseek-v3"
    )

    output_parser = PydanticOutputParser(pydantic_object=RedNote)
    instructions = output_parser.get_format_instructions()
    chain = prompt_template | llm | output_parser
    result = chain.invoke({
        "parser_instructions": instructions,
        "theme": subject
    })

    return result