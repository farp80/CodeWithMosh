def balancedString(query_string):
    possible_combinations = {
        "(": "()",
        "[": "[]",
        "{": "{}"
    }

    tracker = []

    for i in query_string:
        current_value = possible_combinations.get(i, "")

        if "".__eq__(current_value) and len(tracker) != 0:
            last_item = tracker.pop()
            comparison = last_item + "" + i

            if comparison == possible_combinations[last_item]:
                continue
        else:
            tracker.append(i)

    print(tracker)
    if len(tracker) != 0:
        return "No balanced"
    else:
        return "Balanced"


query_string = "]["
result = print(balancedString(query_string))
