from collections import defaultdict


def best_sender(messages: list, senders: list) -> str:
    result = defaultdict(int)

    for i in range(len(senders)):
        result[senders[i]] += len(messages[i].split())

    return sorted(result.items(), key=lambda item: (item[1], item[0]))[-1][0]
