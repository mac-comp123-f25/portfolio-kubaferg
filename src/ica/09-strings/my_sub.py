def name_subst(name, text):
   return text.replace("ZZZ", name)
result = name_subst("Amin", "My teacher ZZZ gave me chocolate")
print(result)
