import matplotlib.pyplot as plt  # Imports nach oben


def assignment(new_list, i, old_list, j):  # Funktion falsch benannt
    """Setzt den Wert von new_list am Index i auf den Wert von old_list am Index j."""  # Docstring hinzugefügt
    new_list[i] = old_list[j]


def merge_sort(list_to_sort_by_merge):  # Funktion falsch benannt
    """Sortiert die übergebene Liste aufsteigend"""  # Docstring hinzugefügt
    if len(list_to_sort_by_merge) > 1:  # unnötige Bedingungen
        mid = len(list_to_sort_by_merge) // 2
        left = list_to_sort_by_merge[:mid]
        right = list_to_sort_by_merge[mid:]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                assignment(list_to_sort_by_merge, i, left, l)  # Parameter wie i=i entfernen
                l += 1
            else:
                assignment(list_to_sort_by_merge, i, right, r)  # Parameter wie i=i entfernen
                r += 1
            i += 1

        while l < len(left):
            list_to_sort_by_merge[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            list_to_sort_by_merge[i] = right[r]
            r += 1
            i += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))

fig, (ax1, ax2) = plt.subplots(ncols=2, tight_layout=True)

ax1.set_title('List before sorting')
ax1.set_xlabel('Index')
ax1.set_ylabel('Value')
ax1.bar(x, my_list)

merge_sort(my_list)
ax2.set_title('List after sorting')
ax2.set_xlabel('Index')
ax2.set_ylabel('Value')
ax2.bar(x, my_list)

plt.show()
