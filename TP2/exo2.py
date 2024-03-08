import time


def syracuse1(n):
    if n == 1:
        return [[1], 0, 1]

    if n % 2 == 0:
        sequence, temps_de_vol, altitude_maximale = syracuse1(n // 2)
    else:
        sequence, temps_de_vol, altitude_maximale = syracuse1(3 * n + 1)

    sequence = [n] + sequence

    temps_de_vol += 1
    altitude_maximale = max(altitude_maximale, n)

    return [sequence, temps_de_vol, altitude_maximale]


def syracuse2(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return 1 + syracuse2(n // 2)

    else:
        return 1 + syracuse2(3 * n + 1)


if __name__ == '__main__':
    # syracuse1_result = syracuse1(28)
    # print('liste:', syracuse1_result[0])
    # print('temps de vol:', syracuse1_result[1])
    # print('altitude maximale:', syracuse1_result[2])
    #
    # print('temps de vol avec syracuse2:', syracuse2(28))

    start_time = time.time()

    for i in range(1, 10 ** 6):
        syracuse2(i)

    end_time = time.time()

    print('Time taken:', end_time - start_time)

