from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Deep beneath the sunless waves of the open ocean, where the crushing pressure of the water would instantly flatten a submarine and the temperature hovers perpetually near freezing, strange and alien landscapes thrive around hydrothermal vents known as black smokers. Erupting from the Earth's crust like mineral-rich chimneys, these towering vents spew superheated water loaded with toxic hydrogen sulfide straight into the abyss at temperatures exceeding 400 degrees Celsius. In any ordinary environment, such extreme conditions would spell certain death; yet, rather than relying on photosynthesis driven by the sun, entire ecosystems here are built upon chemosynthesis. Specialized bacteria convert the noxious chemicals spewed from the Earth's interior into energy, serving as the foundational bedrock for bizarre, giant tube worms, blind shrimp, and pale crabs that have never seen a single ray of sunlight. This astonishing biological oasis reminds us that life is not merely a fragile byproduct of surface conditions, but a resilient, inventive force capable of carving out thriving civilizations in the most hostile, pitch-black corners of our planet.
"""

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
split = splitter.split_text(text)
print(split[0])
