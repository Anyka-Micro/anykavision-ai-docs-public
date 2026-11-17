# FAQ

本部分汇总 SDK 编译、系统使用及开发过程中的常见问题与解决方法，便于快速排查。

## 拍照、录像、小图抓拍、导图、直播等关键模式是否能一起执行？

不能一块执行，拍照、录像、小图抓拍、导图、直播都是单次执行快启完成的，需要独立上下电过程。

## 时间设置指令、查询sd文件数据量等可否同时执行？

附加的指令可以跟模式指令一块执行。

## 陀螺仪摆放位置与摄像头摆放位置如何确认？

需跟摄像头同一垂直平面，可以采用背对背的方式进行结构设计。

## 怎么配置通信串口波特率？

Linux 命令行配置串口波特率的命令是 `stty -F /dev/ttyUSB0 115200`, 根据需要替换 `/dev/ttyUSB0` 串口设备节点 和 `115200` 波特率值。

Linux应用编程配置串口波特率的参考代码如下：

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

    // 获取当前串口配置
    if (tcgetattr(fd, &tty) != 0) {
        perror("tcgetattr");
        return -1;
    }

    // 设置波特率
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

    cfsetispeed(&tty, speed);  // 输入波特率
    cfsetospeed(&tty, speed);  // 输出波特率

    // 设置字符大小为8位
    tty.c_cflag &= ~CSIZE;
    tty.c_cflag |= CS8;
    // 无奇偶校验
    tty.c_cflag &= ~PARENB;
    // 1个停止位
    tty.c_cflag &= ~CSTOPB;
    // 无硬件流控
    tty.c_cflag &= ~CRTSCTS;
    // 启用接收器
    tty.c_cflag |= CREAD | CLOCAL;

    // 禁用规范模式和其他特殊处理
    tty.c_lflag &= ~ICANON;
    tty.c_lflag &= ~ECHO;
    tty.c_lflag &= ~ECHOE;
    tty.c_lflag &= ~ISIG;

    // 禁用软件流控
    tty.c_iflag &= ~(IXON | IXOFF | IXANY);
    tty.c_iflag &= ~(ICRNL | INLCR);

    // 原始输出模式
    tty.c_oflag &= ~OPOST;

    // 设置超时
    tty.c_cc[VMIN] = 0;   // 最小字符数
    tty.c_cc[VTIME] = 5;  // 超时时间(0.5秒)

    // 清空输入输出缓冲区
    tcflush(fd, TCIOFLUSH);

    // 应用新的配置
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

    // 打开串口设备
    serial_fd = open("/dev/ttyUSB0", O_RDWR | O_NOCTTY);
    if (serial_fd < 0) {
        perror("open");
        return -1;
    }

    // 配置串口
    if (configure_serial_port(serial_fd, 115200) < 0) {
        close(serial_fd);
        return -1;
    }

    printf("串口配置完成，波特率: 115200\n");

    // 发送数据
    const char *message = "Hello Serial!\n";
    write(serial_fd, message, strlen(message));

    // 接收数据
    while (1) {
        bytes_read = read(serial_fd, buffer, sizeof(buffer) - 1);
        if (bytes_read > 0) {
            buffer[bytes_read] = '\0';
            printf("接收到: %s", buffer);
        }
        usleep(10000); // 10ms延时
    }

    close(serial_fd);
    return 0;
}
```
