use std::fmt::Write;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let mut res = String::new();

    let t = next().parse().unwrap();
    for i in 1..=t {
        let n: usize = next().parse().unwrap();
        let m: usize = next().parse().unwrap();

        let nums: Vec<Vec<u32>> = (0..n)
            .map(|_| (0..m).map(|_| next().parse::<u32>().unwrap()).collect())
            .collect();

        writeln!(res, "Case #{i}: {}", solve(n, m, nums)).unwrap();
    }
    print!("{res}");
}

fn get_factor_cnt() -> Vec<u32> {
    let m = 10000;
    let mut res = vec![0; m + 1];

    let mut is_prime = vec![true; m + 1];

    for i in 2..=m {
        if is_prime[i] {
            for j in (i..=m).step_by(i) {
                let mut x = j;
                let mut cnt = 0;
                while x % i == 0 {
                    x /= i;
                    cnt += 1;
                }

                res[j] += cnt;
                is_prime[j] = false;
            }
        }
    }
    res
}


fn solve(n: usize, m: usize, nums: Vec<Vec<u32>>) -> String {
    let cnt = get_factor_cnt();

    let mut res = 0;

    for i in 0..n {
        // 이번 턴에서 할 수 있느 것
        let mut add = 0;

        for j in 0..m {
            add += cnt[nums[i][j] as usize];
        }

        res ^= add;
    }

    if res != 0 {
        "YES".to_string()
    } else {
        "NO".to_string()
    }
}


#[test]
fn tmp() {
    let val = solve(2, 3, vec![vec![4, 5, 6], vec![7, 8, 9]]);

    print!("{}", val);
}
