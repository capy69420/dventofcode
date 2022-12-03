    for k in range(3):
                    if list[i+k].count(item_type) == 0:
                        valid = False
                    break
                if valid:
                    priority = priority(item_type)
            