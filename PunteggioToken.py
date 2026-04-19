
Q = X @ W_Q
K = X @ W_K
V = X @ W_V
scores = (Q @ K.T) / math.sqrt(64)
weights = torch.softmax(scores, dim=-1)
output = weights @ V
