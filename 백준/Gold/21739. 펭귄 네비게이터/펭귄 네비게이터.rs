use std::io::{read_to_string, stdin};

const MOD: u128 = 1_000_000_007;
fn factorial(x: u128) -> u128 {
    let mut res = 1;
    for i in 2..=x {
        res = (res * i) % MOD;
    }
    res
}

fn pow_mod(base: u128, exp: u128) -> u128 {
    if exp == 0 {
        return 1;
    }
    let mut res = pow_mod(base, exp / 2);
    res = (res * res) % MOD;
    if exp & 1 != 0 {
        res = res * base % MOD;
    }
    res
}

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: u128 = next().parse().unwrap();
    let a = factorial(2 * n);
    let b = pow_mod(factorial(n), MOD - 2);
    let c = pow_mod(factorial(n + 1), MOD - 2);

    print!("{}", a * b * c % MOD);
}
