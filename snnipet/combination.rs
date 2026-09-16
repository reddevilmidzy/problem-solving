fn comb(n: i32, r: i32) -> i32 {
    let r = r.min(n - r);
    let mut res = 1;

    for i in 1..=r {
        res *= (n - r + i);
        res /= i;
    }

    res
}
