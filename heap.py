import heapq

# Start with an empty min-heap
priority = []

# Add values one by one
for value in [5, 2, 7, 1]:
    heapq.heappush(priority, value)

# Remove the smallest value
print(heapq.heappop(priority))

# Remove the next smallest value
print(heapq.heappop(priority))

# Display the remaining values in sorted order
print(sorted(priority))
import heapq

# Create an empty priority queue
priority_queue = []

# Add tasks as (priority, task_name)
tasks = [
    (2, "Write report"),
    (1, "Answer email"),
    (2, "Attend meeting"),
    (1, "Check database"),
    (3, "Backup files")
]

for priority, task_name in tasks:
    heapq.heappush(priority_queue, (priority, task_name))

# Process tasks in priority order
while priority_queue:
    priority, task_name = heapq.heappop(priority_queue)
    print("Priority:", priority, "| Task:", task_name)
