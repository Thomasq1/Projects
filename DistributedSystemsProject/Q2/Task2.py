import copy
import threading


#Recipe class using the values name ingredients and process to create a recipe object
class Recipe:
    def __init__(self, name, ingredients, process):
        self.name = name
        self.ingredients = ingredients
        self.process = process
    #clone function to create different recipe objects as needed
    def clone(self):
        return copy.deepcopy(self)
    # return string to display the item object in the terminal
    def __str__(self):
        return f"Recipe: {self.name} Ingredients: {self.ingredients} Process: {self.process}"
    #createrecipe function takes 3 input arguments and then creates a recipe object using those arguments
def createRecipe(name, ingredients, process):
    return Recipe(name, ingredients, process)
#clonerecipe uses the clone fucntion to clone the recipe and make changes to its values and then prints the output
def clonerecipe(recipe: Recipe):
    clone = recipe.clone()
    clone.name = "CornFlakes"
    clone.ingredients = ["CornFlakes", "Milk"]
    print(clone)
    

    
if __name__ == '__main__':
#in the main i create a cereal object before using threads to make a cloneof the recipe object and modifying it.
    cereal = createRecipe("Cereal",["cereal,milk"],["add cereal to a bowl", "add milk", "enjoy"])
    print(cereal)
    t1 = threading.Thread(target=clonerecipe(cereal))
    t1.start()
    t1.join()
    
    
