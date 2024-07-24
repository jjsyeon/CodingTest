def solution(data, ext, val_ext, sort_by):
    cols = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    filtered_data = [row for row in data if row[cols[ext]] < val_ext]
    answer = sorted(filtered_data, key = lambda x: x[cols[sort_by]])
    return answer