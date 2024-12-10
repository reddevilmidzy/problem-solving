use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut tokens = stdin.split_whitespace();
    let mut next = || tokens.next().unwrap();

    let mut nums: Vec<i32> = (0..6).map(|_| next().parse().unwrap()).collect();

    let mut res = 0;

    // 6개 짜리 함
    // 6개는 어디 끼워줄 수 없음
    res += nums[5];

    // 5개 짜리 함
    res += nums[4];
    // 5개에는 1만 끼워넣을 수 있음
    nums[0] = 0.max(nums[0] - (11 * nums[4]));

    // 4개짜리 함
    res += nums[3];
    // 4개에선 1이랑 2를 넣을 수 있음

    // 2로 없애고 남은 흔적
    let tmp = 0.max(5 * nums[3] - nums[1]);
    nums[0] = 0.max(nums[0] - tmp * 4);
    nums[1] = 0.max(nums[1] - (5 * nums[3]));

    // 3개짜리 함
    res += (nums[2] + 3) / 4;

    if nums[2] % 4 == 1 {
        nums[0] = 0.max(nums[0] - 7);
        nums[1] -= 5;
        if nums[1] < 0 {
            nums[0] = 0.max(nums[0] + 4 * nums[1]);
            nums[1] = 0;
        }
    } else if nums[2] % 4 == 2 {
        nums[0] = 0.max(nums[0] - 6);
        nums[1] -= 3;
        if nums[1] < 0 {
            nums[0] = 0.max(nums[0] + 4 * nums[1]);
            nums[1] = 0;
        }
    } else if nums[2] % 4 == 3 {
        nums[0] = 0.max(nums[0] - 5);
        nums[1] -= 1;
        if nums[1] < 0 {
            nums[0] = 0.max(nums[0] + 4 * nums[1]);
            nums[1] = 0;
        }
    }
    //2개짜리 함
    res += (nums[1] + 8) / 9;
    if nums[1] % 9 != 0 {
        nums[0] = 0.max(nums[0] - 4 * (9 - nums[1] % 9));
    }

    res += (nums[0] + 35) / 36;
    print!("{res}")
}
