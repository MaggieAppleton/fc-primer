from ice.recipe import recipe
import random


async def set_greeting():
    greetings = ["hello", "goodbye"]
    return random.choice(greetings)


async def say_greeting():
    greeting = await set_greeting()
    return f"{greeting}"


async def main():
    greeting = await say_greeting()
    print(greeting)

recipe.main(main)
