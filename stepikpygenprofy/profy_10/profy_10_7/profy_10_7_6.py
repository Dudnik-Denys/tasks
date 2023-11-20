def parse_ranges(ranges: str):
    ranges = ranges.split(',')
    for custom_range in ranges:
        yield from range(int(custom_range[:custom_range.find('-')]), int(custom_range[custom_range.find('-') + 1:]) + 1)
