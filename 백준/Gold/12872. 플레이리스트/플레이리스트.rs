use std::io::{read_to_string, stdin};

const MOD: i64 = 1_000_000_007;

fn solve(n: usize, m: usize, p: usize, song_len: usize, song_cnt: usize, dp: &mut Vec<Vec<i32>>) -> i32 {
    let left = n - song_cnt;
    if song_len == p { // 플리 길이가 p
        if left == 0 { // 선택하지 않은 곡이 없음
            return 1;
        }
        return 0;
    }
    if dp[song_len][song_cnt] != -1 {
        return dp[song_len][song_cnt];
    }

    let mut tmp: i64 = 0;
    if left > 0 {
        tmp += solve(n, m, p, song_len + 1, song_cnt + 1, dp) as i64 * left as i64;
    }
    if song_cnt > m {
        tmp += solve(n, m, p, song_len + 1, song_cnt, dp) as i64 * (song_cnt - m) as i64;
    }

    dp[song_len][song_cnt] = (tmp % MOD) as i32;
    dp[song_len][song_cnt]
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let m: usize = next().parse().unwrap();
    let p: usize = next().parse().unwrap();

    let mut dp: Vec<Vec<i32>> = vec![vec![-1; n + 1]; p + 1];
    let res = solve(n, m, p, 0, 0, &mut dp);
    print!("{res}")
}
