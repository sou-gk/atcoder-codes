N = int(input());
A = list(map(int, input().split()));
B = list(map(int, input().split()));

answer1 = 0;
answer2 = 0;

B_dict = dict();
for i, b_i in enumerate(B):
  B_dict[b_i] = i;

for i in range(N):
  if A[i] == B[i]:
    answer1 += 1;

for i in range(N):
  if A[i] in B_dict:
    if B_dict[A[i]] != i:
      answer2 += 1;

print(answer1, answer2, sep="\n");
