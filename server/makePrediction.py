def make_prediction(users):
  FACTORS = 5

  cuisines = []
  time_of_day = []
  time_of_year = []
  price_point = []
  lat_ = []
  long_ = []

  unique_tags = []

  tot_category_sum = {}
  for i in range(len(users)):
    curr = users[i]

    for key,value in curr["category_scores"].items():
      if key in tot_category_sum:
        tot_category_sum[key] += value
      else:
        tot_category_sum[key] = value

  sorted_sums = []
  for k,v in tot_category_sum.items():
    sorted_sums.append((k,v))

  sorted_sums = sorted(sorted_sums, key = lambda x: x[1])
  sorted_sums.reverse()
  NUM_TOP = 3
  top_categories = [str(cuisine[0]) for cuisine in sorted_sums[:NUM_TOP]]

  return top_categories