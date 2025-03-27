use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let mut s: String = next().parse().unwrap();
    let k: usize = next().parse().unwrap();
    let n: usize = s.len();

    unsafe {
        if k == n {
            print!("0");
        } else if n / 2 >= k {
            let bytes = s.as_bytes();
            let mut res = 0;
            for i in 0..k {
                if bytes[i] != bytes[n - 1 - (k - i - 1)] {
                    res += 1;
                }
            }
            print!("{res}");
        } else {
            let bytes = s.as_bytes_mut();
            let mut res = 0;

            let mut used = vec![false; n];
            let n = n as i32;
            let k = k as i32;

            for i in 0..n {
                if used[i as usize] {
                    continue;
                }

                let mut cnt = vec![0; 26];
                let mut j = i;
                let mut tmp = 0;
                while j < n {
                    used[j as usize] = true;
                    cnt[bytes[j as usize] as usize - 97] += 1;
                    j = n - 1 - (k - j - 1);
                    tmp += 1;
                }
                let max_v = *cnt.iter().max().unwrap();
                res += tmp - max_v;
            }
            print!("{res}");
        }
    }
}
