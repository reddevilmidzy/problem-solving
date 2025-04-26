const MOD: u64 = 1_000_000_007;

fn pow_mod(base: u64, exp: u64) -> u64 {
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

fn find_catalan(n: u64) -> u64 {
    let mut res = 1;

    for i in 2..=n {
        let a = res * (4 * i - 2) % MOD;
        let b = pow_mod(i + 1, MOD - 2);
        res = a * b % MOD;
    }
    res
}

fn main() {
    let n: u64 = 1_000;

    print!("{}", find_catalan(n));
}
