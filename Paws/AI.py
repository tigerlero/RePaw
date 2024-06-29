# Imports
import copy, math
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import log_loss, accuracy_score, roc_auc_score

df = pd.read_csv('ai_data/pet_adoption_data.csv')
df = df.iloc[:, 1:]
header = list(df.iloc[:, :-1])

# Verifying if there are null values in the dataset
print(f'Number of null data:\n{df.isnull().sum()}')

# Data description & info
print(f'\n{df.describe()}')
print(f'\n{df.info()}')

# Getting the values of the non-numerical columns
stringData = {
    'PetType': {},
    'Breed': {},
    'Color': {},
    'Size': {}
}

keys = ['PetType', 'Breed', 'Color', 'Size']

for key in keys:
    for value in df[key]:
        if value in stringData[key]:
            stringData[key][value] += 1
        else:
            stringData[key][value] = 1

print(stringData)

# Replacing non-numerical with numerical values
petType_mapping = {'Bird': 0, 'Rabbit': 1, 'Dog': 2, 'Cat': 3}
breed_mapping = {'Parakeet': 0, 'Rabbit': 1, 'Golden Retriever': 2, 'Labrador': 3, 'Siamese': 4, 'Persian': 5,
                 'Poodle': 6}
color_mapping = {'Orange': 0, 'White': 1, 'Gray': 2, 'Brown': 3, 'Black': 4}
size_mapping = {'Small': 0, 'Medium': 1, 'Large': 2}

df['PetType'] = df['PetType'].map(petType_mapping)
df['Breed'] = df['Breed'].map(breed_mapping)
df['Color'] = df['Color'].map(color_mapping)
df['Size'] = df['Size'].map(size_mapping)

df.info()
print(df.describe())

# Splitting variables
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_set = X.to_numpy()
y_set = y.to_numpy()

print(f"X set shape: {X_set.shape}\ny set shape: {y_set.shape}")

fig, ax = plt.subplots(1, 5, figsize=(12, 3), sharey=True)
for i in range(len(ax)):
    ax[i].hist(X_set[:, i])
    ax[i].set_xlabel(header[i])
ax[0].set_ylabel("Count")
plt.show()

fig, ax = plt.subplots(1, 6, figsize=(12, 3), sharey=True)
for i in range(len(ax)):
    ax[i].hist(X_set[:, i + 5])
    ax[i].set_xlabel(header[i + 5])
ax[0].set_ylabel("Count")
plt.show()


def z_score_normalization(X):
    mean = np.mean(X)
    std = np.std(X)
    return (X - mean) / std


X_set_norm = z_score_normalization(X_set)

fig, ax = plt.subplots(1, 5, figsize=(12, 3), sharey=True)
for i in range(len(ax)):
    ax[i].hist(X_set_norm[:, i])
    ax[i].set_xlabel(header[i])
ax[0].set_ylabel("Count")
plt.show()

fig, ax = plt.subplots(1, 6, figsize=(12, 3), sharey=True)
for i in range(len(ax)):
    ax[i].hist(X_set_norm[:, i + 5])
    ax[i].set_xlabel(header[i + 5])
ax[0].set_ylabel("Count")
plt.show()


np.random.seed(0)
total_samples = X_set_norm.shape[0]
test_percentage = 0.2

#Number of test samples
n_test_samples = int(total_samples * test_percentage)

#Generate random indices
indices = np.arange(total_samples)
np.random.shuffle(indices)

#Split indices into training and testing sets
test_indices = indices[:n_test_samples]
train_indices = np.setdiff1d(indices, test_indices)

X_train, X_test = X_set_norm[train_indices], X_set_norm[test_indices]
y_train, y_test = y_set[train_indices], y_set[test_indices]

