#!/usr/bin/env python
# -*- coding: utf-8-*-

import random


def search2(data_min, data_max, n, num, tmp_data):
    """
    :param data_min: 下限值
    :param data_max:  上限值
    :param n: 目标值
    :param num: 已查询次数
    :return:
    """
    assert data_max >= n >= data_min
    num += 1  # 查询计数+1

    # mid取中值下限 [2,3) 取 2
    data_mid = (data_max + data_min) / 2

    # 如果最后一次取的该值，则本次取 +1，[2,3) 取 3
    if (data_max - data_min == 1) and data_mid == tmp_data[-1]:
        data_mid += 1

    tmp_data.append(data_mid)
    if data_mid == n:
        # print u'查询{num}次成功，n为{n}, tmp_data: {d}'.format(num=num, n=n, d=tmp_data)
        return num
    elif data_mid > n:
        num += search2(data_min, data_mid, n, num, tmp_data)
    else:
        num += search2(data_mid, data_max, n, num, tmp_data)
    return num


def avg(arr):
    # 求平均数
    avg_d = 1.0 * sum(arr) / len(arr)
    return avg_d


def main():
    # 一次测试
    n = random.choice(xrange(1, 101))
    num = search2(1, 100, n, num=0, tmp_data=[])
    return num


def test(n):
    """
    :param n: 测试次数， 需要为正整数
    :return:
    """
    times = int(n)
    d = [main() for _ in range(times)]
    print u'{n}次执行平均次数{avg_t}'.format(n=n, avg_t=avg(d))

test(10000)
