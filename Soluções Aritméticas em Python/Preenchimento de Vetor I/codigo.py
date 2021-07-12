x = int(input())
vetor = [10]
vetor[0]=x
for i in range (1, 11):
  vetor.append(vetor[i-1]*2)
  print("N[%.d] = " %(i-1), vetor[i-1])