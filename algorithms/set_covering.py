"""
Chapter 8 Grokking - Greedy Set Cover Alg

Cont. pick station that adds most number new states, until all are covered
"""

def greedy_set_cover(states_needed, stations):
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()

        # find best station
        for station, states in stations.items():
            covered = states_needed & states

            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations




if __name__ == "__main__":
    # Set of states we need to cover
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

    # Dictionary of stations and the states they cover
    stations = {
        "kone": set(["id", "nv", "ut"]),
        "ktwo": set(["wa", "id", "mt"]),
        "kthree": set(["or", "nv", "ca"]),
        "kfour": set(["nv", "ut"]),
        "kfive": set(["ca", "az"]),
    }

    # Final set of stations we’ll choose
    result = greedy_set_cover(states_needed, stations)
    print("Final stations:", result)


