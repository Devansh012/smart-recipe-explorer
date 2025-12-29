from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        queryset = Recipe.objects.all()
        cuisine = self.request.query_params.get('cuisine')
        vegetarian = self.request.query_params.get('vegetarian')
        ingredient = self.request.query_params.get('ingredient')

        if cuisine:
            queryset = queryset.filter(cuisine__iexact=cuisine)

        if vegetarian:
            queryset = queryset.filter(is_vegetarian=vegetarian.lower() == 'true')

        if ingredient:
            queryset = queryset.filter(ingredients__contains=[ingredient])

        return queryset


class RecipeDetailView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


import os
from groq import Groq
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SimplifyRecipeView(APIView):
    def post(self, request):
        instructions = request.data.get("instructions")

        if not instructions:
            return Response(
                {"error": "Recipe instructions are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        prompt = (
            "Simplify the following recipe instructions for a beginner. "
            "Use short, clear steps:\n\n"
            f"{instructions}"
        )

        try:
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",  # ✅ UPDATED MODEL
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=150
            )

            simplified_text = completion.choices[0].message.content

            return Response(
                {"simplified_recipe": simplified_text},
                status=status.HTTP_200_OK
            )

        except Exception as e:
            return Response(
                {
                    "error": "AI service failed",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