print(f"X_train shape: {X_train.shape}\tX_test shape: {X_test.shape}\ny_train shape: {y_train.shape}\t\ty_test shape: {y_test.shape}")


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def compute_cost(X, y, w, b):
    m = X.shape[0]
    cost = 0.

    for i in range(m):
        z_i = np.dot(X[i], w) + b
        f_wb_i = sigmoid(z_i)
        cost += (-y[i] * np.log(f_wb_i)) + ((1 - y[i]) * np.log(1 - f_wb_i))
    return cost / m


def compute_gradient(X, y, w, b):
    m, n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.

    for i in range(m):
        z_i = np.dot(w, X[i]) + b
        f_wb_i = sigmoid(z_i)
        err_i = f_wb_i - y[i]
        for j in range(n):
            dj_dw[j] += err_i * X[i, j]
        dj_db += err_i
    return (dj_dw / m), (dj_db / m)


def gradient_descent(X, y, w_in, b_in, alpha, num_iters):
    m = X.shape[0]
    J_hist = []
    w = copy.deepcopy(w_in)
    b = b_in

    for i in range(num_iters):
        dj_dw, dj_db = compute_gradient(X, y, w, b)

        # Updating parameters
        w -= alpha * dj_dw
        b -= alpha * dj_db

        cost = compute_cost(X, y, w, b)
        J_hist.append(cost)

        if i % math.ceil(num_iters / 10) == 0:
            print(f'Iteration {i:4d}: Cost {J_hist[-1]}')

    return w, b, J_hist


np.random.seed(0)

initial_w = np.random.rand(X_train.shape[1])
initial_b = np.random.randn()

num_iters = 10000
alpha = 0.03

final_w, final_b, J_history = gradient_descent(X_train, y_train, initial_w, initial_b, alpha, num_iters)
print(f"\nFor learning rate = {alpha} ---- b, w found by gradient descent: {final_b:0.2f}, {final_w}")


def predict(X, w, b, threshold=0.5):
    m = X.shape[0]
    predictions = np.zeros(m)

    for i in range(m):
        z_i = np.dot(w, X[i]) + b
        f_wb_i = sigmoid(z_i)
        predictions[i] = 1 if f_wb_i >= threshold else 0

    return predictions


def accuracy_score(y_true, y_pred):
    correct_predictions = np.sum(y_true == y_pred) # Calculate the number of correct predictions
    accuracy = correct_predictions / y_true.shape[0] # Calculate accuracy

    return accuracy


preds = predict(X_test, final_w, final_b)
loss_cost = compute_cost(X_test, y_test, final_w, final_b)
acc = accuracy_score(y_test, preds)

print(f'Cost: {loss_cost:.4f}')
print(f'Acc: {acc:.4f}')


plt.plot(J_history, '-')
plt.xlabel('Iterations step')
plt.ylabel('Cost')
plt.title('Cost vs. Iteration')
plt.show()


#Defining the model - Logistic Regression
log_reg = LogisticRegression().fit(X_train, y_train)

y_pred_log = log_reg.predict(X_test)

print(f'Logistic Regression Accuracy: {accuracy_score(y_test, y_pred_log):.4f}')
print(f'ROC AUC Score: {roc_auc_score(y_test, log_reg.predict_proba(X_test)[:, 1]):.4f}')
print(f'Log Loss: {log_loss(y_test, y_pred_log):.4f}')


#Defining the model - Random Forest Classifier
rf_clf = RandomForestClassifier().fit(X_train, y_train)

y_pred_rf = rf_clf.predict(X_test)

print(f'Random Forest Classifier Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}')
print(f'ROC AUC Score: {roc_auc_score(y_test, rf_clf.predict_proba(X_test)[:, 1]):.4f}')


#Defining the model - Ada Boost Classifier
adb = AdaBoostClassifier().fit(X_train, y_train)

y_pred_adb = adb.predict(X_test)

print(f'AdaBoost Classifier Accuracy: {accuracy_score(y_test, y_pred_adb):.4f}')
print(f'ROC AUC Score: {roc_auc_score(y_test, adb.predict_proba(X_test)[:, 1]):.4f}')