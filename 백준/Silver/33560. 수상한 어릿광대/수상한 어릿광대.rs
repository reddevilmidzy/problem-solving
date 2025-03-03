use std::io::{read_to_string, stdin};

fn main() {
    let stdin = read_to_string(stdin()).unwrap();
    let mut token = stdin.split_whitespace();
    let mut next = || token.next().unwrap();

    let n: usize = next().parse().unwrap();
    let nums: Vec<u8> = (0..n).map(|_| next().parse().unwrap()).collect();
    let mut time = 0;
    let mut res = vec![0; 5];
    let mut score = 0;
    let mut add_score = 1;
    let mut add_time = 4;

    for i in 0..n {
        if time > 240 {
            res[prize(score)] += 1;
            score = 0;
            add_score = 1;
            add_time = 4;
            time = 0;
        }

        if nums[i] == 1 {
            res[prize(score)] += 1;
            score = 0;
            add_score = 1;
            add_time = 4;
            time = 0;
        } else if nums[i] == 2 {
            if add_score == 1 {
                add_time += 2;
            } else {
                add_score /= 2;
            }
        } else if nums[i] == 3 {

        } else if nums[i] == 4 {
            time += 56;
        } else if nums[i] == 5 {
            if add_time > 1 {
                add_time -= 1;
            }
        } else if nums[i] == 6 {
            if add_score < 32 {
                add_score *= 2;
            }
        }

        if nums[i] != 1 {
            score += add_score;
            time += add_time;
        }
    }

    if time > 240 {
        res[prize(score)] += 1;
    }

    for i in 1..=4 {
        println!("{}", res[i]);
    }

}

fn prize(score: u32) -> usize {
    if 35 <= score && score < 65 {
        return 1;
    }
    if 65 <= score && score < 95 {
        return 2;
    }
    if 95 <= score && score < 125 {
        return 3;
    }
    if 125 <= score {
        return 4;
    }
    0
}
