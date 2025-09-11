country_code = {'Netherlands' : '031',
                'Poland' : '048',
                'spain' : '034',}

print("Country code for  Poland 048")
print("Country code for  Netherlands 031")
print("Country code for  Spain 034")
print(country_code.get('japan','Not found')) 
print(country_code.get('India','Not found'))