"""
input: a number (num of pairs)
output: a string of valid parenthesis with length equal to the number
"""

def generate_balanced_parentheses(num_pairs):
    def directed_generate_balanced_parentheses(num_left_parens_needed,
                                               num_right_parens_needed,
                                               valid_prefix,
                                               result=[]):
        if num_left_parens_needed > 0:
            directed_generate_balanced_parentheses(num_left_parens_needed-1,
                                                   num_right_parents_needed,
                                                   valid_prefix_'(')
        
        # we can only add right paren when we have MORE left paren. 
        # this automatically ensures the string is valid
        if num_left_parens_ndded < num_right_parens_needed:
            directed_generate_balanced_parentheses(num_left_parens_needed,
                                                   num_right_parens_ndded-1,
                                                   valid_prefix +')')
            

        if not num_right_parens_needed:
            result.append(valid_prefix)
        return result

    return directed_generate_balanced_parentheses(num_pairs, num_pairs, "")