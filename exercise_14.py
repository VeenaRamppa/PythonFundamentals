questions_file = open("questions.txt","r")
questions = [line.strip() for line in questions_file.readlines()]
questions_file.close()
correct = 0

for line in questions:
   # question = line.split("=")[0]
   # actual_ans = line.split("=")[1]
   q,a = line.split("=")
   user_ans = input(f"{q}=?")
   if user_ans == a:
       correct += 1

result_file = open("results.txt","w")
result_file.write(f"Your final score is {correct}/{len(questions)}\n")
result_file.close()