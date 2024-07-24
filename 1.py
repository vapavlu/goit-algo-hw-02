import queue
import random
import time
import threading

# Створити чергу заявок
request_queue = queue.Queue()

# Функція generate_request()
def generate_request():
    while True:
        request_id = random.randint(1000, 9999)
        print(f"Нова заявка створена: {request_id}")
        request_queue.put(request_id)
        time.sleep(random.uniform(0.5, 2))  # Імітація часу між заявками

# Функція process_request()
def process_request():
    while True:
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"Обробляється заявка: {request_id}")
            time.sleep(random.uniform(1, 3))  # Імітація часу обробки заявки
            print(f"Заявка оброблена: {request_id}")
        else:
            print("Черг немає заявок для обробки.")
            time.sleep(1)  # Імітація чекання нових заявок

# Запуск потоків для генерації та обробки заявок
if __name__ == "__main__":
    generator_thread = threading.Thread(target=generate_request)
    processor_thread = threading.Thread(target=process_request)
    
    generator_thread.start()
    processor_thread.start()
    
    generator_thread.join()
    processor_thread.join()
