use std::io::{read_to_string, stdin};

fn fac(n: i64) -> i64 {
    let mut res = 1;
    for i in 1..=n {
        res *= i;
    }
    res
}

fn pass_or_tle(tot: i64, limit: i64, res: &mut String) {
    if tot <= limit {
        res.push_str("May Pass.");
    } else {
        res.push_str("TLE!");
    }
    res.push('\n');
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let c: usize = next().parse().unwrap();
    let mut res: String = String::with_capacity(c);
    let one: i64 = 100_000_000;
    for _ in 0..c {
        // 시복, 최대 범위, 테케 수, 제한시간
        let s: String = next().parse().unwrap();
        let n: i64 = next().parse().unwrap();
        let t: i64 = next().parse().unwrap();
        let l: i64 = next().parse().unwrap();

        if s == "O(N)" {
            pass_or_tle(n * t, one * l, &mut res);
        } else if s == "O(N^2)" {
            pass_or_tle(n * n * t, one * l, &mut res);
        } else if s == "O(N^3)" {
            if n >= 1001 {
                res.push_str("TLE!\n");
                continue;
            }
            pass_or_tle(n * n * n * t, one * l, &mut res);
        } else if s == "O(2^N)" {
            if n >= 30 {
                res.push_str("TLE!\n");
                continue;
            }
            pass_or_tle(2i64.pow(n as u32) * t, one * l, &mut res);
        } else {
            if n >= 13 {
                res.push_str("TLE!\n");
                continue;
            }
            pass_or_tle(fac(n) * t, one * l, &mut res);
        }
    }
    print!("{}", res);
}
