use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    // 하루 이용권 10_000
    // 연속 3일권 25_000 쿠폰 하나
    // 연속 5일권 37_000 쿠폰 두개

    // dp[i][j] i번째 날짜에서 j개의 쿠폰을 가지고 있을 때의 최소 비용
    // 쿠폰은 그냥 넉넉 잡아 100 100으로 가보자.

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let k = 100;
    let nums: Vec<usize> = (0..m).map(|_| next().parse().unwrap()).collect();

    let inf = i32::MAX;
    let mut dp = vec![vec![inf; k + 3]; n + 1];
    dp[0][0] = 0;

    for i in 1..=n {
        for j in 0..k {
            // 휴일이라면
            if nums.contains(&i) {
                dp[i][j] = dp[i - 1][j].min(dp[i][j]);
            }
            // 그냥 하루치 구매
            if dp[i - 1][j] != inf {
                dp[i][j] = dp[i][j].min(dp[i - 1][j] + 10_000);
            }
            // 3일권
            if i >= 3 && dp[i - 3][j] != inf {
                // 쿠폰 추가
                dp[i][j + 1] = dp[i][j + 1].min(dp[i - 3][j] + 25_000);
            }
            if i >= 5 && dp[i - 5][j] != inf {
                // 쿠폰 추가
                dp[i][j + 2] = dp[i][j + 2].min(dp[i - 5][j] + 37_000);
            }

            // 쿠폰 사용
            if j >= 3 && dp[i - 1][j] != inf {
                dp[i][j - 3] = dp[i][j - 3].min(dp[i - 1][j]);
            }
        }
    }

    let mut res = inf;
    for j in 0..k {
        res = res.min(dp[n][j]);
    }

    print!("{res}");
}
