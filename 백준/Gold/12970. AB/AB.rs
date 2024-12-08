use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let k: usize = next().parse().unwrap();

    // k=n-1이라면 a b * ( k)
    // max값은 (n//2) ^ 2
    let max_val = ((n + 1) / 2) * (n / 2);
    if max_val < k {
        print!("-1");
    } else if k <= n - 1 {
        print!("{}A{}", "B".repeat(n - k - 1), "B".repeat(k));
    } else {
        for i in 1..=((n + 1) / 2) {
            if k % i == 0 && i + k / i <= n {
                print!("{}{}{}", "B".repeat(n - i - k / i), "A".repeat(i), "B".repeat(k / i));
                return;
            }
            // AAA BBB 이런 형태인데, B 사이 중간에 A를 넣으면 가능
        }
        for i in 1..=((n + 1) / 2) {
            if i * (n - i) >= k {
                let b_cnt = k % (n - i);
                print!("{}", "A".repeat(i - 1));
                print!("{}A{}", "B".repeat((n - i) - b_cnt), "B".repeat(b_cnt));
                return;
            }
        }
        print!("-1");
    }
}
