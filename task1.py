# String-Based Examination Answer Evaluation
def normalize(text):
    return ''.join(ch.upper() for ch in text if ch.isalnum() or ch in '-_')
 
def evaluate_student(name, answer_key, response, correct_mark=4, negative_mark=1):
    correct = incorrect = unanswered = 0
    response = normalize(response)
    for index, expected in enumerate(answer_key):
        answer = response[index] if index < len(response) else '-'
        if answer in '-_':
            unanswered += 1
        elif answer == expected:
            correct += 1
        else:
            incorrect += 1
    score = correct * correct_mark - incorrect * negative_mark
    return {"name": name, "correct": correct, "incorrect": incorrect,
            "unanswered": unanswered, "score": score}
 
answer_key = normalize(input("Enter answer key: "))
correct_mark = float(input("Marks for each correct answer: "))
negative_mark = float(input("Negative marks for each wrong answer: "))
student_count = int(input("Number of students: "))
 
results = []
for _ in range(student_count):
    name = input("Student name: ")
    response = input("Response string (- for unanswered): ")
    results.append(evaluate_student(name, answer_key, response, correct_mark, negative_mark))
 
results.sort(key=lambda result: (-result["score"], result["name"]))
print("\nRank  Name       Correct  Incorrect  Unanswered  Score")
for rank, result in enumerate(results, start=1):
    print(f"{rank:<5} {result['name']:<10} {result['correct']:<8} "
          f"{result['incorrect']:<10} {result['unanswered']:<11} {result['score']:g}")
 