---
layout: default
title: WFD
description: Plan your meals and browse family recipes by meal and cuisine.
permalink: /wfd/
---

<link rel="stylesheet" href="{{ '/assets/wfd.css' | relative_url }}?v={{ site.time | date: '%s' }}">

# What's For Dinner

What's for dinner? It's the million-dollar question that affects so many households—often before breakfast
is even over. Let chance help with the menu, then browse the recipes below for inspiration.

## Plan your meals

<form id="meal-planner" class="wfd-form">
  <fieldset>
    <legend>Which meals should we plan?</legend>
    <div class="wfd-meal-options">
      <label><input type="checkbox" name="meal" value="breakfast"> Breakfast</label>
      <label><input type="checkbox" name="meal" value="lunch"> Lunch</label>
      <label><input type="checkbox" name="meal" value="dinner" checked> Dinner</label>
    </div>
  </fieldset>
  <div class="wfd-day-options">
    <label for="plan-days">Number of days</label>
    <input id="plan-days" name="days" type="number" min="1" max="31" value="7" required>
    <label><input name="startToday" type="checkbox"> Start from today</label>
  </div>
  <button type="submit">Generate meal plan</button>
  <p class="meta">Choose 1–31 days. Generate again for a fresh set of ideas.</p>
</form>
<p id="planner-status" role="status" aria-live="polite"></p>
<div id="planner-results" class="wfd-results" hidden>
  <section aria-labelledby="meal-plan-title">
    <h2 id="meal-plan-title">Your meal plan</h2>
    <div id="meal-plan"></div>
  </section>
  <section aria-label="Ingredients needed">
    <div id="plan-ingredients"></div>
  </section>
</div>
<noscript>Enable JavaScript to generate a meal plan. You can still browse all the recipes below.</noscript>

## Recipe directory

Browse by meal, then cuisine. Lunch and dinner share a section; sides and desserts are included
for rounding out your menu.

{% assign recipes = site.pages | where: 'layout', 'recipe' | sort: 'title' %}
{% assign meals = 'breakfast,lunch-dinner' | split: ',' %}
<div class="directory-page directory-container">
  {% for meal in meals %}
    <h2>{% if meal == 'breakfast' %}Breakfast{% else %}Lunch and Dinner{% endif %}</h2>
    {% assign cuisines = recipes | group_by: 'cuisine' | sort: 'name' %}
    {% for cuisine in cuisines %}
      {% assign has_meal = false %}
      {% for recipe in cuisine.items %}
        {% if meal == 'breakfast' %}
          {% if recipe.type contains 'breakfast' %}{% assign has_meal = true %}{% endif %}
        {% elsif recipe.type contains 'lunch' or recipe.type contains 'dinner' %}
          {% assign has_meal = true %}
        {% endif %}
      {% endfor %}
      {% if has_meal %}
        <div class="directory-section wfd-cuisine">
          <div class="section-title">{{ cuisine.name | escape }}</div>
          <div class="directory-links directory-links--3" style="--directory-columns: 3;">
            {% for recipe in cuisine.items %}
              {% assign matches_meal = false %}
              {% if meal == 'breakfast' %}
                {% if recipe.type contains 'breakfast' %}{% assign matches_meal = true %}{% endif %}
              {% elsif recipe.type contains 'lunch' or recipe.type contains 'dinner' %}
                {% assign matches_meal = true %}
              {% endif %}
              {% if matches_meal %}
                <div class="directory-entry">
                  <a href="{{ recipe.url | relative_url }}">[&nbsp;{{ recipe.title | escape }}&nbsp;]</a>
                </div>
              {% endif %}
            {% endfor %}
          </div>
        </div>
      {% endif %}
    {% endfor %}
  {% endfor %}
</div>

## Suggest a recipe / Fix

Have a household favorite or spotted something to fix? Share a recipe, a link, or a correction.
The button opens your email app with a draft addressed
to me, ready for you to review and send.

<form id="recipe-suggestion" class="wfd-form" data-email="{{ site.email | escape }}">
  <label for="suggestion-name">Recipe name</label>
  <input id="suggestion-name" name="recipe" type="text" maxlength="160" required>
  <fieldset>
    <legend>When would you serve it?</legend>
    <div class="wfd-meal-options">
      <label><input type="checkbox" name="meal" value="breakfast"> Breakfast</label>
      <label><input type="checkbox" name="meal" value="lunch"> Lunch</label>
      <label><input type="checkbox" name="meal" value="dinner"> Dinner</label>
    </div>
  </fieldset>
  <label for="suggestion-cuisine">Cuisine (optional)</label>
  <input id="suggestion-cuisine" name="cuisine" type="text" maxlength="100">
  <label for="suggestion-details">Recipe, link, or correction</label>
  <textarea id="suggestion-details" name="details" rows="5" maxlength="6000" required></textarea>
  <button type="submit">Suggest a recipe / Fix by email</button>
</form>
<p id="suggestion-status" role="status" aria-live="polite"></p>
<noscript>Email your suggestion to <a href="mailto:{{ site.email }}">{{ site.email }}</a>.</noscript>

<script id="wfd-basic-ingredients" type="application/json">
{{ site.data.basic_ingredients | jsonify }}
</script>
<script id="wfd-recipes" type="application/json">
[
{% for recipe in recipes %}
  {% assign recipe_html = recipe.content | markdownify %}
  {% assign ingredients = recipe_html | split: '<h2 id="ingredients">Ingredients</h2>' | last
    | split: '<h2' | first %}
  {
    "title": {{ recipe.title | jsonify }},
    "url": {{ recipe.url | relative_url | jsonify }},
    "type": {{ recipe.type | jsonify }},
    "ingredients": {{ ingredients | jsonify | replace: '<', '\u003c' }},
    "basic_ingredients": {% if recipe.basic_ingredients %}{{ recipe.basic_ingredients | jsonify }}
      {% else %}[]{% endif %},
    "planner": {% if recipe.planner == false %}false{% else %}true{% endif %}
  }{% unless forloop.last %},{% endunless %}
{% endfor %}
]
</script>
<script src="{{ '/assets/wfd.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
