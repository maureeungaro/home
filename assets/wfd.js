/* The planner runs entirely in the browser; recipe suggestions open an email draft. */
(() => {
  "use strict";
  const recipes = JSON.parse(document.getElementById("wfd-recipes").textContent);
  const sharedBasics = new Set(JSON.parse(document.getElementById("wfd-basic-ingredients").textContent)
    .map(value => value.toLowerCase().trim()));
  const planner = document.getElementById("meal-planner");
  const output = document.getElementById("meal-plan");
  const status = document.getElementById("planner-status");
  const results = document.getElementById("planner-results");
  const ingredientsOutput = document.getElementById("plan-ingredients");
  const label = value => value.charAt(0).toUpperCase() + value.slice(1);
  const checkedMeals = form => Array.from(form.querySelectorAll('input[name="meal"]:checked'))
    .map(input => input.value);

  function shuffled(items) {
    const result = items.slice();
    for (let i = result.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
  }

  function shoppingIngredients(recipe) {
    const list = document.createElement("div");
    // This HTML comes from the Ingredients section rendered by Jekyll at build time.
    list.innerHTML = recipe.ingredients;
    const normalize = value => value.replace(/\s+/g, " ").trim().toLowerCase();
    const basics = new Set((recipe.basic_ingredients || []).map(normalize));
    const ingredientName = value => normalize(value)
      .replace(/,?\s+(?:to taste|for frying|for deep-frying|divided|optional|plus more.*|or the amount.*)$/, "")
      .replace(/^(?:a )?pinch of\s+/, "")
      .replace(/^\d+(?:[./]\d+)?\s*(?:(?:g|ml|l|teaspoons?|tablespoons?|cups?)\s+)?/, "")
      .replace(/^(?:extra-virgin|fine|flaky|coarsely ground|ground)\s+/, "")
      .replace(/^(?:whole|unsalted|salted|softened|melted|cold|warm|hot|lukewarm)\s+/, "")
      .trim();
    const isBasic = value => basics.has(normalize(value)) || sharedBasics.has(ingredientName(value));
    const omitAlternatives = value => {
      const parts = value.split(/\s+or\s+/);
      const needed = parts.filter(part => !isBasic(part));
      if (needed.length === parts.length) return value;
      if (!needed.length) return "";
      const quantity = value.match(/^\d+(?:[./]\d+)?\s*(?:(?:g|ml|l|teaspoons?|tablespoons?|cups?)\s+)?/);
      if (quantity && !/^\d/.test(needed[0])) needed[0] = quantity[0] + needed[0];
      return needed.join(" or ");
    };
    return Array.from(list.querySelectorAll("li")).map(item => {
      const text = item.textContent.replace(/\s+/g, " ").trim()
        .replace(/, soaked in (.+) and squeezed$/, (match, liquid) => isBasic(liquid) ? "" : match);
      if (isBasic(text)) return "";
      const parts = text.split(/,\s*|\s+and\s+/)
        .map(part => part.replace(/^and\s+/i, "").trim());
      const needed = parts.map(omitAlternatives).filter(Boolean);
      if (needed.length === parts.length && needed.every((part, index) => part === parts[index])) return text;
      return needed.filter(part => !/^(optional|divided|to taste)$/.test(part)).join(", ");
    }).filter(Boolean);
  }

  planner.addEventListener("submit", event => {
    event.preventDefault();
    const meals = checkedMeals(planner);
    const days = Number(planner.elements.days.value);
    if (!meals.length) {
      status.textContent = "Choose at least one meal.";
      return;
    }
    if (!Number.isInteger(days) || days < 1 || days > 31) {
      status.textContent = "Choose a whole number of days between 1 and 31.";
      return;
    }
    const pools = Object.fromEntries(meals.map(meal => [meal,
      recipes.filter(recipe => recipe.planner !== false && recipe.type.includes(meal))]));
    const missing = meals.filter(meal => !pools[meal].length);
    if (missing.length) {
      status.textContent = `No recipes available for ${missing.join(", ")}. Choose another meal.`;
      return;
    }
    const queues = Object.fromEntries(meals.map(meal => [meal, shuffled(pools[meal])]));
    const plan = document.createDocumentFragment();
    const selectedRecipes = new Map();
    const today = new Date();
    const dateFormat = new Intl.DateTimeFormat(undefined, {
      weekday: "long", month: "long", day: "numeric", year: "numeric"
    });
    for (let day = 1; day <= days; day++) {
      const section = document.createElement("section");
      section.className = "wfd-day";
      const heading = document.createElement("h3");
      if (planner.elements.startToday.checked) {
        const date = new Date(today.getFullYear(), today.getMonth(), today.getDate() + day - 1);
        heading.textContent = dateFormat.format(date);
      } else {
        heading.textContent = `Day ${day}`;
      }
      const list = document.createElement("ul");
      const used = new Set();
      for (const meal of meals) {
        if (!queues[meal].length) queues[meal] = shuffled(pools[meal]);
        const distinct = queues[meal].findIndex(recipe => !used.has(recipe.url));
        const recipe = queues[meal].splice(distinct < 0 ? 0 : distinct, 1)[0];
        used.add(recipe.url);
        selectedRecipes.set(recipe.url, recipe);
        const item = document.createElement("li");
        item.append(`${label(meal)}: `);
        const link = document.createElement("a");
        link.href = recipe.url;
        link.textContent = recipe.title;
        item.append(link);
        list.append(item);
      }
      section.append(heading, list);
      plan.append(section);
    }
    output.replaceChildren(plan);
    const ingredients = document.createDocumentFragment();
    for (const recipe of selectedRecipes.values()) {
      const section = document.createElement("section");
      section.className = "wfd-ingredient-recipe";
      const name = document.createElement("p");
      name.className = "wfd-ingredient-name";
      name.textContent = recipe.title;
      const list = document.createElement("ul");
      list.className = "wfd-ingredient-list";
      for (const text of shoppingIngredients(recipe)) {
        const item = document.createElement("li");
        item.textContent = text;
        list.append(item);
      }
      section.append(name, list);
      ingredients.append(section);
    }
    ingredientsOutput.replaceChildren(ingredients);
    results.hidden = false;
    status.textContent = `Your ${days}-day meal plan is ready. Follow a recipe link for ingredients and steps.`;
  });

  const suggestion = document.getElementById("recipe-suggestion");
  suggestion.addEventListener("submit", event => {
    event.preventDefault();
    const data = new FormData(suggestion);
    const title = data.get("recipe").trim();
    const details = data.get("details").trim();
    if (!title || !details) {
      document.getElementById("suggestion-status").textContent = "Enter a recipe name and its details.";
      return;
    }
    const body = [
      `Recipe: ${title}`,
      `Meals: ${checkedMeals(suggestion).join(", ") || "Not specified"}`,
      `Cuisine: ${data.get("cuisine").trim() || "Not specified"}`,
      "", details
    ].join("\n");
    window.location.href = `mailto:${suggestion.dataset.email}?subject=`
      + encodeURIComponent(`WFD recipe suggestion / fix: ${title}`) + "&body=" + encodeURIComponent(body);
    document.getElementById("suggestion-status").textContent =
      "Your email draft is ready to open. Review it in your email app and send it when ready.";
  });
})();
