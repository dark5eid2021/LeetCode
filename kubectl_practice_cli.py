import random

questions = [
    {
        "question": "Get all pods in all namespaces",
        "answer": "kubectl get pods -A"
    },
    {
        "question": "Show logs for pod named 'api-server' and container 'app'",
        "answer": "kubectl logs api-server -c app"
    },
    {
        "question": "Start a shell session in pod 'web-app'",
        "answer": "kubectl exec -it web-app -- /bin/sh"
    },
    {
        "question": "Port forward 'frontend-app' from pod port 80 to local 8080",
        "answer": "kubectl port-forward frontend-app 8080:80"
    },
    {
        "question": "Scale deployment 'payment-service' to 5 replicas",
        "answer": "kubectl scale deploy payment-service --replicas=5"
    },
    {
        "question": "Apply configuration from deployment.yaml",
        "answer": "kubectl apply -f deployment.yaml"
    },
    {
        "question": "Delete pod 'temp-debugger' in namespace 'dev'",
        "answer": "kubectl delete pod temp-debugger -n dev"
    },
    {
        "question": "Describe deployment 'api-gateway' in the default namespace",
        "answer": "kubectl describe deployment api-gateway -n default"
    },
    {
        "question": "Create a namespace called 'test-env'",
        "answer": "kubectl create ns test-env"
    },
    {
        "question": "Show CPU and memory usage of pods with wide output",
        "answer": "kubectl top pod -o wide"
    },
]

def start_cli():
    print("🧠 Kubernetes CLI Practice Tool")
    print("Type the correct kubectl command based on the question.\nType 'hint' to see the answer or 'exit' to quit.\n")

    random.shuffle(questions)
    score = 0

    for i, q in enumerate(questions):
        print(f"Q{i + 1}: {q['question']}")
        user_input = input("Your command: ").strip()

        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'hint':
            print(f"💡 Hint: {q['answer']}")
            continue
        elif user_input.strip() == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. Expected: {q['answer']}\n")

    print(f"🏁 Quiz Complete. Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    start_cli()
