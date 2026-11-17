# FAQ

This section collects common questions and solutions about building the SDK, using the system and developing applications, to help you troubleshoot quickly.

## Can key modes such as photo, video recording, small-image snapshot, media transfer and live streaming run at the same time?

No. Photo, video recording, small-image snapshot, media transfer and live streaming each run as a single fast-boot session, and each needs its own power-on and power-off cycle.

## Can commands such as setting the time or querying the amount of data on the SD card run at the same time?

Yes. These auxiliary commands can be sent together with a mode command.

## How do I decide where to place the gyroscope relative to the camera?

The gyroscope must be in the same vertical plane as the camera. You can design the mechanics with the two mounted back to back.

## How do I configure the baud rate of the communication serial port?

On the Linux command line, set the baud rate with `stty -F /dev/ttyUSB0 115200`. Replace `/dev/ttyUSB0` with your serial device node and `115200` with the baud rate you need.

The following reference code configures the baud rate in a Linux application:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <termios.h>
#include <sys/select.h>

int configure_serial_port(int fd, int baudrate) {
    struct termios tty;

    // Get the current serial port configuration
    if (tcgetattr(fd, &tty) != 0) {
        perror("tcgetattr");
        return -1;
    }

    // Set the baud rate
    speed_t speed;
    switch (baudrate) {
        case 9600:   speed = B9600;   break;
        case 19200:  speed = B19200;  break;
        case 38400:  speed = B38400;  break;
        case 57600:  speed = B57600;  break;
        case 115200: speed = B115200; break;
        case 230400: speed = B230400; break;
        case 460800: speed = B460800; break;
        case 921600: speed = B921600; break;
        default:     speed = B115200; break;
    }

    cfsetispeed(&tty, speed);  // Input baud rate
    cfsetospeed(&tty, speed);  // Output baud rate

    // 8-bit characters
    tty.c_cflag &= ~CSIZE;
    tty.c_cflag |= CS8;
    // No parity
    tty.c_cflag &= ~PARENB;
    // 1 stop bit
    tty.c_cflag &= ~CSTOPB;
    // No hardware flow control
    tty.c_cflag &= ~CRTSCTS;
    // Enable the receiver
    tty.c_cflag |= CREAD | CLOCAL;

    // Disable canonical mode and other special processing
    tty.c_lflag &= ~ICANON;
    tty.c_lflag &= ~ECHO;
    tty.c_lflag &= ~ECHOE;
    tty.c_lflag &= ~ISIG;

    // Disable software flow control
    tty.c_iflag &= ~(IXON | IXOFF | IXANY);
    tty.c_iflag &= ~(ICRNL | INLCR);

    // Raw output mode
    tty.c_oflag &= ~OPOST;

    // Set the timeout
    tty.c_cc[VMIN] = 0;   // Minimum number of characters
    tty.c_cc[VTIME] = 5;  // Timeout (0.5 s)

    // Flush the input and output buffers
    tcflush(fd, TCIOFLUSH);

    // Apply the new configuration
    if (tcsetattr(fd, TCSANOW, &tty) != 0) {
        perror("tcsetattr");
        return -1;
    }

    return 0;
}

int main() {
    int serial_fd;
    char buffer[256];
    ssize_t bytes_read;

    // Open the serial device
    serial_fd = open("/dev/ttyUSB0", O_RDWR | O_NOCTTY);
    if (serial_fd < 0) {
        perror("open");
        return -1;
    }

    // Configure the serial port
    if (configure_serial_port(serial_fd, 115200) < 0) {
        close(serial_fd);
        return -1;
    }

    printf("Serial port configured, baud rate: 115200\n");

    // Send data
    const char *message = "Hello Serial!\n";
    write(serial_fd, message, strlen(message));

    // Receive data
    while (1) {
        bytes_read = read(serial_fd, buffer, sizeof(buffer) - 1);
        if (bytes_read > 0) {
            buffer[bytes_read] = '\0';
            printf("Received: %s", buffer);
        }
        usleep(10000); // 10 ms delay
    }

    close(serial_fd);
    return 0;
}
```
