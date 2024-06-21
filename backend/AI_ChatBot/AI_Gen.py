from g4f.client import Client


def Reply(client: Client ,message: str)->str:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content
