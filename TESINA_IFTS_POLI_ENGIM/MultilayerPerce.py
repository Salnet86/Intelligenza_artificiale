from sklearn.neural_network import MLPClassifier

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0] 

mlp = MLPClassifier(hidden_layer_sizes=(4,), activation='relu', max_iter=2000)
mlp.fit(X, y)

print("Test della rete neurale MLP su XOR:")
for i in X:
    predizione = mlp.predict([i])
    print(f"Input: {i} -> Output: {predizione[0]}")
  
