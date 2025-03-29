#!/usr/bin/python3

import argparse
import math
import random
from datetime import datetime, timedelta


def generate_tomato_clock_schedule(start_time, end_time, work_duration, break_duration):
    # 必须包含的活动
    mandatory_activities = ["数学", "英语", "身体锻炼"]

    # 所有可能的活动
    all_activities = [
        "数学",
        "英语",
        "读技术书",
        "读杂书",
        "读新闻报纸",
        "读英文新闻报纸",
        "写字",
        "写文章",
        "写日记",
        "写回忆录",
        "修习新技术",
        "开发项目",
        "冥想",
        "归理知识库",
        "整理备忘录",
        "身体锻炼",
        "代码练习",
        "复习",
    ]

    # 初始化活动列表
    activities = []
    for activity in mandatory_activities:
        activities.append(activity)

    # 添加其他活动直到达到所需数量
    cycle = timedelta(minutes=work_duration + break_duration)
    count_of_cycles = math.floor((end_time - start_time) / cycle)
    while len(activities) < count_of_cycles:  # 假设一天安排8个番茄钟周期
        remaining_activities = list(set(all_activities) - set(activities))
        if not remaining_activities:
            break
        next_activity = remaining_activities.pop()
        activities.append(next_activity)

    # 打乱活动顺序
    random.shuffle(activities)

    # 计算每个时间段的时间
    schedule = []
    current_time = start_time
    for i, activity in enumerate(activities):
        end_work_time = current_time + timedelta(minutes=work_duration)
        schedule.append(
            (
                current_time.strftime("%H:%M"),
                end_work_time.strftime("%H:%M"),
                activity,
            )
        )
        current_time = end_work_time + timedelta(minutes=break_duration)

    return schedule


def main():
    parser = argparse.ArgumentParser(description="Generate a tomato clock schedule.")
    parser.add_argument(
        "-s",
        "--start-time",
        type=str,
        default="18:00",
        help="Start time in HH:MM format (default: 18:00)",
    )
    parser.add_argument(
        "-e", "--end-time", type=str, default="22:00", help="End time (HH:MM)"
    )
    parser.add_argument(
        "-w",
        "--work-duration",
        type=int,
        default=25,
        help="Work duration in minutes (default: 25)",
    )
    parser.add_argument(
        "-b",
        "--break-duration",
        type=int,
        default=5,
        help="Break duration in minutes (default: 5)",
    )

    args = parser.parse_args()

    try:
        start_time = datetime.strptime(args.start_time, "%H:%M")
        end_time = datetime.strptime(args.end_time, "%H:%M")
    except ValueError:
        print("Invalid time format. Please use HH:MM.")
        return

    schedule = generate_tomato_clock_schedule(
        start_time, end_time, args.work_duration, args.break_duration
    )

    print(f"Today's daily schedule starting at {args.start_time}:")
    for entry in schedule:
        print(f"{entry[0]} - {entry[1]}: {entry[2]}")


if __name__ == "__main__":
    main()
