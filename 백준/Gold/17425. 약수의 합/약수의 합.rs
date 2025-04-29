use std::fmt::Write;
use std::io::{read_to_string, stdin};

const N: usize = 1_000_000;

fn solve() -> Vec<u64> {
    let mut facs = vec![0u64; N + 1];
    facs[1] = 1;
    for i in 2..=N {
        for j in 1..=N {
            if i * j > N {
                break;
            }
            facs[i * j] += j as u64;
        }
    }

    for i in 2..=N {
        facs[i] += facs[i - 1] + i as u64;
    }

    facs
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let arr = solve();

    let t: usize = next().parse().unwrap();
    let mut stdout = String::with_capacity(t);
    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        writeln!(stdout, "{}", arr[n]).unwrap();
    }

    print!("{stdout}");
}
