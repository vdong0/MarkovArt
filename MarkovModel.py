
class MarkovModel(object):

    """
    Creates a markov model given all the image rgb lists
    """
    def train_model(self, rgb_lists, order):
        markov_dict = {}

        for rgb_list in rgb_lists:
            start = 0
            for end in range(order, len(rgb_list) - 1):

                current_state = rgb_list[start:end]
                next_color = rgb_list[end] #rgb tuple

                state_string = self.rgb_list_to_string(current_state)

                if not state_string in markov_dict:
                    markov_dict[state_string] = []

                markov_dict[state_string].append(next_color)
                #if state_string in markov_dict:
                #    markov_dict[state_string].append(next_color)

                #else:
                #    markov_dict[state_string] = [next_color]

                start += 1

        return markov_dict



    """
    Converts rgb_list to a string, used for the Keys of our markov dictionary
    """
    def rgb_list_to_string(self, rgb_list):
        string_key = ""
        for rgb_tuple in rgb_list:
            r, g, b = rgb_tuple
            rgb_string = "{r}/{g}/{b},".format(r = r, g = g, b = b)

            string_key += rgb_string

        return string_key[:-1] #to get rid of ending comma

    """
    Converts rgb string to rgb_list
    """
    def rgb_string_to_list(self, rgb_string):

        rgb_list = []

        split_list = rgb_string.split(',')

        for color_string in split_list:
            split_color_string_list = color_string.split('/')

            r = split_color_string_list[0]
            g = split_color_string_list[1]
            b = split_color_string_list[2]

            rgb_list.append((r, g, b))

        return rgb_list
