from sklearn.metrics import accuracy_score, confusion_matrix
import model

y_pred = model.model.predict(model.X_test)
acc = accuracy_score(model.y_test, y_pred)
cm = confusion_matrix(model.y_test, y_pred)

print("Model Training Completed!")
print("Accuracy Score:", acc)
print("Confusion Matrix:")
print(cm)
