
# List Copy

scores = [10,9,7,4,5]
values = scores
print("scores[3] = ",scores[3])
print("values[3] = ",values[3])
scores[3] = 10
print("scores[3] = ",scores[3])
print("values[3] = ",values[3])

print()

scores2 = list(scores)
print("scores2[3] = ",scores2[3])
print("scores[3] = ",scores[3])
scores2[3] = -1
print("scores2[3] = ",scores2[3])