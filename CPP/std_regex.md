---
aliases: []
author: Maneesh Sutar
date: 2024-05-28
tags:
- cpp
title: C++ std::regex
---

# C++ std::regex

The updated is present [here](https://github.com/maneesh29s/just-cpp-things/blob/main/src/regex.cc)

````cpp
#include <cmath>
#include <iostream>
#include <regex>
#include <string>

using std::cout;
using std::endl;

int main() {
    std::string original{
        "The sun dipped below the horizon, casting long shadows across the deserted beach. "};

    cout << original << endl << endl;
    // String Replacement: Replace all occurrences of the word "beach" with "coast".

    std::regex string_replace_regex("beach");
    std::string replaced = std::regex_replace(original, string_replace_regex, "coast");

    cout << "beach to coast: " << replaced << endl;

    cout << endl;


    // Advanced replace with capturing groups
    // Replace the words starting with s, by duplicating them
    std::regex ad_string_replace_regex("\\b(?=s)([\\w]+)\\b");

    // Use '$' to specify capturing groups. 
    // $0 = entire substring matching the regex patten 
    // $1 and so on = individual capture groups
    std::string ad_replaced = std::regex_replace(original, ad_string_replace_regex, "$1$1");

    cout << "double words starting with s: " << ad_replaced << endl;

    cout << endl;

    // String Search: Find all instances of words that start with the letter "s".

    /*
    std::regex_match will only return true if the regular expression matches the entire
    string sequence
    std::regex_search will successfully match any subsequence of the given sequence, ONLY ONCE

    To search "globally" we have to use std::sregex_iterator
    std::sregex_iterator will iterator over the string, every time it will call regex_search,
    and save the result in an object of std::smatch
    *operator on std::sregex_iterator will return the object of std::smatch
    str(n) or operator[n] on std::smatch object will return
        n = 0: entire matched string
        n > 0: capturing groups
    */

    std::regex string_search_regex("\\bs(\\w*)\\b");  // capturing group is added just for fun

    std::sregex_iterator iter(original.begin(), original.end(), string_search_regex);
    std::sregex_iterator end;

    cout << "Instances of words that start with s: " << endl;
    while (iter != end) {
        std::smatch match = *iter;

        // number of std::sub_match in the current std::smatch
        // std::cout << match.size() << " ";

        std::cout << match[0] << " ";  // whole matched string
        // std::cout << match[1] << " ";  // 1st captured group
        ++iter;
    }
    cout << endl << endl;

````
