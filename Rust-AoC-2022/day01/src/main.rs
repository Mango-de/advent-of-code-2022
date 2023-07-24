#![allow(non_snake_case)]

use std::fs::read_to_string;

fn main() {
    // fn parse_to_i32(s: &str) -> i32 {
    //     s.parse().unwrap()
    // }
    let lines = read_lines("../../../inputs/01");
    let sums = make_sum_blocks(&lines);
    part1(&sums);
    part2(sums);
}

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}

fn make_sum_blocks(lines: &Vec<String>) -> Vec<i32> {
    let mut blocks: Vec<Vec<i32>> = Vec::new();
    let mut current_block: Vec<i32> = Vec::new();

    for line in lines {
        if line.is_empty() {
            if !current_block.is_empty() {
                blocks.push(current_block);
                current_block = Vec::new();
            }
        } else {
            let num: i32 = line.parse().expect("Invalid number");
            current_block.push(num);
        }
    }

    if !current_block.is_empty() {
        blocks.push(current_block);
    }

    blocks.iter().map(|block| block.iter().sum()).collect()
}

fn part1(sums: &Vec<i32>) {
    println!("{}", sums.iter().max().unwrap());
}

fn part2(mut sums: Vec<i32>) {
    sums.sort_by(|a, b| b.cmp(a));
    println!("{:?}", sums[..3].iter().sum::<i32>());
}
