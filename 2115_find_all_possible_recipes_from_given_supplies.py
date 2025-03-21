# set and find
# there may be cycles in the graph
# so be-aware
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        d = {r: i for r, i in zip(recipes, ingredients)}
        def find(recipe, ingredient, v):
            for i in ingredient:
                if i in v:
                    return False
                if i not in supplies:
                    if i not in d:
                        return False
                    v.add(recipe)
                    if not find(i, d[i], v):
                        return False
                    v.discard(recipe)
            
            supplies.add(recipe)
            return True
        
        for recipe, ingredient in zip(recipes, ingredients):
            find(recipe, ingredient, set())
        
        return [r for r in recipes if r in supplies]