n = int(input())
num_votes = dict()
for num in range(n):
    cand, votes = input().split()
    num_votes[cand] = num_votes.get(cand, 0) + int(votes)
for cand, votes in sorted(num_votes.items()):
    print(cand, votes)
