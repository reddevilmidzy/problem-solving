use std::collections::HashSet;
use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();

    let nums: Vec<String> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut cnt: Vec<u64> = vec![0; 10];
    let mut cant_be_zero = HashSet::new();

    for num in nums {
        let st = num.as_bytes();
        cant_be_zero.insert(st[0] - 'A' as u8);
        for i in 0..st.len() {
            // println!("{}", st[i] - 'A' as u8);
            cnt[(st[i] - 'A' as u8) as usize] += 10_u64.pow((st.len() - i - 1) as u32);
        }
    }

    let mut tmp = Vec::with_capacity(10);

    for i in 0..10 {
        tmp.push((cnt[i], i as u8));
    }

    tmp.sort();
    let mut res: u64 = 0;
    for i in 0..10 {
        if !cant_be_zero.contains(&tmp[i].1) {
            tmp.remove(i);
            break;
        }
    }

    for i in 0..9 {
        res += cnt[tmp[i].1 as usize] * (i+1) as u64;
    }
    print!("{res}")
}
