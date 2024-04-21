from collections import deque


N, M = map(int, input().split())
num_truth, *truths = map(int, input().split())
truths = set(truths)
parties = deque()

for _ in range(M):
    num, *members = map(int, input().split())
    parties.append([num, members])

stats = True

while stats:
    stats = False
    for _ in range(len(parties)):
        num, members = parties.popleft()
        for member in members:
            if member in truths:
                truths.update(members)
                stats = True
                break
        else:
            parties.append([num, members])

print(len(parties))