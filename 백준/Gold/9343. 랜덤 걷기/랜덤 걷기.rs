use std::fmt::Write;
use std::io::{read_to_string, stdin};

const MOD: u128 = 1_000_000_007;

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

    let m = 2_000_000;
    let mut fac = vec![1; m + 1];
    for i in 1..=m {
        fac[i] = fac[i - 1] * i as u128 % MOD;
    }

    let t: u32 = next().parse().unwrap();

    let mut res = String::new();

    for _ in 0..t {
        let n: usize = next().parse().unwrap();
        let a = fac[2 * n];
        let b = pow_mod(fac[n], MOD - 2);
        let c = pow_mod(fac[n + 1], MOD - 2);

        writeln!(res, "{}", a * b * c % MOD).unwrap();
    }
    print!("{res}");
}
