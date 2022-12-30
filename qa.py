from ice.recipe import recipe


DEFAULT_CONTEXT = "We're running a hackathon on 9/9/2022 to decompose complex reasoning tasks into subtasks that are easier to automate & evaluate with language models. Our team is currently breaking down reasoning about the quality of evidence in randomized controlled trials into smaller tasks e.g. placebo, intervention adherence rate, blinding procedure, etc."

DEFAULT_QUESTION = "What is happening on 9/9/2022?"


def make_prompt1(context: str, question: str) -> str:
    return f"""
Background text: "{context}"

Let’s think step by step. Answer the following question about the background text above:

Question: "{question}"
Answer: " 
""".strip()


def make_prompt2(context: str, question: str, initial_answer: str) -> str:
    return f"""
You are a helpful agent who is trying to answer the question: "{question}"

You have this background context: "{context}"

Here is a first attempt at answering the question: "{initial_answer}"

Please improve this answer.
Answer: " 
""".strip()


async def answer(
    context: str = DEFAULT_CONTEXT, question: str = DEFAULT_QUESTION
) -> str:
    prompt1 = make_prompt1(context, question)
    initial_answer = await recipe.agent().complete(prompt=prompt1, stop='"')
    prompt2 = make_prompt2(context, question, initial_answer)
    answer = await recipe.agent().complete(prompt=prompt2, stop='"')
    return answer

recipe.main(answer)
