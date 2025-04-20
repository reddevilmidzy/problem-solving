// 러스트로 문자열은 에바다...ㅎ

use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let mut tmp = next().bytes();
    let n = tmp.len();
    let mut st = vec![0; n * 2 + 1];

    for i in 1..=n {
        st[i * 2 - 1] = tmp.next().unwrap();
    }
    let n = st.len();

    let mut a = vec![0i32; n];
    let mut r = 0;
    let mut p = 0;

    for i in 0..n {
        if r < i {
            a[i] = 0;
        } else {
            let ii = (2 * p) as i32 - i as i32;
            if ii < 0 {
                a[i] = (r - i) as i32;
            } else {
                a[i] = ((r - i) as i32).min(a[ii as usize]);
            }
        }

        let mut left = i as i32 - a[i] - 1;
        let mut right = i as i32 + a[i] + 1;

        while left >= 0 && (right as usize) < n && st[left as usize] == st[right as usize] {
            a[i] += 1;
            left = i as i32 - a[i] - 1;
            right = i as i32 + a[i] + 1;
        }
        if i + a[i] as usize > r {
            r = i + a[i] as usize;
            p = i;
        }
    }

    let mut res = 0;

    for i in 0..n {
        res = res.max(2 * a[i] + 1);
    }

    print!("{}", res / 2);
}
