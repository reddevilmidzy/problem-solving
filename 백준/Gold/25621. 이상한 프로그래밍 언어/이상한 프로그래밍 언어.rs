use std::io::{read_to_string, stdin};

const MOD: u128 = 1_000_000_007;

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let mut k: u128 = next().parse().unwrap();

    for _ in 0..n {
        let u: String = next().parse().unwrap();
        let v: String = next().parse().unwrap();

        let uu = u.chars().next().unwrap();
        let vv = v.chars().next().unwrap();

        let new_k = if uu == '*' {
            k * u[1..].parse::<u128>().unwrap()
        } else {
            0.max(k as i128 + u.parse::<i128>().unwrap()) as u128
        };
        if vv == '*' {
            k *= v[1..].parse::<u128>().unwrap();
        } else {
            let t = (-(k as i128)).max(v.parse::<i128>().unwrap());
            k = (k as i128 + t) as u128;
        }
        k = 0.max(k).max(new_k) % (MOD * MOD);
    }

    print!("{}", k % MOD);
}
