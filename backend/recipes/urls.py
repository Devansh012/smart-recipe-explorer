from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView, SimplifyRecipeView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view()),
    path('recipes/<int:pk>/', RecipeDetailView.as_view()),
    path('ai/simplify/', SimplifyRecipeView.as_view()),  

]
