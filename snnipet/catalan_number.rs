fn main() {
    let n: usize = 1_000;
    const MOD: u64 = 1_000_000_007;
    let mut dp = vec![0u64; n + 1];
    dp[0] = 1;
    dp[1] = 1;

    for i in 1..=n {
        let mut tmp = 0u64;
        for j in 0..i {
            tmp = ((tmp % MOD) + (dp[j] * dp[i - j]) % MOD) % MOD;
        }
        dp[i] = tmp;
    }
}
