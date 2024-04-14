import asyncio

test_type = 10

sensors = ['sensor_37', 'sensor_03', 'sensor_28', 'sensor_31', 'sensor_50', 'sensor_01', 'sensor_14', 'sensor_30',
           'sensor_32', 'sensor_18', 'sensor_11', 'sensor_49', 'sensor_34', 'sensor_42', 'sensor_21', 'sensor_05',
           'sensor_16', 'sensor_24', 'sensor_39', 'sensor_44']

all_data_dict = {
    'sensor_37': {
        'data': ['5cf6c0', '4f75f6', 'aa19cb', '12bab5', '104542', '278605', '195646', '1eef92', '624716', '67143a'],
        'time': 1.86},
    'sensor_03': {
        'data': ['c8050e', 'ed40ef', '171cc2', '784d63', '8b34fa', '781359', '331a3e', 'd13a32', 'e97cc3', '1667ba'],
        'time': 2.96},
    'sensor_28': {
        'data': ['d2595c', '78740f', '8f3507', 'ea78d6', 'ebc569', '3818c4', 'fa1f6c', '5fc388', '025779', '8592fb'],
        'time': 1.04},
    'sensor_31': {
        'data': ['67efee', '091f4f', '87fd73', '12742b', 'c9c2de', 'd81a22', '5343cf', '4b0ab0', '1468eb', '41e493'],
        'time': 0.57},
    'sensor_50': {
        'data': ['106bfe', '76817d', 'aa21d4', '5f126b', '8e1997', '0f2e21', '33bbb4', '4309d2', '564a93', '0241d4'],
        'time': 1.31},
    'sensor_01': {
        'data': ['a043ba', 'e16038', '03a839', 'c0cb52', 'f511d9', 'cb8f68', 'd9d9b0', '341314', 'a5534e', 'a92b26'],
        'time': 2.97},
    'sensor_14': {
        'data': ['d4c6e8', 'd449f7', '285887', '53b93c', '0bbc6a', 'df7089', 'dd787b', '6a27f5', 'baddd6', '5bcd01'],
        'time': 1.97},
    'sensor_30': {
        'data': ['43b55e', 'c41a6f', 'dfc44b', '574738', 'eb2993', 'a8a06b', '1c08e6', 'ee73f5', 'ae198b', 'ee2e2e'],
        'time': 2.99},
    'sensor_32': {
        'data': ['2b9687', '8a33cd', '17b190', '889258', '13918c', '78707c', 'b6db90', '51fe1e', '06ccfa', '6f6de6'],
        'time': 2.11},
    'sensor_18': {
        'data': ['520b8b', '7c818f', '0cd87f', '076a7e', '11914a', '85f879', '1bdacb', '373576', '16a52e', '1d11bc'],
        'time': 1.76}, 'sensor_11': {
        'data': ['b49786', 'b5b441', '318c23', '7bf841', '332084', 'f8b2d7', 'd97720', 'f7d61a', '0294f1', 'c9c387'],
        'time': 1.44},
    'sensor_49': {
        'data': ['bed509', 'ecddf5', 'f61422', 'fcfa2f', 'bec392', '4b2bff', '6ff09e', 'f39e2b', '3f2e1b', 'ae7431'],
        'time': 0.92},
    'sensor_34': {
        'data': ['ac5626', 'c7d4bc', 'e8f823', '3aed1b', '34a9d3', 'cb87d5', 'f0ef1f', '7393e8', 'c68548', '71f7de'],
        'time': 1.24},
    'sensor_42': {
        'data': ['a79467', 'ae184e', '5f50cb', 'b7a518', '3634d5', '9975a0', '1c71d7', '0f3b2a', '2e4a45', 'e264b3'],
        'time': 2.04},
    'sensor_21': {
        'data': ['9ca2c7', 'cc7e9a', '9da217', '440847', '0d1dd9', '878ce7', 'ca5720', '1e5b82', '377825', '4659ca'],
        'time': 0.38},
    'sensor_05': {
        'data': ['3b36a4', '5c17ff', '134eee', '52db9f', 'a0d4af', '211849', 'b3a47e', 'd1640c', 'a4b860', '1ee8d9'],
        'time': 0.61},
    'sensor_16': {
        'data': ['5a9aba', 'daea47', '9b14b2', '28f8ed', '4d7cb5', '1f2fdb', 'ffc5c0', '87aa9d', 'f130e8', 'e31de4'],
        'time': 1.34},
    'sensor_24': {
        'data': ['c71e90', '832693', '6a1f18', '8f867a', 'f40c5b', 'acb508', 'd2c7ba', 'c1c740', '30e8f8', '4c35cd'],
        'time': 1.13},
    'sensor_39': {
        'data': ['1ca5a0', 'fa6cf6', '048899', '76c985', '016f1f', '247377', '7b54c1', 'daa2f3', '228f36', '2a6093'],
        'time': 1.86},
    'sensor_44': {
        'data': ['798ffe', '2d95ac', 'fc0140', '0c8a86', 'b18944', '83c86a', 'da1bbd', '016794', 'bb1bb2', 'f8cb22'],
        'time': 2.39}
}


def space_time(sensor_name: str) -> int | float:
    return all_data_dict[sensor_name]['time']


def space_data(sensor_name: str) -> list:
    return all_data_dict[sensor_name]['data']


async def sensor_data(sensor_name: str) -> str:
    await asyncio.sleep(space_time(sensor_name))
    return sensor_name + '_data: ' + ''.join(space_data(sensor_name))


async def main() -> list:
    tasks = [sensor_data(sensor) for sensor in sorted(sensors)]
    results = [f'Результаты проведения теста типа {test_type}:']
    results.extend(await asyncio.gather(*tasks))
    return results


if __name__ == '__main__':
    print(asyncio.run(main()))
