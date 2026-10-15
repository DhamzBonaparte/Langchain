from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand      # Instance attribute
        self.model = model      # Instance attribute
        self.year = year        # Instance attribute
        self.is_running = False # Default state

    def start_engine(self):
        self.is_running = True
        return f"The {self.year} {self.brand} {self.model}'s engine is now running. Vroom!"

    def stop_engine(self):
        self.is_running = False
        return f"The {self.brand} {self.model} has been turned off."

car1 = Car("Toyota", "Corolla", 2022)
car2 = Car("Tesla", "Model 3", 2024)

print(car1.brand)                
print(car2.model)               

print(car1.start_engine())       
print(car2.stop_engine())       
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)

res = splitter.split_text(text)
print(res[0])
print(len(res))
