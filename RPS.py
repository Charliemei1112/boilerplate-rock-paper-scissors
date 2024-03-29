# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
# We can adapt abbey's method but with longer memory. We can keep track of the last 5 moves and play the move that would have beaten the most common move in that history.

# play_order = 4
def player(prev_play, opponent_history = [], play_order={}):
    # define counter moves
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}

    # if no previous play, set it to 'R'
    if not prev_play:
        prev_play = 'R'
    
    # add the last move to the opponent history
    opponent_history.append(prev_play)

    # Set default prediction to 'P'
    prediction = 'P'

    if len(opponent_history) > 3:
        # Join last 4 plays with potential next play of 'R', 'P', 'S'
        last_four = "".join(opponent_history[-4:])
        play_order[last_four] = play_order.get(last_four, 0) + 1

        # Join last 3 plays with potential next play of 'R', 'P', 'S'
        potential_plays = [ "".join([*opponent_history[-3:], v]) for v in ['R', 'P', 'S']]

        # Add potential plays to play_order if not already in it
        potential_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # Get the most common play from potential_order
        if potential_order:
            prediction = max(potential_order, key=potential_order.get)[-1:]

    return counter_moves[prediction]