import requests
import matplotlib.pyplot as plt
url = "https://jsonplaceholder.typicode.com/users"
data = requests.get(url).json()
students = []
scores = []
for i, user in enumerate(data):
    students.append(user['name'])
    scores.append((i + 1) * 10)
avg = sum(scores) / len(scores)
print("Average Score:", avg)
plt.bar(students, scores)
plt.xticks(rotation=45)
plt.title("Student Scores")
plt.tight_layout()
plt.show()
