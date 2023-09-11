from bs4 import BeautifulSoup
import requests
Optimized Python script:


class RecipeScraper:
    @staticmethod
    def scrape_recipe_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            recipe_title = soup.select_one('.recipe-title').get_text()
            ingredient_list = [ingredient.get_text()
                               for ingredient in soup.select('.ingredient li')]
            instructions = [step.get_text()
                            for step in soup.select('.step div')]
            return recipe_title, ingredient_list, instructions
        except requests.exceptions.HTTPError as e:
            print('Failed to scrape recipe data:', e)


def main():
    url = 'https://example.com'
    recipe_title, ingredient_list, instructions = RecipeScraper.scrape_recipe_data(
        url)
    NutritionAnalyzer.analyze_nutritional_info(ingredient_list)
    RecipeGenerator.generate_sustainable_recipe()
    ShoppingListGenerator.generate_shopping_list(ingredient_list)
    UserFeedback.get_user_feedback()
    MealPlanningIntegration.integrate_with_meal_planning()


if __name__ == '__main__':
    main()
