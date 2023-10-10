def linear_search_product(product_list,target_product):
  indices=[]
  for index,product in enumerate(product_list):
    if product==target_product:
      indices.append(index)
      return indices
#Example list of products
product=["apple","banana","orange","apple","grape"]
#Target product to search for
target_product="apple"
#perform linear search 
result=linear_search_product(product,target_product)
if result:
  print(f"the product'{target_product}'was found at indices:{result}")
else:
  print(f"the product'{target_product}'was not found in the list.")
