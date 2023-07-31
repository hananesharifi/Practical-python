def min_days_to_repay(n, m, opportunities):
    def min_days_to_repay(n, m, opportunities):
        opportunities.sort(key=lambda x: x[0] / x[1], reverse=True)
        days = 0

        m = 0

        for p_i, c_i in opportunities:
            if remaining_m >= c_i:
                num_opportunities = min(remaining_m // c_i, 1)  # انتخاب حداکثر یک بار سرمایه‌گذاری
                remaining_m -= num_opportunities * c_i
                days += num_opportunities

        return days


if __name__ == "__main__":
    n, m = map(int, input().split())
    opportunities = [tuple(map(int, input().split())) for _ in range(n)]
    result = min_days_to_repay(n, m, opportunities)
    print(result)
