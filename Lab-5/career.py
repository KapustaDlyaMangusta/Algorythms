def max_experience(levels, experience):
    dp = [0] * (levels + 1)

    for i in range(levels - 1, -1, -1):
        print("-------------------")
        print(dp)

        for j in range(i + 1):
            experience[i][j] += max(dp[j], dp[j + 1])
        dp = experience[i][:i + 2]

        print(experience[i])
        print(f"upd: {dp}")
        print("-------------------")

    return experience[0][0]


with open('career.in', 'r') as file:
    levels = int(file.readline())
    experience = [list(map(int, file.readline().split())) for _ in range(levels)]

result = max_experience(levels, experience)

with open('career.out', 'w') as file:
    file.write(str(result))
