scaler = StandardScaler()
X_zscore = scaler.fit_transform(X) # Qui applichi la formula (x-media)/std

pca = PCA(n_components=1)
X_pca = pca.fit_transform(X_zscore) # Qui estrai la feature principale

mlp = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic')
mlp.fit(X_pca, y) # Qui la rete impara a prevedere 1 o 0
