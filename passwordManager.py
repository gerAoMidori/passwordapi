import string
import random
import re

class PassWordManager:
    def __init__(self):
        pass
    
    def get_numbers(self, total, n):
        lu = []
        for i in range(n - 1):
            val = random.randint(1, total//2)
            lu.append(val)
            total = total - val
        lu.append(total)
        return lu
    
    def create(self, length, number_of_types, upper, digits, special):
        """length (integer) : The length of the password"
        number_of_types (integer) : The different types of caracters we have (The minimum is 1(lowercase) and the maximum is 4)
        upper (boolean) : If we have uppercase letters
        digits (boolean) : If we have numerbers
        special (boolean) : If we have punctuations
        """
        items = []
        if number_of_types >= 2:
            vals = self.get_numbers(length, number_of_types)
            items += random.sample(string.ascii_lowercase, vals[0])
            vals.pop(0)
            if upper:
                items += random.sample(string.ascii_uppercase, vals[0])
                vals.pop(0)
            if digits:
                items += random.choices(string.digits, k = vals[0])
                vals.pop(0)
            if special:
                items += random.sample(string.punctuation, vals[0])
                vals.pop(0)
        else:
            items = random.sample(string.ascii_lowercase, length)
        
        random.shuffle(items)
        items_to_str =  map(str, items)
        password = "".join(items_to_str)

        return password
    

    def check_strength(self, password):

        if len(password) <= 6:
            return "Very Weak"
            
        if re.match(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9]).{8,}$', password):
            return "Strong"

        elif re.match(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])$.{8,}', password):
            return "Medium"
        
        elif re.match(r'(?=.*[a-z])(?=.*\d).{7,}$', password) or re.match(r'^(?=.*[A-Za-z])(?=.*[^A-Za-z0-9]).{7,}$', password):
            return "Weak"
        
        return "Weak"