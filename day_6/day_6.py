
FILE_NAME = 'input.txt'
PACKET_MARKER = 14


def check_marker(marker):
    return len(set(marker)) == PACKET_MARKER


def main():
    with open(FILE_NAME) as file:
        packet = file.readline()

    i = 0
    while i + PACKET_MARKER <= len(packet) - 1:
        marker = packet[i:i+PACKET_MARKER]
        if check_marker(marker):
            print(f'Marker: {marker}, Marker Pos: {i + PACKET_MARKER}')
            break
        i += 1


if __name__ == '__main__':
    main()
