import os
from openai import OpenAI
from dotenv import load_dotenv

from gen_arr import parse_txt


load_dotenv()


ai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def gg():
    products = parse_txt()
    
    for product in products:
        print(product)

def gen_title(product):
    """
    prompt = f'Generiraj meta title za unaprijeđenje SEO-a za proizvod "{product}"'
    response = ai_client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user',
            'content': prompt
        }],
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5
    )
    """

    return f'Generiraj meta title za unaprijeđenje SEO-a za proizvod "{product}"'


if __name__ == '__main__':
    meta_title = gen_title('tava za palačinke')
    
    
    print(meta_title)
