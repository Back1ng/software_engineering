def find_id_sequence(entries, search_id):
    if search_id not in entries:
        return ()

    first_index = entries.index(search_id)
    second_index = entries[first_index + 1:].index(search_id) + first_index + 1 if search_id in entries[first_index + 1:] else len(entries)

    return entries[first_index:second_index + 1] if second_index < len(entries) else entries[first_index:]

print(find_id_sequence((1, 2, 3), 8))
print(find_id_sequence((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_id_sequence((1, 2, 8, 5, 1, 2, 9), 8))
