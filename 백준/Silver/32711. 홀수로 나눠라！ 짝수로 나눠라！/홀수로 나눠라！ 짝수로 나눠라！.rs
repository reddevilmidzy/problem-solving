use std::io::{read_to_string, stdin};
fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<i32> = (0..n).map(|_| next().parse().unwrap()).collect();

    let mut odd = 0;
    let mut even = 0;

    for num in &nums {
        if *num % 2 == 0 {
            even += 1;
        } else {
            odd += 1;
        }
    }

    // 그냥 다 하나로 묶어서 홀수로 나눔
    if odd % 2 != 0 {
        print!("1");
        return;
    } else if n > 1 && odd == 0 { // 홀수 하나도 없고 둘로 나눔
        print!("1");
        return;
    } else if n == 1 { // odd=0, even=1
        print!("0");
        return;
    }
    // 이제 odd에 따라서 홀수로 나눠야할지 짝수로 나눠야 할지가 나눠짐
    // 아니 무조건 짝수로 나눠야함. 일단 odd갯수가 짝수기 홀수로 나눌수 없음
    if odd == 2 && nums[0] % 2 != 0 && nums[n - 1] % 2 != 0 {
        print!("0");
        return;
    }
    print!("1");
}
