#![allow(non_snake_case)]

use std::fs::read_to_string;

fn main() {
    let lines = read_lines("../../../inputs/03");
    part1(&lines);
    part2(&lines);
}

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}

fn find_common_element1(v1: Vec<char>, v2: Vec<char>) -> char {
    for c in v1 {
        if v2.contains(&c) {
            return c;
        }
    }

    ' '
}

fn find_common_element2(v1: Vec<char>, v2: Vec<char>, v3: Vec<char>) -> char {
    for c in v1 {
        if v2.contains(&c) && v3.contains(&c) {
            return c;
        }
    }

    ' '
}

fn get_priority(item: char) -> i32 {
    if item.is_uppercase() {
        return item as i32 - 38;
    } else {
        return item as i32 - 96;
    }
}

fn part1(lines: &Vec<String>) {
    let mut priority_sum = 0;

    for rucksack in lines {
        let (comp1, comp2) = rucksack.split_at(rucksack.len() / 2);
        let v1: Vec<char> = comp1.chars().collect();
        let v2: Vec<char> = comp2.chars().collect();
        let item_type = find_common_element1(v1, v2);

        priority_sum += get_priority(item_type);
    }

    println!("{}", priority_sum)
}

fn part2(lines: &Vec<String>) {
    let mut priority_sum = 0;

    for i in (0..lines.len()).step_by(3) {
        let v1: Vec<char> = lines[i].chars().collect();
        let v2: Vec<char> = lines[i + 1].chars().collect();
        let v3: Vec<char> = lines[i + 2].chars().collect();
        let group_item = find_common_element2(v1, v2, v3);

        priority_sum += get_priority(group_item);
    }

    println!("{}", priority_sum)
}
