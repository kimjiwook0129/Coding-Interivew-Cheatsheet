## Dynamic Programming [동적 프로그래밍]

Dynamic Programming (DP) is an algorithmic technique breaking a problem down into simpler subproblems. We save the solutions for the subproblems and use them to solve the bigger problem. In DP, We can rewrite any recurrence formula, the relation between each terms. [동적 프로그래밍은 큰 문제를 작은 문제들로 나누어 문제를 풀어나가는 방식입니다. 작은 문제들로부터 나온 해답을 저장하고 큰 문제를 푸는데 사용합니다. 동적 프로그래밍에서는 각 항들 사이의 관계식을 의미하는 점화식을 그대로 코드로 옮겨서 구현할 수 있습니다.]

- Memoization (Top-Down) Method [메모아제이션 (탑다운) 방식]

  - We call recursions to call subproblems to solve big problems

    ```c++
    int dp[MAXN]
    int solve(int x) {
        if (x==0) return 1;
        if (dp[x]!=-1) return dp[x];
        return (dp[x] = x * solve(x-1));
    }
    ```

- Tabulation (Bottom-Up) Method [테뷸레이션 (바텀업) 방식]

  - We use iterations to solve smaller problems first, then use the results to solve bigger problem

    ```c++
    int dp[MAXN];
    int dp[0] = 1;
    for (int i = 1; i< =n; i++) {
        dp[i] = dp[i-1] * i;
    }
    ```

[Source](https://www.geeksforgeeks.org/tabulation-vs-memoization/)
