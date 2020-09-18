from MarkovModel import MarkovModel
import random

class MarkovProcess(object):

    """
    Given a Markov Model (dict), creates a complete RGB list
    """
    def create_rgb_list(self, model, length, order):

        mm = MarkovModel() ## Using this just for the rgb_string_to_list func
                            ## As well as rgb_list_to_string

        current_state = random.choice(list(model.keys()))

        rgb_list = mm.rgb_string_to_list(current_state)

        index = 1
        for n in range(order, length):

            next_color = random.choice(model[current_state])
            rgb_list.append(next_color)
            current_state = mm.rgb_list_to_string(rgb_list[index:])

            index += 1

        return rgb_list
